#!/bin/sh

# windows10でやる場合、errno 71 protocol error が出る。
# Powershellを管理者権限で開くことで解決する。Winは相変わらず面倒。

echo '----- Preparation -----'
yum update -y
yum install -y yum-utils
yum groupinstall -y development

echo '----- Install Apache -----'
yum install -y httpd httpd-devel
httpd -v

echo '----- Install Mariadb -----'
touch     /etc/yum.repos.d/MariaDB.repo
chmod 777 /etc/yum.repos.d/MariaDB.repo
echo "# MariaDB 10.3 CentOS repository list - created 2018-05-12 03:19 UTC" >  /etc/yum.repos.d/MariaDB.repo
echo "# http://downloads.mariadb.org/mariadb/repositories/"                 >> /etc/yum.repos.d/MariaDB.repo
echo "[mariadb]"                                                            >> /etc/yum.repos.d/MariaDB.repo
echo "name = MariaDB"                                                       >> /etc/yum.repos.d/MariaDB.repo
echo "baseurl = http://yum.mariadb.org/10.3/centos7-amd64"                  >> /etc/yum.repos.d/MariaDB.repo
echo "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB"                   >> /etc/yum.repos.d/MariaDB.repo
echo "gpgcheck=1"                                                           >> /etc/yum.repos.d/MariaDB.repo
yum install -y MariaDB-server MariaDB-client
mysqld --version
systemctl start mysqld
mysqladmin -u root password 'password'

# README に書くけどこのあとこれを手打ちする必要ある。
# $ sudo mysql -u root -p
# password
# MariaDB > SET character_set_database=utf8;
# MariaDB > SET character_set_server=utf8;
# MariaDB > create database app;
# MariaDB > exit

echo '----- Install Python -----'
yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum install -y python36u python36u-libs python36u-devel python36u-pip
python -V
python3.6 -V

echo '----- Make Python3.6 environment -----'
cd /vagrant/
python3.6 -m venv env3.6
source /vagrant/env3.6/bin/activate

echo '----- Pip -----'
pip install --upgrade pip setuptools
pip install -r requirements.txt

# 参考: 【Django】Apacheとmod_wsgi環境でDjango2を使う方法を解説 – CentOS7
#     https://it-engineer-lab.com/archives/161

echo '----- Create django.conf -----'
touch /etc/httpd/conf.d/django.conf
chmod 777 /etc/httpd/conf.d/django.conf
chmod 777 /var/www
# Python パスの設定。
echo "WSGIPythonHome     /vagrant/env3.6"                                      >  /etc/httpd/conf.d/django.conf
echo "WSGIPythonPath     /vagrant:/vagrant/env3.6/lib/python3.6/site-packages" >> /etc/httpd/conf.d/django.conf
echo "Alias /robots.txt  /var/www/static/robots.txt"                           >> /etc/httpd/conf.d/django.conf
echo "Alias /favicon.ico /var/www/static/favicon.ico"                          >> /etc/httpd/conf.d/django.conf
echo "Alias /media/      /vagrant/media/"                                      >> /etc/httpd/conf.d/django.conf
echo "Alias /static/     /var/www/static/"                                     >> /etc/httpd/conf.d/django.conf
echo "<Directory /var/www/static>"                                             >> /etc/httpd/conf.d/django.conf
echo "    Require all granted"                                                 >> /etc/httpd/conf.d/django.conf
echo "</Directory>"                                                            >> /etc/httpd/conf.d/django.conf
echo "<Directory /vagrant/media>"                                              >> /etc/httpd/conf.d/django.conf
echo "    Require all granted"                                                 >> /etc/httpd/conf.d/django.conf
echo "</Directory>"                                                            >> /etc/httpd/conf.d/django.conf
# wsgi の設定。
echo "WSGIScriptAlias    / /vagrant/config/wsgi.py"                            >> /etc/httpd/conf.d/django.conf
echo "<Directory /vagrant/config>"                                             >> /etc/httpd/conf.d/django.conf
echo "    <Files wsgi.py>"                                                     >> /etc/httpd/conf.d/django.conf
echo "        Require all granted"                                             >> /etc/httpd/conf.d/django.conf
echo "    </Files>"                                                            >> /etc/httpd/conf.d/django.conf
echo "</Directory>"                                                            >> /etc/httpd/conf.d/django.conf

echo '----- Create mod_wsgi.conf -----'
# venv環境内soのパスを書く。
find /vagrant/env3.6 -name 'mod_wsgi*.so'
touch /etc/httpd/conf.modules.d/mod_wsgi.conf
chmod 777 /etc/httpd/conf.modules.d/mod_wsgi.conf
echo "LoadModule wsgi_module /vagrant/env3.6/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so" > /etc/httpd/conf.modules.d/mod_wsgi.conf

echo '----- Start apache -----'
apachectl start
