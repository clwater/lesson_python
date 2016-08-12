#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import print as print
from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    #user_agent = request.headers.get('User-Agent')
    return '<h1>Hello Word</h1>'
    #return '<p>Your browser is %s</p>' % user_agent
    #return '%s' % request.headers

    #return '<h1>Bad Request</h1>' , 400
    # response = make_response('<h1>This document carries a cookie!')
    # response.set_cookie('answer' , '42')
    # return response
    #return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name

# @app.route('/user/<id>')
# def get_user(id):
#     user = id
#     if not user:
#         abort(404)
#     return '<h1>Hello . %s </h1>' % user

if __name__ == '__main__':
    app.run(debug=True)


