# -*- coding:utf-8 -*-
from bottle import route, run
import os


@route('/')
def hello():
    return "Hello World!"

run()

#run(host='localhost', port=8080, debug=True)