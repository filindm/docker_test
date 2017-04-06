$script = <<SCRIPT
apt-get install -y software-properties-common python-software-properties apt-transport-https
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
apt-get update
apt-cache policy docker-engine
apt-get install -y docker-engine docker-compose
systemctl status docker
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = "kaorimatz/ubuntu-16.04-amd64"
    config.vm.network :forwarded_port, guest: 5000, host: 5000, auto_correct: true
    config.vm.provider "virtualbox" do |v|
        v.name = "Docker Test"
        v.customize ["modifyvm", :id, "--memory", "1024"]
    end
    config.vm.box_check_update = false
    config.vm.provision "shell", inline: $script
end
