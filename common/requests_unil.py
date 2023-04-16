#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: requests_unil.py
@time: 2023/4/16 18:21
@desc: 
"""
import json

import requests

class RequestsUnil():
    session =  requests.session()
    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()
        rep = None
        if method=='get':
            rep = RequestsUnil.session.request(method, url=url, data=data, **kwargs)
        else:
            data = json.dumps(data)
            rep = RequestsUnil.session.request(method, url=url, json=data, **kwargs)
        return rep.text