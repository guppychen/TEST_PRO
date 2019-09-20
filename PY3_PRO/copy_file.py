#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from os.path import exists

from_file = input("Please input your source file:")
new_file = input("Please input your dest file:")
# exists 判断文件是否存在
print("Dose new_file exist ? %r" % exists(new_file))
txt = open(from_file)
in_file = txt.read()
new_file =  open(new_file, 'w')
new_file.write(in_file)
print("Copy done.")
new_file.close()
