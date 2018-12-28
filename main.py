#!/usr/bin/env python
# coding=utf-8

from flask import Flask
import re
import requests
import json

STATIC_URL = 'https://pub-static.haozhaopian.net'

app = Flask(__name__)

@app.route('/')
def index():
    re.match('^/([a-zA-Z]{2})/','/en/sdfds')
    return 'index!'

@app.route('/hello')
def hello():
    return 'Hello,World!'

if __name__ == '__main__':
    r = requests.get(STATIC_URL + '/assets/res/sticker/d63ce32c-3397-4b01-9a81-56d2f5bebc291.svg')
    #r1 = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})
    if r.status_code == 404:
        print(r.status_code)

    dict1 = {}
    dict1['id'] = "This is one"
    dict1['url'] = "This is two"
    f = open('sticker.json','a',encoding = 'utf-8')
    json.dump(dict1,f)
    re = json.loads(f.read())
    print(re[1]['id'])
    #app.run()