#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: test_send_request.py
@time: 2023/4/10 23:23
@desc: 
"""
import requests




class TestOne:
    def get_session(self):
        session = requests.session()
        return  session
    def testOne(self):
        url = ""
        data = {
            "appid": "",
        }
        rep = self.get_session().request("post",url = url , json = data)