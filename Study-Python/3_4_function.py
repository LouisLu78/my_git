# -*- coding: utf-8 -*-
def say_hi():
    print('hello') 
    
say_hi()
say_hi()

def print_time_two(a,b):
    c=a*b
    print(c)
    
print_time_two(4,8)

def repeat_str(str, times):
    repeated_strs=str*times
    return repeated_strs

repeated_strings=repeat_str("happy time ",4)
print(repeated_strings)