# -*- coding: utf-8 -*-

import paramiko
import time
import sys

port = '22'
username = 'sysadmin'
password = 'sysadmin'
ip = raw_input("Please input E7 shelf ip: ")
# ip = "10.137.14.204"

msg1flag = 0
cmd_flag = 0
commands = ['show version','show running ont','show running policy-map',\
            'show running class-map','show running snmp','show running vlan']
configs = ['ont','policy-map','class-map','snmp']
str = "No entries found"
str_vlan = "vlan"
str_version = "details"
str_nu = 4
str_vlan_nu = 2

# 核心方法，该方法连接远程主机并打开一个终端，并将该终端返回
def msg1(ip, port, username, password, flag):
    try:
        # 设置ssh连接的远程主机地址和端口
        t = paramiko.Transport(ip, port)
        # 设置登录名和密码
        t.connect(username=username, password=password)
        # 连接成功后打开一个channel
        chan = t.open_session()
        # 设置会话超时时间
        chan.settimeout(timeout=180)
        # 打开远程的terminal
        chan.get_pty()
        # 激活terminal
        chan.invoke_shell()
        print "Connection successful ! Wait ......"
        return chan
    except Exception, e:
        print e
        flag += 1
        time.sleep(5)
        if flag < 3:
            msg1(ip, port, username, password, flag)
        print "Connection failed !"
        raw_input("Press Enter key to exit")
        exit()




def mycmd(chan, my1flag):
    try:
        time.sleep(2)
        for command in commands:
            chan.send(command + '\n')  # 输入命令
        time.sleep(2)
        i = 1
        while i < 2:
            chan.send('\n')
            i += 1
        time.sleep(2)
        result = chan.recv(65535)  # 得到命令返回的结果
        # result_len = len(result)  # 得到结果字符串的长度
        # print result_len
        print result
        pos = result.count(str)
        pos1 = result.count("vlan")
        pos_version = result.index(str_version)
        version = result[pos_version+21:pos_version+38]
        print "*******************************************************"
        print "No entries number is : %d" % pos
        print "vlan number is       : %d" % (pos1 - 1)
        print "System version is    : %s" % version
        print "E7 shelf ip is       : %s" % ip
        if pos == str_nu and pos1 == str_vlan_nu:
            print """
            ***********************************************
            System is clean, you can start regression now !
            ***********************************************
            """
        else:
            print "*******************************************************"
            for config in configs:
                i = result.count(config)
                if i >= 2:
                    print "Please clear %s config !" % config
                else:
                    continue
            j = result.count("vlan")
            if j >= 3:
                print "Please clear vlan config(exclude vlan 999) !"
            print """
                     *******************************************************
                     System has residual configuration, please clear first !
                     *******************************************************
                     """
        return result

    except Exception, e:
        print e
        my1flag += 1
        time.sleep(5)
        if my1flag < 3:
            mycmd(chan, my1flag)
        raw_input('Press "Enter" key to exit')
        exit()


now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 时间
print now_time

def main():
    chan_ip_test = msg1(ip, port, username, password, msg1flag)
    mycmd(chan_ip_test, cmd_flag)
    raw_input('Press "Enter" key to exit')
    exit()

if __name__ == '__main__':
    sys.exit(main())