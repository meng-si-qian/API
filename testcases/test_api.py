#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: test_api.py
@time: 2023/4/16 00:57
@desc: 
"""
import pytest

class TestApi:

    @pytest.mark.parametrize('args',['百里','星耀','依然'])
    def test_api1(self,args):
        print(args)

    @pytest.mark.parametrize('name,arg',[['百里',13],["依然",14]])
    def test_api2(self,name,arg):
        print(name,arg)

if __name__ == '__main__':
    pytest.main(['test_api.py'])