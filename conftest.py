#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: conftest.py
@time: 2023/4/12 23:52
@desc: 
"""
import pytest

@pytest.fixture()
def confTest(scope="function"):
    print('滴滴滴')
    yield
    print('啦啦啦')
