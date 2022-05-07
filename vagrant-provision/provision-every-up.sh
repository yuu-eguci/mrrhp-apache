#!/bin/sh

# NOTE: mariadb は vagrant halt ごとに閉じてしまいます。
#       開発前にオープンするための provision です。
sudo systemctl start mariadb.service
sudo setenforce 0
sudo apachectl restart
