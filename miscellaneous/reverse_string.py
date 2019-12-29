# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/28
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

s='accuracy of the information'
#method one
s_list=['']*len(s)
print(s_list)
j=len(s)-1
# for i in range(len(s)):
#     if i<=j:
#         s_list[j]=s[i]
#         s_list[i]=s[j]
#         j-=1
# we can also use the following loop as
for c in s:
    s_list[j]=c
    j-=1
print(s_list)
s_reversed=''.join(s_list)
print(s_reversed)

#method 2
s_reversed=s[::-1]
print(s_reversed)