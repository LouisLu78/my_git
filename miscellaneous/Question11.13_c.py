# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2020/1/17
# Email: gq4350lu@hotmail.com
# If not explicitly pointed out, all the codes are written by myself.

import random, time

def phoneWords(number):
    num=['', '', 'ABC', 'DEF', 'GHI', 'JKL',
         'MNO', 'PRS', 'TUV', 'WXY']
    words = set()
    word = ''
    L = 0
    while L < 3**len(str(number)):

        for c in str(number):
            if c != '0' and c != '1':
                n = eval(c)
                word += random.choice(list(num[n]))

        words.add(word)
        L = len(words)
        word = ''

    return words

def main():
    number=2534746
    phoneWord = list(phoneWords(number))
    chunk=[list(phoneWord[i: i+20]) for i in range (0,len(phoneWord),20)]
    for shortlist in chunk:
        print(shortlist)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('The program costs %.2f seconds.'%(end - start))

