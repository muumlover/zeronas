#!/usr/bin/env python3
# encoding: utf-8

"""
@Time    : 2020/1/6 11:16
@Author  : Sam Wang
@Email   : muumlover@live.com
@Blog    : https://blog.muumlover.com
@Project : zeronas
@FileName: app.py
@Software: PyCharm
@license : (C) Copyright 2019 by Sam Wang. All rights reserved.
@Desc    : 
    
"""

from flask import Flask

from apis.files import file_view

app = Flask(__name__)
app.add_url_rule('/file_api', 'index', file_view)


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.after_request(after_request)

if __name__ == '__main__':
    app.run()
