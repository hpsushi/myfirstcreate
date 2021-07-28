# -*- coding: utf-8 -*-
"""
作者：Haiping.hu
日期：2021/7/27 8:48 上午
"""
import  requests


def post_main(url,data,expect):
    response = requests.post(url,params=data,verify = False)
    print(response.text)
    print(response.url)

def get_main(url,data,expect):
    response = requests.get(url, params=data,verify=False)
    print(response.text)