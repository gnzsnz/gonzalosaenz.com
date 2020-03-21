Title: Manage remote VMs with virsh
Date: 2020-03-21
Modified: 2020-03-21
Category: Misc
Tags: virsh
Slug: Manage remote VMs with virsh
Authors: Gonzalo Saenz
Status: draft
Summary: This post will go through the steps to manage a VM running on a remote host with virsh.

The objective of this post is to describe the steps needed to manage a VM running on a remote KVM host.

Prerequisites:

* running KVM remote hypervisor
* have a remote VM on the hypervisor
* ssh access to the hypervisor

# Using virsh connect parameter

`virsh` can be used to manage VMs (and volumes, network, etc...) on the hypervisor. And this can be done when the hypervisor is a remote machine as well.

To achieve this, in the remote client you will run:
```sh
apt install libvirt-clients
virsh --connect qemu+ssh://devops@hypervisor:/system
```

This will connect to a remote host called `hypervisor` using ssh. Once you are connected you can do virsh stuff on it.

```
virsh # list
 Id    Name                           State
----------------------------------------------------
 1     VM1                            running
 2     VM2                            running

virsh # start VM3
Domain VM3 started

virsh # list
 Id    Name                           State
----------------------------------------------------
 1     VM1                            running
 2     VM2                            running
 3     VM3                            running

virsh # quit
```

## Automating the boring stuff

You can define your default hypervisor in libvirt configurations file `/etc/libvirt/libvirt.conf`

```sh
nano /etc/libvirt/libvirt.conf

uri_aliases = ["hypervisor=qemu+ssh://devops@hypervisor:/system"]
uri_default = "qemu+ssh://devops@hypervisor:/system"
```

Once you have defined your defaults you can manage your VMs with:
```sh
virsh
virsh --connect hypervisor
```

## References
* [virsh man page](https://manpages.ubuntu.com/manpages/bionic/man1/virsh.1.html)
* https://libvirt.org/remote.html
* https://libvirt.org/remote.html
* [Red Hat's excellent libvirt documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/chap-Remote_management_of_guests#form-Transport_modes-Remote_URIs)
