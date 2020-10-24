import requests
from utils.LogUtil import my_log
def requests_get(url,headers):
    r=requests.get(url,headers=headers)
    code=r.status_code
    try:
        body = r.json()
    except Exception as e:
        body=r.text

    res=dict()
    res["code"] = code
    res["body"] = body
    return res

def requests_post(url,headers=None,json=None):
    r=requests.post(url,json,headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res["code"] = code
    res["body"] = body
    return res

class Request:
    def __init__(self):
        self.log=my_log("Requests")
    def ruquests_api(self,url,json=None,headers=None,method="get",data=None,cookies=None):
        if method=="get":
            self.log.debug("get请求")
            r=requests.get(url,json=json,headers=headers,data=data,cookies=cookies)
        elif method == "post":
            self.log.debug("post请求")
            r = requests.post(url, json=json, headers=headers,data=data,cookies=cookies)
        #2. 重复的内容，复制进来
        #获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        #内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        #字典返回
        return res


    def get(self,url,**kwargs):
        return self.ruquests_api(url,method="get",**kwargs)
    def post(self,url,**kwargs):
        return self.ruquests_api(url,method="post",**kwargs)