Mrrhp Apache
===

![](media/media.jpg)

## Installation

https://github.com/yuu-eguci/mrrhp-docker


## Open on virtual environment THROUGH Apache

Install them.

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/)

And install vagrant-vbguest. I don't know if this is required or not tho.

```bash
vagrant plugin install vagrant-vbguest
```

You have to locate **.env** file next to manage.py file.

```plaintext
DATABASE_URL=mysql://root:password@localhost:3306/app
SLACK_WEBHOOK_URL=your-slack-webhook-url
```

**Windows user has to open Powershell as Administrator!** Or you cannot create symbolic links and setup will fail.

```bash
vagrant up
vagrant ssh
```

In the virtual env, do below to register yourself as a superuser.

```bash
sudo /env3.6/bin/python3.6 /vagrant/manage.py createsuperuser --settings=config.settings.production
```

Access [localhost:1991/](http://localhost:1991/) then.  
Access [localhost:1991/admin/](http://localhost:1991/admin/) as well.

When you wanna close the env.

```bash
exit
vagrant halt
```


## After tweaking static files

You have to check that there are no 404 files with `runserver` and through Apache as well.

Before checking through Apache you have to use these commands.

```bash
sudo /env3.6/bin/python3.6 /vagrant/manage.py collectstatic -c --noinput  --settings=config.settings.production
```

**Attention! If the file you tweak is style.css, don't forget to update GET query of it.**

And then you can commit!


## After /fixtures/initial_db_data.json is modified

You have to run the command below to register data to your own db.

```bash
sudo /env3.6/bin/python3.6 /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production
```


## Open DB on your virtual env with MySQLworkbench

```bash
vagrant ssh
```

```bash
sudo mysql -u root -p
password
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO root@'192.168.33.1' IDENTIFIED BY 'password';
```

Access through Workbench.

| Hostname      | Username | Password | Default Schema |
| ------------- | -------- | -------- | -------------- |
| 192.168.33.12 | root     | password | app            |

If you fail to access, check the error message to remake access user again.

```bash
MariaDB [(none)]> DROP USER 'root'@'192.168.33.1';
```

## Useful commands

```bash
source /env3.6/bin/activate
sudo apachectl restart
sudo systemctl restart mysqld
python /vagrant/manage.py makemigrations --settings=config.settings.production
python /vagrant/manage.py migrate --settings=config.settings.production

python /vagrant/manage.py dumpdata app.post app.tag app.year app.config -o /vagrant/fixtures/initial_db_data.json --indent 2 --settings=config.settings.production
python /vagrant/manage.py loaddata /vagrant/fixtures/initial_db_data.json --settings=config.settings.production

sudo tail -f /var/log/httpd/error_log
sudo tail -f /var/log/httpd/access_log

systemctl enable httpd.service
systemctl disable httpd.service
systemctl list-unit-files -t service | grep httpd
systemctl status firewalld.service
```
