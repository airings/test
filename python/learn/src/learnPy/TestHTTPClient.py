'''
Created on Apr 10, 2016

@author: airings
'''

import urllib2
import json
import httplib

def http_get():
    url='http://localhost:8080/'  
    response = urllib2.urlopen(url)       
    return response.read()

def http_post():
    url='http://192.168.1.13:9999/test'
    values ={'user':'Smith','passwd':'123456'}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息



if __name__ == '__main__':
    ret = http_get()
    print("RET %r" % (ret))