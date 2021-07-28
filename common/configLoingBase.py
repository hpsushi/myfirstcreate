# -*- coding: utf-8 -*-
"""
作者：Haiping.hu
日期：2021/7/27 3:20 下午
"""
import configparser

def readloginconfig():
    config = configparser.ConfigParser()
    config.read("../testfile/config.ini",encoding="utf-8")
    res = config.options("base")
    phone = config.get("base","phone")
    pwd = config.get("base","pwd")
    tenantid = config.get("tenantid")
    logininfo = [phone,pwd,tenantid]
    return logininfo

if __name__ == "__main__":
    readconfig()