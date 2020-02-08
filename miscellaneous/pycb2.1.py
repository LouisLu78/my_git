# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/2/8
# Email: gq4350lu@hotmail.com

from fnmatch import fnmatchcase

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
list1 = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(list1)

list2 = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(list2)
