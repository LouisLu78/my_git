# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/25
# If not explicitly pointed out, all the codes are written by myself.

file=r'C:\Users\Basanwei\Exercise\ex\downfile.txt'
with open(file,'r') as f:
    lines=f.readlines()
word_number=0
for line in lines:
    word_number+=len(line.split())
print('The file consists of %d lines.'%len(lines))
print('And it totally contains %d words,'%word_number, end=' ')
print('which means each line is roughly composed of %.0f words.'%(word_number/len(lines)))