# -*- mode: ruby -*-
# vi: set ft=ruby :

###########################################################################
# This configuration file is the starting point for understanding how the
# virtual machine is configured and provides a default provider that uses
# Virtualbox to provide virtualization. It also contains an *experimental*
# provider for using an AWS EC2 microinstance in the cloud. The AWS provider
# works but is a bit bleeding edge and incomplete from the standpoint of
# providing all of the functionality that it should at this time, so it should
# only be used by hackers who are comfortable working in the cloud. After
# filling in the necessary AWS credentials below use the --provider=aws
# option to use the AWS provider. See https://github.com/mitchellh/vagrant-aws
# for more details.
#
# See http://docs.vagrantup.com/v2/vagrantfile/index.html for additional
# details on Vagrantfile configuration in general.
###########################################################################

Vagrant.configure("2") do |config|

  # SSH forwarding: See https://help.github.com/articles/using-ssh-agent-forwarding
  config.ssh.forward_agent = true

  #########################################################################
  # Virtualbox configuration - the default provider for running a local VM
  #########################################################################

  config.vm.provider :virtualbox do |vb, override|

    # The Virtualbox image
    override.vm.box = "ubuntu/focal64"
    #override.vm.box_url = "http://files.vagrantup.com/precise64.box"

    # Port forwarding details

    # Note: Unfortunately, port forwarding currently is not implemented for
    # the AWS provider plugin, so you'll need to manually open them through the
    # AWS console or with the EC2 CLI tools. (It would be possible to do it
    # all through an additional Chef recipe that runs as part of MTSW2E, but
    # just isn't implemented yet.) Only port 8888 is essential
    # to initially access IPython Notebook and get started.

    # Pelican
    override.vm.network :forwarded_port, host: 8000, guest: 8000

  end

  #
  config.vm.provision "shell",
    inline: <<-SCRIPT
    # prepare dev enviroment
    echo 'Acquire::http { Proxy "192.168.1.2"; }' | sudo tee /etc/apt/apt.conf.d/01proxy
    sudo apt-get update
    sudo DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y python3-venv python3-wheel

    # install Pelican dependencies
    cd /vagrant
    python3 -m venv .
    source bin/activate
    python3 -m pip install --no-cache-dir -r requirements.txt

    SCRIPT

  config.vm.provision "shell",
    run: "always",
    inline: <<-SCRIPT2
    # start Pelican
    cd /vagrant
    source bin/activate
    echo "starting Pelican ..."
    nohup pelican -lr content/ -o output/ -s pelicanconf.py & sleep 1
    echo "Pelican started."
    SCRIPT2

end
