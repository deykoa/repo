# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def parse_neighbors(command_output):
    lines=command_output.split('\n')
    mark=False
    ports={}
    for line in lines[:-1]:
        if line.startswith('Device'):
           mark=True
           continue

        if line.endswith('neighbors'):
           dev=line.split('>')

        if mark:
           lin=line.split()
           ports[(dev[0],lin[1]+lin[2])]=(lin[0],lin[-2]+lin[-1])
    return ports


if __name__=='__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        cdp=f.read()
        print(parse_neighbors(cdp))
