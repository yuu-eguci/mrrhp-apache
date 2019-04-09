Mrrhp Apache
===

## Installation

```
$ git clone https://gitlab.com/midori-mate/mrrhpapache.git
```


## Open on virtual environment

Install them.

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/)

```
$ vagrant up
$ vagrant ssh
```

In the virtual env.

```
$ source /vagrant/env3.6/bin/activate
$ python /vagrant/manage.py migrate
$ python /vagrant/manage.py createsuperuser
$ python /vagrant/manage.py collectstatic -c --noinput
$ sudo apachectl restart
```

Access [localhost:1991/](http://localhost:1991/) then.  
Access [localhost:1991/admin/](http://localhost:1991/admin/) as well.

Close the env.

```
$ exit
$ vagrant halt
```
