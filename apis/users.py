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
import json
from flask import request, jsonify

from util.user_module import User


class UserAction:
    def __init__(self):
        pass

    @staticmethod
    def list():
        users = User.list()
        return jsonify({'code': 0, 'message': '', 'body': users, 'count': len(users)})

    @staticmethod
    def space(username):
        user = {
            'name': username,
            'type': 'user',
            'size': User.space(username),
            'time': ''
        }
        return jsonify({'code': 0, 'message': '', 'body': user})


def handle_user():
    user = 'test'
    data = json.loads(request.get_data(as_text=True))
    if 'action' not in data:
        return '...'
    if data['action'] not in UserAction.__dict__:
        return '...'
    action = UserAction.__dict__[data.pop('action')].__func__
    try:
        return action(**data)
    except Exception as err:
        return jsonify({'code': -1, 'message': err.message})
