#!/usr/bin/python

import os,subprocess

print(os.popen("uname -a").read())

val=subprocess.Popen("ls -l /tmp; uptime", stdout=subprocess.PIPE, shell=True)
(output,error)=val.communicate()
print(output)

a=subprocess.Popen("echo Hello World",shell=True, stdout=subprocess.PIPE)
(output,error)=a.communicate()
print(output)
