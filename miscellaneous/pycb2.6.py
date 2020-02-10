# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/10
# Email: gq4350lu@hotmail.com

import re

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

text = 'UPPER PYTHON, lower python, Mixed Python'
newtext = re.sub('python', matchcase('snake'), text, re.I)
print(newtext)
