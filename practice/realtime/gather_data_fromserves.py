#!/usr/bin/python3

import paramiko,time
k=paramiko.RSAKey.from_private_key_file("./mykey.pem")
ssh= paramiko.SSHClient ()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
serverlist = open("servers.txt",'r')
for server in serverlist.readlines():
    ssh.connect(server.strip("\n"),username="ec2-user", pkey = k)
    print("-------------------- Executing code on",server.strip("\n"),"------")
    commands = ["df -hT","uname -a","ls -l /tmp"]
    for i in commands:
            stdin,stdout,stderr = ssh.exec_command(i)
            print("----------------- Executing commands",i, "----------------")
            stdout_str = stdout.read().decode('utf-8')
            time.sleep(2)
            print(stdout_str)
    ssh.close()
