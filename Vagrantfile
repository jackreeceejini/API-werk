# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provision :shell, path: "pg_config.sh"
  config.vm.box = "bento/ubuntu-16.04-i386"
  config.vm.network "forwarded_port", guest: 5000, host: 5070
  config.vm.network :forwarded_port, guest: 6379, host: 6380

  
  # Work around disconnected virtual network cable.
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--cableconnected1", "on"]

  $script = <<-SCRIPT
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install -y redis-server
  sudo mv /etc/redis/redis.conf /etc/redis/redis.conf.old
  echo "bind 0.0.0.0" | sudo tee /etc/redis/redis.conf
  cat /etc/redis/redis.conf.old | grep -v bind | sudo tee -a /etc/redis/redis.conf
  sudo service redis-server restart
  date > /etc/vagrant_provisioned_at
  SCRIPT
  config.vm.provision :shell, inline: $script
  end
end
