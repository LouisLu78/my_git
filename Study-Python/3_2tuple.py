# -*- coding: utf-8 -*-

'''
Created on 2019��8��30��

@author: Basanwei
'''



number_tuple= (1,5,7,9)
print("number_tuple:" + str(number_tuple))

string_tuple=("bbs","python","love")

mixed_tuple=("java", 379, "python", 5.11)

print("mixed_tuple:" + str(mixed_tuple))

# access the element in the list
second_num=number_tuple[1]
third_string=string_tuple[2]
fourth_mixed=mixed_tuple[3]

print("second_num："+ str(second_num))
print("third_string："+ str(third_string))
print("fourth_mixed:"+ str(fourth_mixed))

print("second_num:{0}, third_string:{1}, fourth_mixed:{2}".format(second_num, third_string, fourth_mixed))

print((1,2,3)+(10,20,30))
print(mixed_tuple[-2])
print(mixed_tuple[1:])


