# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/23
# If not explicitly pointed out, all the codes are written by myself.

import wikipedia
import requests

res=requests.get('http://www.wikipedia.org')
print(res.status_code)

print(wikipedia.summary('atom bomb'))
print(wikipedia.search('atom bomb', results=5))