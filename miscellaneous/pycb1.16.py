# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/30
# Email: gq4350lu@hotmail.com

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = (n for n in mylist if n > 0)
for number in pos:
    print(number)