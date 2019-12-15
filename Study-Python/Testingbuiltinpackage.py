'''
Created on 2019825

@author: Basanwei
'''
import os
import requests
print(os.getcwd())

r=requests.get("http://www.sohu.com")

print(r.url)
print(r.encoding)
print(r.text)