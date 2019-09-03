# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt') as f:
    for line in f:
        line =line.replace('O','OSPF')
        res = line.split()
        res.remove('via')
        inf = '''
Protocol:          {}
Prefix:            {}
AD/Metric:         {}
Next-HOP:          {}
Last update:       {}
Outbound Interface {}
'''
        print(inf.format(res[0],res[1],res[2],res[3],res[4],res[5]))

