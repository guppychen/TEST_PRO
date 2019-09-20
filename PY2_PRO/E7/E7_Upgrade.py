# -*- coding: utf-8 -*-

import common_tools, sys, time, os

port = '22'
username = 'sysadmin'
password = 'sysadmin'
ssh_flag = 0
get_version_flag = 0
update_time = 360
reboot_time = 360
ip = raw_input("Please input E7 shelf ip: ")


def Get_Version(chan, my1flag):
    str_version = "details"
    try:
        time.sleep(5)
        chan.send('show version' + '\n')  # 输入命令
        time.sleep(2)
        result = chan.recv(65535)  # 得到命令返回的结果
        print result
        # 从details开始查找并截取版本号
        version_pos = result.index(str_version)
        version = result[version_pos+21:version_pos+38]
        print '*' * 60
        print "System version is    : %s" % version
        print "E7 shelf ip is       : %s" % ip
        return version

    except Exception, e:
        print e
        my1flag += 1
        time.sleep(5)
        if my1flag < 3:
            Get_Version(chan, my1flag)
        print '\n' * 3
        os.system("pause")
        sys.exit()

def judge():
    next = raw_input("Do you want to upgrade ? 'y' or 'n' : " )
    if next == 'y' or next == 'Y' :
        print "Please follow next steps to upgrade."
        print '*' * 60
    elif next == 'n' or next == 'N' :
        print '*' * 60
        print '\n' * 3
        os.system("pause")
        sys.exit()
    else :
        print "Input invalid, please input again."
        judge()

def Upgrade_Version(chan, my1flag):
    status_check = 'in progress'
    try:
        time.sleep(5)
        url = raw_input('Please input new build url : ')
        chan.send('upgrade activate filename ' + url + '\n')  # 输入命令
        time.sleep(5)
        chan.send('show upgrade status\n')
        time.sleep(2)
        result = chan.recv(65535)  # 得到命令返回的结果
        print result
        if status_check in result:
            print '*' * 60
            print "Upgrade in progress, please wait till finished."
            common_tools.bar(update_time)
            print "\nInstall finished."
            print '*' * 60
        else:
            print '*' * 60
            print "Upgrade failed, please check url and try again."
            print '\n' * 3
            os.system("pause")
            sys.exit()

    except Exception, e:
        print e
        my1flag += 1
        time.sleep(5)
        if my1flag < 3:
            Upgrade_Version(chan, my1flag)
        print '\n' * 3
        os.system("pause")
        sys.exit()

def reload(chan, my1flag):
    try:
        time.sleep(5)
        chan.send('show upgrade status\n')
        time.sleep(5)
        chan.send(' \n' * 5)
        chan.send('reload all\n')  # 输入命令
        time.sleep(2)
        chan.send('y' + '\n' * 2)
        time.sleep(2)
        result = chan.recv(65535)  # 得到命令返回的结果
        print result
        print "System is rebooting now, please wait ......"
        common_tools.bar(reboot_time)

    except Exception, e:
        print e
        my1flag += 1
        time.sleep(5)
        if my1flag < 3:
            Upgrade_Version(chan, my1flag)
        print '\n' * 3
        os.system("pause")
        sys.exit()

def main():
    if common_tools.check_ip(ip) == True:
        pass
    else:
        print "IP address is illegally, please check !"
        os.system("pause")
        sys.exit()
    chan_get = common_tools.ssh_login(ip, port, username, password, ssh_flag)
    pre_version = Get_Version(chan_get, get_version_flag)

    judge()

    chan_set = common_tools.ssh_login(ip, port, username, password, ssh_flag)
    Upgrade_Version(chan_set, get_version_flag)

    chan_reload = common_tools.ssh_login(ip, port, username, password, ssh_flag)
    reload(chan_reload, get_version_flag)

    print "\nCheck version now......"
    chan_get2 = common_tools.ssh_login(ip, port, username, password, ssh_flag)
    current_version = Get_Version(chan_get2, get_version_flag)
    if pre_version != current_version:
        print "Previous version : %s" % pre_version
        print "Current version  : %s" % current_version
        print '*' * 60
        print "Upgrade successful ! Congratulations !"
    else:
        print "Previous version : %s" % pre_version
        print "Current version  : %s" % current_version
        print '*' * 60
        print "Upgrade the same build ? Please try again !"
    print '\n' * 3
    os.system("pause")
    sys.exit()

if __name__ == '__main__':
    sys.exit(main())

