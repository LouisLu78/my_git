'''
Created on 2019828

@author: Basanwei
'''
import sys

a=3
b=6
c=8.29
d=4.19

e=complex(c, d)
f=complex(float(a),float(b))

print("a is type:", type(a))
print("c is type:", type(c))

print(a+b)
print(d/c)

print(e)
print(e+f)
print(sys.float_info)