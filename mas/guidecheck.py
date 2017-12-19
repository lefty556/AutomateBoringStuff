#! /usr/bin/python

# This program checks for any failure to uncompress guide files
# downloaded from Gracenote's ftp site
# The script sshs into mbo-05 and checks the GuideManager logs
# for any server in mbo-05.txt

import subprocess
import os
import commands

site = ''
ip = ''

# Get fresh MAS MBO-05 host and IP list
ohosts = "ohosts -v mbo-05 | awk '{print $2, $4}'"
servers = commands.getoutput(ohosts)
server_info = {}

for line in servers.split('\n'):
    site, ip = line.split()
    server_info[site] = ip


# Connect to each server and run grep for error

COMMAND="grep 'ERROR.*Failed to uncompress' /usr/local/mystro/logs/Guide*"
total = 0
brokelist = []
for site, ip in server_info.items():
    ip ='mystro@' + ip.strip()

    # Ports are handled in ~/.ssh/config since we use OpenSSH
    ssh = subprocess.Popen(["ssh", "%s" % ip, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result:
        print 'From site %s (%s):' % (site, ip)
        print ''.join(result)
        total += 1
        brokelist.append(site)

print 'Total Number of Sites impacted: ' + str(total)
print 'Site(s) Impacted:'
print '\n'.join(brokelist)
