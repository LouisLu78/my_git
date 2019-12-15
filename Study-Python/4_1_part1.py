# -*- coding: utf-8 -*-
#Created on 20190908

#@author: Basanwei

num = 90
guess = int(input("please input an integer: "))
if guess == num:
   print("Bingo! U r correct!")
   print("However you have no award!")
elif guess<num:
    print("the number is greater than that!")
else:
    print("the number is less than that!") 
print("DONE!")


 
for i in range(5, 10):
    print(i) 
else:
    print("the loop is done!")