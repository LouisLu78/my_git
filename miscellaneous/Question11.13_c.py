# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/17
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import random

def phoneNumber(number):
    num=['', '', 'ABC', 'DEF', 'GHI', 'JKL',
         'MNO', 'PRS', 'TUV', 'WXY']
    words=[]
    word = ''

    while True:
        L0 = len(words)
        for c in str(number):
            if c != '0' and c != '1':
                n = eval(c)
                word += random.choice(list(num[n]))
        if word not in words:
            words.append(word)
            L = len(words)
        word = ''
     # how to find the condition to jump out the loop? to be completed later

    return words

number=253278
print(len(phoneNumber(number)))



