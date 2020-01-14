#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/1/14 13:26
@Author  : Skogen
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : zeronas
@FileName: user_module
@Software: PyCharm
@license : (C) Copyright 2019 by Sam Wang. All rights reserved.
@Desc    :

"""

import os


class User:
    def __init__(self):
        pass

    @staticmethod
    def list():
        return [x.strip() for x in os.popen('cat /etc/passwd | grep "sata" | cut -f1 -d":"').readlines()]

    @staticmethod
    def exist(username):
        return 256 != os.system('cat /etc/passwd | cut -f1 -d":" | grep -w "{username}"'.format(username=username))

    @staticmethod
    def add(username):
        if User.exist(username):
            return False
        return 256 != os.system(
            'useradd {username} -g users -M -d /sata/home/{username} -f 0'.format(username=username))

    @staticmethod
    def delete(username):
        return False and username
