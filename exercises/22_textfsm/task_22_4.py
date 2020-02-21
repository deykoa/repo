# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
import yaml
from task_22_3 import parse_command_dynamic
from netmiko import ConnectHandler
def send_and_parse_show_command(device_dict,command,templates_path,index):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        res=ssh.send_command(command)
    result=parse_command_dynamic(res,{'Command':command},index,templates_path)
    return result
if __name__=='__main__':
    with open('devices.yaml') as ff:
        devices=yaml.safe_load(ff)
        for device in devices:
            print(send_and_parse_show_command(device,'sh ip int br','templates','index'))
