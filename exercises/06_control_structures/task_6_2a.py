# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:
    x = input('vvidite ip-addres v formate 10.1.1.1: ')
    ipt = x.split('.')
    ip=[]
    for oct in ipt:
        if oct.isdigit() and int(oct)>=0 and int(oct)<=255:
            ip.append(int(oct))
        else:
            x=input('nevernuy format, povtor: ')
            break
    if len(ip)==4:
        break
    else:
        x=input('dolzno dut6 4 okteta  4erez to4ky,povtor: ')
if x=='255.255.255.255':
    print('broadcast')
elif x=='0.0.0.0':
    print('unassigned')
elif ip[0]<=223:
    print('unicast')
elif ip[0]>=224 and ip[0]<=239:
    print('multicat')
else:
    print('unused')
