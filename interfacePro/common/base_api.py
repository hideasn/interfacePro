# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/9 11:00
文件: base_api.py
项目: interfacePro
描述: 
'''
import requests

class BaseApi:

    def request_send(self, method):
        requests.Request(method=method)
