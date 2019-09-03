# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ignore = ['duplex', 'alias', 'Current configuration']
mark=True
with open(argv[1]) as f, open('config_sw_cleared.txt','w') as wr:
    for line in f:
        mark=True
        for i in ignore:
            if i in line:
                mark=False
        if mark:
           wr.write(line)
