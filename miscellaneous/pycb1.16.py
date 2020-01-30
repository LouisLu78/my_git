# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/30
# Email: gq4350lu@hotmail.com

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
pos = (n for n in mylist if n > 0)
for number in pos:
    print(number)

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)