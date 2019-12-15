# -*- coding: utf-8 -*-

'''
Created on 2019��8��28��

@author: Basanwei
'''
print ("你好吗")
print("what's your name? \nJerry") #\n is change the line


number_list= [1,5,7,9]
print("number_list:" + str(number_list))

string_list=["bbs","python","love"]

mixed_list=["java", 379, "python", 5.11]

print("mixed_list:" + str(mixed_list))

# access the element in the list
second_num=number_list[1]
third_string=string_list[2]
fourth_mixed=mixed_list[3]

print("second_num："+ str(second_num))
print("third_string："+ str(third_string))
print("fourth_mixed:"+ str(fourth_mixed))

print("second_num:{0}, third_string:{1}, fourth_mixed:{2}".format(second_num, third_string, fourth_mixed))

number_list[1] = 30
print("second_num changed："+ str(number_list))

del mixed_list[1]
print("mixed_list after deletion:" + str(mixed_list))
