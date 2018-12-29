#!/usr/bin/env python
# coding=utf-8

from flask import Flask
import re
import requests
import json
from app import users
from common import FileUtils
import threading
import time


STATIC_URL = 'https://pub-static.haozhaopian.net'
THREAD_NUM = 20
PAGE_SZIE = 100

app = Flask(__name__)

@app.route('/')
def index():
    re.match('^/([a-zA-Z]{2})/','/en/sdfds')
    return 'index!'

@app.route('/hello')
def hello():
    return 'Hello,World!'

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,pageNo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.pageNo = pageNo
    def run(self):
        print ("开始线程：" + self.name)
        users.handle_sticker_400(self.name,self.pageNo,PAGE_SZIE,STATIC_URL)
        print ("退出线程：" + self.name)

# 为线程定义一个函数
def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

if __name__ == '__main__':
    #users.handle_sticker_400('23',54,PAGE_SZIE,STATIC_URL)
    # r = requests.get(STATIC_URL + '/assets/res/sticker/d63ce32c-3397-4b01-9a81-56d2f5bebc291.svg')

    #====================================================================
    # pageNo = FileUtils.read_file_last('pageNo.txt')
    # threadN = 0;
    # while threadN < THREAD_NUM:
    #     pageNo = pageNo + 1 
    #     threadN = threadN + 1            
    #     with open('pageNo.txt', 'r',encoding = 'utf-8') as p:
    #         listNo = p.read()
    #         if str(pageNo) not in listNo:
    #             FileUtils.in_file('pageNo.txt',pageNo)
    #             #创建新线程
    #             thread1 = myThread(1, "Thread-"+str(threadN)+"-"+str(pageNo), threadN,pageNo)
    #             thread1.start()
    #         else:
    #             print('>>>>>>>>>>>>>>>chongfu')


    #=======================================================================
    headers={
        'Authorization':''
    }
    # print(rep.text)      
    with open('sticker_error.txt', 'r',encoding = 'utf-8') as p:
        re = p.readlines()
        for i in re:
            id = i.split('===')[0]
            rep = requests.post(url='http://:8025/sticker/syncResources', params={'ids': id,'syncState':'01'},headers=headers)  
            print(rep.text)      
    #app.run()