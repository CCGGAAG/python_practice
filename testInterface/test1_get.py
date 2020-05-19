# coding:utf-8
import requests

url = "http://10.82.12.25/centralize-purchase/#/"
r = requests.get(url)

print(r)
print(r.status_code)
assert r.status_code == 200