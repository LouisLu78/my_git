# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/18
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import time

def phoneWords(number):

    s_number = str(number)
    L = len(s_number)
    num=['', '', 'ABC', 'DEF', 'GHI', 'JKL',
         'MNO', 'PRS', 'TUV', 'WXY']
    words = set()

    if L == 1:
        n = eval(s_number)
        if n != 0 and n != 1:
            for ch in num[n]:
                word = ch
                words.add(word)

    else:
        s_number_temp = s_number[:(L-1)]
        words_temp = phoneWords(s_number_temp)
        n = eval(s_number[-1])
        if n != 0 and n != 1:
            for w in words_temp:
                for ch in num[n]:
                    word = w + ch
                    words.add(word)
    return words

def main():

    number = 5347936556987
    phoneWord = list(phoneWords(number))
    chunk=[list(phoneWord[i: i+20]) for i in range (0,len(phoneWord),20)]
    for shortlist in chunk:
        print(shortlist)
    print("It contains totally %d words."%len(phoneWord))

if __name__ == '__main__':

    start = time.time()
    main()
    end = time.time()
    print('The program costs %.2f seconds.'%(end - start))


