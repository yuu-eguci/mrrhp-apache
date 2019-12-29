# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "CentOS7.2"
  config.vm.box_url = "https://github.com/CommanderK5/packer-centos-template/releases/download/0.7.2/vagrant-centos-7.2.box"
  config.vm.network "forwarded_port", guest: 80, host: 1991
  config.vm.network "private_network", ip: "192.168.33.12"
  config.vm.hostname = "django.local"
  config.vm.synced_folder ".", "/vagrant"
  config.vm.provision :shell, privileged: false, :path => "vagrant-provision/provision.sh"
end
