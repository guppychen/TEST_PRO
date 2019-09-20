#!/usr/bin/env python
# -*- coding: UTF-8 -*-
filename = "file_read.txt"
txt = open(filename)
print(txt.readline(),end='')
print(txt.readline(),end='')
print(txt.readline(),end='')
print(txt.readline(),end='')
#return to location of 0 byte
txt.seek(0)
print(txt.readline(),end='')
txt.close()