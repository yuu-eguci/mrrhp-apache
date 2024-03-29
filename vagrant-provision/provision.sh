#!/bin/sh

# エラーが発生したら exit します。
# NOTE: provision 中にエラーが発生し、どれかのコマンドがインストールできなかったとき
#       問題の認識をやりやすくするため。
set -e

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
# python3-devel がないと mod_wsgi が入らない。
sudo yum install python3 python3-devel -y
which python
which python3.6

echo '----- Create Python3.6 environment -----'
sudo python3.6 -m venv /env3.6  # python3.6仮想環境はルートに作ることにする。
# sudo だと source /env3.6/bin/activate が使えないので /env3.6/bin/python3.6 を直接使います。
sudo which /env3.6/bin/python3.6

# なんか Vagrant では yum で取得する pip に異常があるので別途仮想python3.6環境内へインストール。(ImportError main)
echo '----- Install pip -----'
sudo curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o /get-pip.py
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

# ふたつの VirtualHost ディレクティブによって、
# http については "localhost" からのアクセスのみ許可する設定です。
# XXX: なぜかこの設定で https://www.mrrhp.com も deny される。なんでや。
<VirtualHost *:80>
    ServerName any
    <Location />
        Require all denied
    </Location>
</VirtualHost>
<VirtualHost *:80>
    ServerName localhost
    <Directory /vagrant/config>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>

# ふたつの VirtualHost ディレクティブによって、
# https については "www.mrrhp.com" からのアクセスのみ許可する設定です。
# NOTE: これらのディレクティブは https 環境 (本番) でコメント解除してください。
#       いや、環境構築用の設定は別であるべきなんだけれど、 MrrhpApache では
#       知見をすべてコードに突っ込むコンセプトで進んでいるので。
# <VirtualHost *:443>
#     ServerName any
#     SSLEngine on
#     SSLCertificateFile /etc/letsencrypt/live/www.mrrhp.com/cert.pem
#     SSLCertificateKeyFile /etc/letsencrypt/live/www.mrrhp.com/privkey.pem
#     SSLCertificateChainFile /etc/letsencrypt/live/www.mrrhp.com/chain.pem
#     <Location />
#         Require all denied
#     </Location>
# </VirtualHost>
# <VirtualHost *:443>
#     ServerName www.mrrhp.com
#     SSLEngine on
#     SSLCertificateFile /etc/letsencrypt/live/www.mrrhp.com/cert.pem
#     SSLCertificateKeyFile /etc/letsencrypt/live/www.mrrhp.com/privkey.pem
#     SSLCertificateChainFile /etc/letsencrypt/live/www.mrrhp.com/chain.pem
#     <Directory /vagrant/config>
#         <Files wsgi.py>
#             Require all granted
#         </Files>
#     </Directory>
# </VirtualHost>

<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE image/gif
    AddOutputFilterByType DEFLATE image/jpeg
    AddOutputFilterByType DEFLATE image/png
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/json
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>
__EOF__
# NOTE: ↑deflate は PageSpeed Insights の「テキスト圧縮の有効化」に対応するため導入しました。
#       が、有効になっているのかはよくわかりません。
#       次のふたつの module が有効になっている必要があるらしいです。
#       LoadModule filter_module modules/mod_filter.so
#       LoadModule deflate_module modules/mod_deflate.so

echo '----- Create mod_wsgi.conf -----'
# venv環境内soのパスを書く。find /env3.6 -name 'mod_wsgi*.so' でわかる。
sudo touch     /etc/httpd/conf.modules.d/mod_wsgi.conf
sudo chmod 777 /etc/httpd/conf.modules.d/mod_wsgi.conf
cat << __EOF__ > /etc/httpd/conf.modules.d/mod_wsgi.conf
LoadModule wsgi_module /env3.6/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so
WSGIPassAuthorization On
__EOF__

# Make a directory for django-axes loggging
echo '----- Mkdir -----'
sudo mkdir -m 777 /var/log/mrrhp-apache

echo '----- Django startup -----'
/env3.6/bin/python3.6 /vagrant/manage.py migrate --settings=config.settings.production
/env3.6/bin/python3.6 /vagrant/manage.py collectstatic -c --noinput --settings=config.settings.production
/env3.6/bin/python3.6 /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production

echo '----- Start apache -----'
sudo setenforce 0
sudo apachectl restart

echo '----- Auto start -----'
sudo systemctl enable httpd.service

# axes を追加したことで、パーミッションの変更が必要になりました。
# NOTE: これを設定しないと internal server error が発生します。
#       ちなみにそのときのログは sudo cat /var/log/httpd/error_log で参照できます。
sudo chmod 666 /var/log/mrrhp-apache/django-axes.log
sudo chmod 666 /var/log/mrrhp-apache/error.log
