#!/bin/sh
wget "http://downloads.rclone.org/rclone-v1.28-linux-amd64.zip" &&
unzip rclone-v1.28-linux-amd64.zip &&
cd rclone-v1.28-linux-amd64 &&
sudo cp rclone /usr/sbin/ &&
sudo chown root:root /usr/sbin/rclone &&
sudo chmod 755 /usr/sbin/rclone &&

sudo pip install pexpect
