# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

res = ospf_route.split()
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

