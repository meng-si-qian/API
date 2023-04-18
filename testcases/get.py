#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: get.py
@time: 2023/4/18 22:36
@desc: 
"""
import requests

from common.yaml_util import YamlUtil
import pytest
class Test_new:
    @pytest.mark.parametrize('args',YamlUtil().read_yaml('/get_new'))
    def test_01_api(self,args):
        url = args['api_request']['url']
        method= args['api_request']['method']
        headers= args['api_request']['headers']
        params = args['api_request']['params']
        req = requests.Request(method=method,url=url,json=params,headers=headers)
        print(req.json)

if __name__ == '__main__':
    pytest.main(['-vs'])