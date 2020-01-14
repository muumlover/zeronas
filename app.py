#!/usr/bin/env python3
# encoding: utf-8

"""
@Time    : 2020/1/6 11:16
@Author  : Skogen
@Email   : muumlover@live.com
@Blog    : https://blog.ronpy.com
@Project : zeronas
@FileName: app.py
@Software: PyCharm
@license : (C) Copyright 2019 by Sam Wang. All rights reserved.
@Desc    : 
    
"""

from flask import Flask

from apis.files import handle_file
from apis.users import handle_user

app = Flask(__name__)
app.add_url_rule('/api/file', 'api_file', handle_file)
app.add_url_rule('/api/user', 'api_user', handle_user)


@app.errorhandler(404)
def handle_default(error):
    return app.send_static_file('file.html')


# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.after_request(after_request)

if __name__ == '__main__':
    app.run()
