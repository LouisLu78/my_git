# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/15
# Email: gq4350lu@hotmail.com

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print('Method one to sort dictionary:')
print(min_price)
print(max_price)
print('\n')
min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])
print('Method two to sort dictionary:')
print(min_price)
print(max_price)