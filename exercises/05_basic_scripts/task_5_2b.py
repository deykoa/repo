# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

x = [argv[1],argv[2]]
ip=x[0].split('.')
ip=[int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])]
mask=int(x[1])*'1'+(32-int(x[1]))*'0'
ip_b='{:08b}{:08b}{:08b}{:08b}'.format(ip[0],ip[1],ip[2],ip[3])
ip_s=ip_b[:int(x[1])]+(32-int(x[1]))*'0'
print(ip_s)

vuvod_n='''
Network:
{0:<8d} {1:<8d} {2:<8d} {3:<8d}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
vuvod_m='''
Mask:
{}
{:<8} {:<8} {:<8} {:<8}
{} {} {} {}
'''
print(vuvod_n.format(int(ip_s[:8],2),int(ip_s[8:16],2),int(ip_s[16:24],2),int(ip_s[24:32],2)))
print(vuvod_m.format('/'+x[1],int(mask[:8],2),int(mask[8:16],2),int(mask[16:24],2),int(mask[24:],2),mask[:8],mask[8:16],mask[16:24],mask[24:]))
