#!/usr/bin/env python3
# encoding: utf-8

"""
@Time    : 2020/1/6 11:16
@Author  : Skogen
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : zeronas
@FileName: files
@Software: PyCharm
@license : (C) Copyright 2019 by Sam Wang. All rights reserved.
@Desc    : 
    
"""
import os
from datetime import datetime

from flask import jsonify, request, make_response, send_from_directory

from util.file_size import approximate_size


def get_size(file_path):
    if not os.path.isfile(file_path):
        return '-'
    return approximate_size(os.path.getsize(file_path))


def get_time(file_path):
    if not os.path.isfile(file_path):
        return '-'
    return datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')


def get_files(base_path, target_path):
    file_list = []
    for file_name in os.listdir(target_path):
        file_path = os.path.join(target_path, file_name)
        file_list.append({
            'type': 'file' if os.path.isfile(file_path) else 'dir',
            'name': file_name,
            'path': '/' + os.path.relpath(file_path, base_path),
            'size': get_size(file_path),
            'time': get_time(file_path)
        })
    return file_list


def handle_file():
    user = 'test'
    path = request.args.get("path") or ""
    base_path = '/sata/home/' + user + '/'

    target_path = base_path + path
    if os.path.isdir(target_path):
        return jsonify({'code': 0, 'message': '', 'type': 'dir', 'items': get_files(base_path, target_path)})
    else:
        try:
            response = make_response(send_from_directory(*os.path.split(target_path), as_attachment=True))
            return response
        except Exception as e:
            return jsonify({'code': -1, 'message': '{}'.format(e)})
