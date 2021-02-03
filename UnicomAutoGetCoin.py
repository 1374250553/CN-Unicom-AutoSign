# coding=utf-8
# author:@QiuYueBai

import http.cookiejar
import json
import os
import sys
import urllib.request as urllib2
import ssl
import urllib
import datetime
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
class Qiandao():

    def __init__(self):
        self.cookie = http.cookiejar.CookieJar()
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(self.opener)


    def sign(self,data):
        global a
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Cookie': '_version=iphone_c@8.0101; city=051|540|90657326|-99; cw_mutual=7064d003eb3c8934e769e430ecf3d64af98860225d2b39ea5a384904434dbb5e5bd354cc17afd089bf019d59a825e82765ed4b6148458fecb59f7ef3f5a972c6; ecs_acc=mv6aWHxk7wbabTvEI2D32I7kwtFHCT3PAuhWTJIecDvCyegHUk1LdPAI556fd0sO1HqWK25KUpJsDHC9FfTjiEJl55X5jt3F46VKT5ALSG9Nx12Fdj3QzxsXbYizxswUprKu9UpjCMFk7VCWpCIK7Sp9H86FzNOrAJKsuGp2Se0=; ecs_token=eyJkYXRhIjoiM2VhYTI3MjNlMTJkY2M0Y2Q3NWFlNDA3NzE3NDNkMTkwMjM0ZjFjMzRmNjk5MmY4ZTZiYjIxNmVmYTE2NjdmYjdmMTQzODcwMWY1NzY4YjRlY2VjYWJhZjQ0M2VlMTBiNDMzOWFlNDRjNzJhNTM5NTZlODExYjE5M2M0MTQxYzVlNTY3YzhhNzg5MzM1YWQ4ZTZkNWZmZGE2ZmQ1NjRiOTdkMzk3MjA1YmNkNDFkNDVlYTgyODY2YjRkODk5YzliIiwidmVyc2lvbiI6IjAwIn0=; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxODUwMzA1NTM3NSIsInBybyI6IjA1MSIsImNpdHkiOiI1NDAiLCJpZCI6IjUzN2QwNDYzMWEyYjY5MGM5NGZhNjc0YjE5NWFiYWQyIn0.K32MEsF8p7MxQzXgVVQjwtlZ4QF5TjDItDtKSvhnnqQ; login_type=19; u_account=18503055375; c_sfbm=234g_00; channel=GGPD; devicedId=009CE565-D87A-463D-AAE3-3D56082406CC',
            'User-Agent': 'ChinaUnicom4.x/1000 CFNetwork/1209 Darwin/20.2.0',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        data = data.encode('utf-8')
        req2 = urllib2.Request("http://m.client.10010.com/mobileService/login.htm",headers=headers)
        req2 = urllib2.urlopen(req2,data)
        if req2.getcode() == 200:
            print('login success!')
        try:
            for item1 in self.cookie:
                if item1.name == 'a_token':
                    a = item1.value
        except:
            print("cant get cookies")
        data2={'stepflag':'22'}
        data2=urllib.parse.urlencode(data2).encode('utf-8')
        
        req3 = urllib2.Request("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=" + a)
        if urllib2.urlopen(req3).getcode() == 200:
            print('querySigninActivity success!')
        
        req4 = urllib2.Request("https://act.10010.com/SigninApp/signin/daySign", "btnPouplePost".encode('utf-8'))
        if urllib2.urlopen(req4).getcode() == 200:
            print('daySign success!')
            
        req5 = urllib2.Request("https://act.10010.com/SigninApp/signin/getIntegral")
        r = self.opener.open(req5)
        print( ' coin: ' + r.read().decode('utf-8'))
        
        data2={'stepflag':'22'}
        data2=urllib.parse.urlencode(data2).encode('utf-8')
        data3={'stepflag':'23'}
        data3=urllib.parse.urlencode(data3).encode('utf-8')
        for x in range(3):
           get_req6 = urllib2.Request("http://act.10010.com/SigninApp/mySignin/addFlow",data2)
           req6 = self.opener.open(get_req6)
           get_req7 = urllib2.Request("http://act.10010.com/SigninApp/mySignin/addFlow",data3)
           req7 = self.opener.open(get_req7)
if __name__ == '__main__':

    user = Qiandao()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    data = timestamp+sys.argv[1]

    user.sign(data)
