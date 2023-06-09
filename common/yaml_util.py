#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: yaml_util.py
@time: 2023/4/13 23:52
@desc: 
"""
import os
import yaml


class YamlUtil:
    #读取yaml文件
    def read_extract_yaml(self,key):
        with open(os.getcwd()+"/extract.yml",mode="r",encoding='utf-8') as f:
            vaule  = yaml.load(stream=f,Loader=yaml.FullLoader)
            return vaule[key]

    #写入yaml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd()+"/extract.yml",mode="a",encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    # 写入yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml",mode="w",encoding='utf-8') as f:
            f.truncate()

    # 获取测试用例
    def read_testcars_yaml(self,yaml_name):
        with open(os.getcwd()+"/testcases/"+yaml_name,mode="r",encoding='utf-8') as f:
            vaule  = yaml.load(stream=f,Loader=yaml.FullLoader)
            return vaule
    #读取yaml文件
    def read_yaml(self,yaml_name):
        with open(os.getcwd()+yaml_name,mode="r",encoding='utf-8') as f:
            vaule  = yaml.load(f,Loader=yaml.FullLoader)
            return vaule
