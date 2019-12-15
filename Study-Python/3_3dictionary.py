# -*- coding: utf-8 -*-
#Created on 2019831

#@author: Basanwei

phone_book={'Louis':7806, 'Jerry':8085, 'amao':2160}

mixed_dict={'Andy':3341, 11:3.25}

print("Louis'phone number is:" + str(phone_book['Louis']))

#revise a dictionary

phone_book['amao']=1234
print("amao's phone number is:" + str(phone_book['amao']))

phone_book['Grace']=3501

print("phone book is:" + str(phone_book))

del phone_book['amao']

print("changed phone book is:" + str(phone_book))

phone_book.clear()
print("cleared phone book is:" + str(phone_book))
#同一个字典，不能有相同的Key
#Key 可以是tuple,不能是List
