# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
a=[]
with open('CAM_table.txt') as f:
    for line in f:
        if 'DYNAMIC' in line:
            a.append(line.replace('  DYNAMIC  ','').rstrip().split())

vlan = input('vvedite nomer vlana: ')
for strok in a:
    if strok[0] ==vlan:
        print('{:<8}{:18}{:8}'.format(strok[0],strok[1],strok[2]))

