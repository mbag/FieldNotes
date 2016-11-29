Add static route on *nix
========================

On Centos 6.8
+++++++++++++

To add static route add following line to file `/etc/sysconfig/network`:
```
GATEWAY=192.168.1.1
```
this will make the route permanent across reboots, however you can also add default route using standard route command:
```
route add default gw 192.168.1.1
```


On SmartOS/Solaris
++++++++++++++++++
Prior to Solaris 11 the /etc/defaultrouter was used, but nowadays `route` command with `-p` is used:
```
route -p add default 192.168.1.1
```
`-p` makes this change permanent across reboots.

