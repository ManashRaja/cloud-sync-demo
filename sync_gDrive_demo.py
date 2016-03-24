#!/usr/bin/python
import pexpect

print "Starting Google Drive Auth"
child = pexpect.spawn('rclone config')
child.expect('e/n/d/s/q>')
child.sendline('n')
child.expect('name>')
child.sendline('cloud')
child.expect('Storage>')
child.sendline('6')
child.expect('client_id>')
child.sendline('')
child.expect('client_secret')
child.sendline('')
child.expect('y/n>')
child.sendline('y')
child.expect('y/e/d>')
child.sendline('y')
child.expect('e/n/d/s/q>')
child.sendline('q')
print "Google Drive Auth complete"
print "Syncing Data folder of Browser activity (/usr/share/sugar/activities/Browse.activity/data) with Google Drive at backup/Browse"
sync = pexpect.spawn('rclone copy /usr/share/sugar/activities/Browse.activity/data cloud:backup/Browse')
sync.expect('Elapsed')
print "Done"
