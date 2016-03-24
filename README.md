# cloud-sync-demo

A demo prototype for third party cloud sync feature.  
This demo syncs the data folder of "Browse" activity (/usr/share/sugar/activities/Browse.activity/data)  
to "backup/Browse" folder on your Google Drive

Depends: rclone and pexpect

You can either install the above dependencies by running:  
`sudo ./install_rclone_pexpect.sh`

or Manually as below:  
Install rclone from http://www.rclone.org/install/  
Install pexect with : `pip install pexpect`

Usage:  
`./sync_gDrive_demo.py`
