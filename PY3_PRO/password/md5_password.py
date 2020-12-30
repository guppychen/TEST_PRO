"""
    md5保存用户密码
"""


import hashlib

user = {'Ace':'ed14ce9bf3b748c9ae8fc1f229bd28d0','Bob':'345'}


def user_login(username,password):
    md5str = username + password
    md5 = hashlib.md5()
    md5.update(md5str.encode('utf-8'))
    new_password = md5.hexdigest()
    if (username,new_password) in user.items():
        print('login success !')
    else:
        print('user or password error !')


def main():
    user_login('Ace','123')


if __name__ == '__main__':
    main()
