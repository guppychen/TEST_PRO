# -*- coding: utf-8 -*-

import time, paramiko, sys, os, re

# Check IP
def check_ip(ipAddr):
  compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\
                            \d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
  if compile_ip.match(ipAddr):
    return True
  else:
    return False

# This is progress bra function, input the bar time(second)
def bar(second):
# \r 表示将光标的位置回退到本行的开头位置■□
    jd = '\r[%s%s] [%d%%]'
    for i in range(60+1):
        a = '#' * i
        b = '.' * (60-i)
        c = (float(i) / 60) * 100
        print jd % (a,b,c),
        time.sleep(float(second) / 60)

# 核心方法，该方法连接远程主机并打开一个终端，并将该终端返回
def ssh_login(ip, port, username, password, flag):
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
            ssh_login(ip, port, username, password, flag)
        print "Connection failed, please check your input !\n\n\n"
        os.system("pause")
        sys.exit()



