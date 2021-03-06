import requests
from utils.RequsetsUtil import requests_get
from utils.RequsetsUtil import requests_post
from utils.RequsetsUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from common.Base import init_db
import pytest
import json

conf = ConfigYaml()
url_add = conf.get_conf_url()
def testlogin():


    url=url_add+"/authorizations/"
    # url="http://211.103.136.242:8064/authorizations/"
    data={"username":"python","password":"12345678"}
    # r = requests.post(url, json=data)
    # print(r.json())
    # print(requests_post(url,json=data))
    req=Request()
    r=req.post(url,json=data)
    print(r)
    code = r["code"]
    #assert code == 200
    AssertUtil().assert_code(code,200)
    #返回结果内容
    #body = json.dumps(r["body"])
    body = r["body"]
    #assert '"user_id": 1, "username": "python"' in body
    AssertUtil().assert_in_body(body,'"user_id": 1, "username": "python"')
    conn=init_db("db_1")
    res_db=conn.fetchone("select id,username from tb_users where username='python'")
    print("数据库%s"%res_db)
    user_id =body["user_id"]
    assert user_id ==res_db["id"]

def testinfo():
    url = url_add+"/user/"
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTYwMzUyNTgwNX0.nI8SyizGPhgGw1i-V-KgXSdB_7TNkL90eDJCemaSlp8"
    headers={
        'Authorization':'JWT ' + token
    }
    # r=requests.get(url,headers=headers)
    # print(r.json())
    # print(requests_get(url,headers=headers))
    print(Request().get(url,headers=headers))


def goods_list():
    url=url_add+"/categories/115/skus"
    # url="http://211.103.136.242:8064/categories/115/skus"
    data ={
        "page":"1",
        "page_size":"5",
        "ordering":"create_tiem"
        }
    print(requests.get(url,json=data).json())

def cart():
    url = url_add + "/cart/"
    # url = "http://211.103.136.242:8064/cart/"
    data={"sku_id":"3","count":"1","selected":"true"}
    token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTYwMzUyODYwMH0._158_DZRKen7g9nevLwtrfznsZYupMduBfwaPJyRfsA"
    headers={
        'Authorization':'JWT ' + token
    }
    # r=requests.post(url,json=data,headers=headers)
    # print(r.json())
    print(requests_post(url,json=data,headers=headers))

def order():
    url = url_add + "/orders/"
    # url = "http://211.103.136.242:8064/orders/"
    data= {"address":"1","pay_method":"1"}
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTYwMzUyODYwMH0._158_DZRKen7g9nevLwtrfznsZYupMduBfwaPJyRfsA"
    headers = {
        'Authorization': 'JWT ' + token
    }
    r = requests.post(url, json=data, headers=headers)
    print(r.json())
if __name__ == '__main__':
    # login()
    # info()
    # goods_list()
    # cart()
    # order()
    pytest.main(["-s"])