#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: all.py
@time: 2023/4/12 23:59
@desc: 
"""
import pytest
import os


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate temp -o reports --clean")