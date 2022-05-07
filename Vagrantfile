# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.network "forwarded_port", guest: 80, host: 1991
  config.vm.hostname = "django.local"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision :shell, :privileged => false, :path => "vagrant-provision/provision.sh"
  config.vm.provision :shell, :privileged => false, :path => "vagrant-provision/provision-every-up.sh", :run => "always"
end
