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
        paramss = args['api_request']['paramss']
        req = requests.Request(method=method,url=url,json=paramss,headers=headers)

if __name__ == '__main__':
    pytest.main(['-vs'])