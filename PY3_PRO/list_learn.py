#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# linux下执行命令的方法
# import os, time
# cmd = "ls -lh"
# while True:
#         print(cmd)
#         print(os.popen(cmd).read())
#         time.sleep(5)

elements = []
for i in range(0,9):
    print("this is line %d" %i)
    elements.append(i)
print(elements)
print(elements[3])
