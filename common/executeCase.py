# -*- coding: utf-8 -*-
"""
作者：Haiping.hu
日期：2021/7/27 9:46 上午
"""
import requests
import json
import hashlib
from common.readTestCaseExcel import readdata
from common.baseConfig import gettoken
import warnings
warnings.filterwarnings("ignore")

def calldata(data2):
    token_now = gettoken()
    print(token_now["token"],token_now["uid"])
    data = {"_sm": "md5",
            "_aid": "500",
            "_domid": "2000",
            "_ft": "json",
            "_tk": token_now["token"]+"",
            "_uid": token_now["uid"]+"",
            "_tenantid": token_now["tenantid"]+"",
            "param": json.dumps(data2),}
    return data

def executeData():
    caselists = readdata()
    #要把这个列表根据no来排序，如果用例是需要顺序执行的话[{"":""}]
    for caselist in caselists:
        testdata = caselist["data"]
        mt = caselist["mt"]
        testdata = eval(testdata)
        testdata["_mt"] = mt
        handle_testdata = calldata(testdata)
        finaldata = generate_sig(handle_testdata)
        url = caselist["url"]
        method = caselist["method"]
        expectresult = caselist["expect"]
        if method == "GET":
            get_main(url, finaldata, expectresult)
        else:
            post_main(url,finaldata,expectresult)

if __name__ == "__main__":
    executeData()

