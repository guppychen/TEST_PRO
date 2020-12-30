"""
    检查密码强度
"""

def check_num_in(password):
    is_num_in = False
    for i in password:
        if str.isnumeric(i):
            is_num_in = True
            break
    return is_num_in


def check_letter_in(password):
    is_letter_in = False
    for i in password:
        if str.isalpha(i):
            is_letter_in = True
            break
    return is_letter_in

def main():
    """
        main
    """
    try_times = 3
    while try_times > 0 :
        level = 0
        password = input('请输入密码：')
        if len(password) >= 8:
            level += 1
        else:
            print('密码必须大于8位！')
        if check_num_in(password):
            level += 1
        else:
            print('密码必须包含数字！')
        if check_letter_in(password):
            level += 1
        else:
            print('密码必须包含字母！')
        if level == 3:
            print('符合密码强度！您输入的密码为：{}'.format(password))
        try_times -= 1
    if try_times == 0:
        print('超出最大尝试次数！')


if __name__ == '__main__':
    main()
