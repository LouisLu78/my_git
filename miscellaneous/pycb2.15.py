# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/19
# Email: gq4350lu@hotmail.com

s = '{name} has {n} messages.'
new_s = s.format(name='Guido', n=37)
print(new_s)

name = 'Guido'
n = 37
new_s = s.format_map(vars())
print(new_s)

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido',37)
new_s = s.format_map(vars(a))
print(new_s)