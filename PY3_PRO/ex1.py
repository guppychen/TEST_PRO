#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#from sys import argv
script = "ex1.py"
user_name = "Zed"
prompt = "#"
print("Hi %s, I'm the %s script." % (user_name,script))
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" %(likes,lives,computer))