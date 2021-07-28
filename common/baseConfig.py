# -*- coding: utf-8 -*-
"""
作者：Haiping.hu
日期：2021/7/27 3:25 下午
"""
import requests
import json
import hashlib
from common.configLoingBase import readloginconfig
import warnings
warnings.filterwarnings("ignore")

def sha1jiami(password):
    psd = hashlib.sha1(password.encode("utf-8"))
    jiamistr = psd.hexdigest()
    return jiamistr

def jiamimd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()

def generate_sig(data):
    offset = '0ce37dd6b927730161a1e559c2336d0a'   #这个是我们公司的秘钥
    s = ''
    res = sorted(data.items(), key=lambda item: item[0])
    for i in range(0, len(res)):
        s = s + res[i][0] + '=' + res[i][1]
    s += offset
    _sig = jiamimd5(s)
    return _sig

def gettoken():
    #post方法
    inilist = readloginconfig()
    phone = inilist[0]
    rawpwd = inilist[1]
    tenantid = inilist[2]
    pwd = sha1jiami(rawpwd)
    dict1 = {}
    dict1["_sm"]="md5"
    dict1["_ft"]="json"
    dict1["mobile"]=phone
    dict1["password"]=pwd
    dict1["-aid"]="500"
    dict1["_tk"]=""
    dict1["_uid"]=""
    dict1["_tenantid"]=tenantid
    dict1["_domid"]="2000"
    dict1["_mt"]="user.wapLogin" #这里这个参数写死了，因为这个是定的，不会因为什么原因会有变化
    _sig = generate_sig(dict1)
    dict1["_sig"]=_sig
    url = "https://api.zhaogang.com/web.api"
    response = requests.post(url,dict1,verify=False)
    responsejson = eval(response.text)
    token = responsejson["content"][0]["token"]
    uid = responsejson["content"][0]["uid"]
    uidtoken ={"token":token,"uid":uid,"tenantid":tenantid}
    return uidtentoken

if __name__ == "__main__":
    gettoken()