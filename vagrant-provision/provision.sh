#!/bin/sh

# windows10でやる場合、errno 71 protocol error が出る。
# Powershellを管理者権限で開くことで解決する。Winは相変わらず面倒。

echo '----- Firewall setting -----'
systemctl restart firewalld  # Vagrant 環境のとき最初は起動してない。
firewall-cmd --add-service=http  --zone=public --permanent
firewall-cmd --add-service=https --zone=public --permanent
systemctl restart firewalld

echo '----- Preparation -----'
yum makecache fast
yum update -y
yum install -y yum-utils
yum groupinstall -y development

echo '----- Install Apache -----'
yum install -y httpd httpd-devel
httpd -v

echo '----- Install Mariadb -----'
touch     /etc/yum.repos.d/MariaDB.repo
chmod 777 /etc/yum.repos.d/MariaDB.repo
cat << __EOF__ > /etc/yum.repos.d/MariaDB.repo
# MariaDB 10.3 CentOS repository list - created 2018-05-12 03:19 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.3/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1
__EOF__
yum install -y MariaDB-server MariaDB-client
mysqld --version
systemctl start mysqld
mysqladmin -u root password 'password'

echo '----- Initial settings for Mariadb -----'
mysql -u root -ppassword << __EOF__
SET character_set_database=utf8;
SET character_set_server=utf8;
CREATE DATABASE app;
GRANT ALL PRIVILEGES ON *.* TO root@'192.168.33.1' IDENTIFIED BY 'password';
__EOF__

echo '----- Install Python -----'
yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum install -y python36u python36u-libs python36u-devel python36u-pip
python -V
python3.6 -V

echo '----- Make Python3.6 environment -----'
mkdir /vagrant/
cd /vagrant/
python3.6 -m venv env3.6
source /vagrant/env3.6/bin/activate

echo '----- Pip -----'
pip install --upgrade pip setuptools
pip install -r requirements.txt

# 参考: 【Django】Apacheとmod_wsgi環境でDjango2を使う方法を解説 – CentOS7
#     https://it-engineer-lab.com/archives/161

echo '----- Create django.conf -----'
touch     /etc/httpd/conf.d/django.conf
chmod 777 /etc/httpd/conf.d/django.conf
chmod 777 /var/www
cat << __EOF__ > /etc/httpd/conf.d/django.conf
WSGIPythonHome     /vagrant/env3.6
WSGIPythonPath     /vagrant:/vagrant/env3.6/lib/python3.6/site-packages
Alias /robots.txt  /var/www/static/robots.txt
Alias /favicon.ico /var/www/static/favicon.ico
Alias /media/      /vagrant/media/
Alias /static/     /var/www/static/
<Directory /var/www/static>
    Require all granted
</Directory>
<Directory /vagrant/media>
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
# venv環境内soのパスを書く。
find /vagrant/env3.6 -name 'mod_wsgi*.so'
touch     /etc/httpd/conf.modules.d/mod_wsgi.conf
chmod 777 /etc/httpd/conf.modules.d/mod_wsgi.conf
cat << __EOF__ > /etc/httpd/conf.modules.d/mod_wsgi.conf
LoadModule wsgi_module /vagrant/env3.6/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so
__EOF__

echo '----- Django startup -----'
python /vagrant/manage.py migrate --settings=config.settings.production
python /vagrant/manage.py collectstatic -c --noinput
python /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production

echo '----- Start apache -----'
apachectl start

echo '----- Auto start -----'
systemctl enable httpd.service
