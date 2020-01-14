#!/usr/bin/env python
# encoding: utf-8

"""
@Time    : 2020/1/14 15:00
@Author  : Skogen
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : zeronas
@FileName: users
@Software: PyCharm
@license : (C) Copyright 2019 by Sam Wang. All rights reserved.
@Desc    :

"""
import os

from flask import request, jsonify

from util.user_module import User


def handle_user():
    user = 'test'
    users = [{
        'name': x,
        'type': 'user',
        'size': 0,
        'time': ''
    } for x in User.list()]
    return jsonify({'code': 0, 'message': '', 'items': users, 'count': len(users)})
