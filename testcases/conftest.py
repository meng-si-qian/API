#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: conftest.py
@time: 2023/4/12 23:52
@desc: 
"""
import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def confTest():
    print('滴滴滴')
    yield
    print('啦啦啦')


# @pytest.fixture(scope="session",autouse=True)
def claer_yaml():
    YamlUtil.clear_extract_yaml()