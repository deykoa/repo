# -*- coding: utf-8 -*-
'''Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''
from textfsm import TextFSM
from pprint import pprint
def parse_command_output(template,command_output):
    with open(template) as f:
        tabl=TextFSM(f)
        headers=tabl.header
        res = tabl.ParseText(command_output)
        result,intdict=[],{}
        for interf in res:
            for i in range(0,len(headers)):
                intdict[headers[i]]=interf[i]
            result.append(intdict.copy())
    return result


if __name__=='__main__':
    with open('output/sh_ip_int_br.txt') as ff:
        pprint(parse_command_output('templates/sh_ip_int_br.template',ff.read()))
