#!/bin/sh

# windows10でやる場合、errno 71 protocol error が出る。
# Powershellを管理者権限で開くことで解決する。Winは相変わらず面倒。

echo '----- Firewall setting -----'
sudo systemctl restart firewalld  # Vagrant 環境のとき最初は起動してない。
sudo firewall-cmd --add-service=http  --zone=public --permanent
sudo firewall-cmd --add-service=https --zone=public --permanent
sudo firewall-cmd --add-service=mysql --zone=public --permanent
sudo systemctl restart firewalld

echo '----- Preparation -----'
yum makecache fast
sudo yum update -y
sudo yum install -y yum-utils
sudo yum groupinstall -y development

echo '----- Install Apache -----'
sudo yum install -y httpd httpd-devel
httpd -v

echo '----- Install Mariadb -----'
sudo touch     /etc/yum.repos.d/MariaDB.repo
sudo chmod 777 /etc/yum.repos.d/MariaDB.repo
cat << __EOF__ > /etc/yum.repos.d/MariaDB.repo
# MariaDB 10.3 CentOS repository list - created 2019-04-26 10:54 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.3/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
__EOF__
sudo yum install -y MariaDB-server MariaDB-client
mysqld --version
sudo systemctl start mariadb.service
mysqladmin -u root password 'password'

echo '----- Initial settings for Mariadb -----'
mysql -u root -ppassword << __EOF__
SET character_set_database=utf8;
SET character_set_server=utf8;
CREATE DATABASE app;
GRANT ALL PRIVILEGES ON *.* TO root@'192.168.33.1' IDENTIFIED BY 'password';
__EOF__

echo '----- Install Python -----'
sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm
sudo yum install -y python36u python36u-libs python36u-devel
which python
which python3.6

echo '----- Create Python3.6 environment -----'
sudo python3.6 -m venv /env3.6  # python3.6仮想環境はルートに作ることにする。
# sudo だと source /env3.6/bin/activate が使えないので /env3.6/bin/python3.6 を直接使います。
sudo which /env3.6/bin/python3.6

# なんか Vagrant では yum で取得する pip に異常があるので別途仮想python3.6環境内へインストール。(ImportError main)
echo '----- Install pip -----'
sudo curl https://bootstrap.pypa.io/get-pip.py -o /get-pip.py
sudo /env3.6/bin/python3.6 /get-pip.py
sudo rm /get-pip.py -f
sudo /env3.6/bin/python3.6 -m pip install --upgrade pip setuptools
sudo /env3.6/bin/python3.6 -m pip install -r /vagrant/requirements.txt

# 参考: 【Django】Apacheとmod_wsgi環境でDjango2を使う方法を解説 – CentOS7
#     https://it-engineer-lab.com/archives/161

echo '----- Create django.conf -----'
sudo touch     /etc/httpd/conf.d/django.conf
sudo chmod 777 /etc/httpd/conf.d/django.conf
sudo chmod 777 /var/www
mkdir -m 777 /var/www/media
mkdir -m 777 /var/www/media/markdownx
cat << __EOF__ > /etc/httpd/conf.d/django.conf
WSGIPythonHome     /env3.6
WSGIPythonPath     /vagrant:/env3.6/lib/python3.6/site-packages
Alias /robots.txt  /var/www/static/robots.txt
Alias /sitemap_index.xml  /var/www/static/sitemap_index.xml
Alias /sitemap_static.xml  /var/www/static/sitemap_static.xml
Alias /favicon.ico /var/www/static/favicon.ico
Alias /media/      /var/www/media/
Alias /static/     /var/www/static/
<Directory /var/www/static>
    Require all granted
</Directory>
<Directory /var/www/media>
    Require all granted
</Directory>
WSGIScriptAlias    / /vagrant/config/wsgi.py
<Directory /vagrant/config>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
__EOF__

echo '----- Create mod_wsgi.conf -----'
# venv環境内soのパスを書く。find /env3.6 -name 'mod_wsgi*.so' でわかる。
sudo touch     /etc/httpd/conf.modules.d/mod_wsgi.conf
sudo chmod 777 /etc/httpd/conf.modules.d/mod_wsgi.conf
cat << __EOF__ > /etc/httpd/conf.modules.d/mod_wsgi.conf
LoadModule wsgi_module /env3.6/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so
WSGIPassAuthorization On
__EOF__

echo '----- Django startup -----'
/env3.6/bin/python3.6 /vagrant/manage.py migrate --settings=config.settings.production
/env3.6/bin/python3.6 /vagrant/manage.py collectstatic -c --noinput --settings=config.settings.production
/env3.6/bin/python3.6 /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production

echo '----- Start apache -----'
sudo apachectl restart

echo '----- Auto start -----'
sudo systemctl enable httpd.service
