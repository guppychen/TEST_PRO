# -*- coding: UTF-8 -*-

import random
import re
import sys


def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


# i = 1


# add operation
def add(a, b):
    c = a + b
    return c


# subtract operation
def subtract(a, b):
    c = a - b
    return c


# call add operation
def printadd(j):
    while j <= n:
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        c = add(a,b)
        if c <=100:
            print(j, ".", a, "+", b, "=", c)
            j = j + 1
        else:
            continue


# call subtract operation
def printsub(j):
    while j <= n:
        a = random.randint(10, 100)
        b = random.randint(10, 100)
        c = subtract(a,b)
        if c >= 0:
            print(j, ".", a, "-", b, "=", c)
            j = j + 1
        else:
            continue


var1 = input("请问要出什么题？ 输入1：加法  输入2：减法 : ")
if is_number(var1) is False:
    print("你输入的题型不是数字！")
    input("press any key to exit")
    exit()
else:
    var1 = int(var1)
if var1 != 1 and var1 != 2:
    print("你输入的题型非法！")
    input("press any key to exit")
    exit()

n = input("请问要出几道题? 输入100以内的数： ")
if is_number(n) is False:
    print("你输入的题量不是数字！")
    input("press any key to exit")
    exit()
if int(n) > 100:
    print("你输入的题量太多了！")
    input("press any key to exit")
    exit()
else:
    n = int(n)


def main():
    i = 1
    if var1 == 1:
        printadd(i)
        input("press any key to exit")
    if var1 == 2:
        printsub(i)
        input("press any key to exit")


if __name__ == '__main__':
    sys.exit(main())







