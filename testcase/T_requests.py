import requests

r=requests.get("http://www.4399.com")
print(r.status_code)
print(r.headers)
# print(r.json())
print(r.url)
print(r.cookies)
print(r.text)
