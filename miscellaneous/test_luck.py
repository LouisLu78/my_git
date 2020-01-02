# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/2
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

'''
The codes below show a gamble game testing luck of player. The codes can be viewed as a translation from C program
 presented in a textbook.
'''

import random

def rollDice():
    die1, die2 = random.randint(1,6), random.randint(1,6)
    return die1 + die2

# for i in range(100):
#     if i%5==0:
#         print('\n')
#     print('%4d'%rollDice(),end=' ')

def main():
    flag=-1
    sum = rollDice()
    print('sum is %d.' % sum)
    if sum in [7,11]:
        flag=1
    elif sum in [2,3,12]:
        flag=0
    else:
        while (flag==-1):
            rand_result = rollDice()
            print('rand_result is %d.'%rand_result)
            if rand_result==sum:
                flag=1
            elif rand_result==7:
                flag=0
    if flag==0:
        print('You lose.')
    if flag==1:
        print('You win.')

if __name__=='__main__':
    main()
