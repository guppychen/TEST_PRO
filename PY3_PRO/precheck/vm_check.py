#!/usr/bin/env python
import paramiko

hostname = 'nancafe2-stptest-16'
username = 'cafetest'
password = 'cafetest'
vm_list = ['nancafe2-stptest-16','nancafe2-stptest-17','nancafe2-stptest-18','nancafe2-stptest-20','nanw-ontuser-10',\
           'nanw-ontuser-11','nanw-ontuser-15','nanw-ontuser-16','nanw-ontuser-17','nanw-ontuser-18','10.245.58.193',\
           '10.245.57.193']
agent_list = ['nancafe2-stptest-16','nancafe2-stptest-17','nancafe2-stptest-18','nancafe2-stptest-20']
port = 22
message = '0% packet loss'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def ping_test(vm_list):
    ssh.connect(hostname=hostname, port=port, username=username, password=password)
    index = 0
    for vm in vm_list:
        stdin, stdout, stderr = ssh.exec_command('ping %s -c 2' %vm)
        out = stdout.readlines()
        if len(out) > 5 and message in out[5]:
            print(vm + ' is reachable.')
            index += 1
        else:
            print(vm + ' is not reachable, please check !')
    if index == len(vm_list):
        print('vm check pass !')
    else:
        print('vm check fail !')
    ssh.close()

def agent_clean(agent_list):
    for agent in agent_list:
        ssh.connect(hostname=agent, port=port, username=username, password=password)
        ssh.exec_command('rm -rf /export/home/cafetest/*.img;rm -rf /export/home/cafetest/stp/results_*')
        stdin, stdout, stderr = ssh.exec_command('cd stp;ls')
        print(agent,stdout.readlines())
        ssh.close()
    print('agent is clean.')

ping_test(vm_list)
agent_clean(agent_list)