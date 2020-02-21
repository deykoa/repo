# -*- coding: utf-8 -*-
'''
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
'''
import yaml
from pprint import pprint
from itertools import repeat
from task_22_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor
def send_and_parse_command_parallel(devices,command,template_path,index,max_work=3):
    res=[]
    with ThreadPoolExecutor(max_workers=max_work) as executor:
        result=executor.map(send_and_parse_show_command,devices,repeat(command),repeat(template_path),repeat(index))
        for device, output in zip(devices, result):
            res.append({device['ip']: output})
    return res
if __name__=='__main__':
    with open('devices.yaml') as f:
        devices=yaml.safe_load(f)
        pprint(send_and_parse_command_parallel(devices,'sh ip int br','templates','index'))
