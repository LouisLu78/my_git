# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/9
# Email: gq4350lu@hotmail.com

import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
newText = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(newText)

dateRegex = re.compile(r'(\d+)/(\d+)/(\d+)')
mo = dateRegex.sub(r'\3-\1-\2', text)
print(mo)
