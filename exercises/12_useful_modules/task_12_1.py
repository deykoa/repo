# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess

def ping_ip_addresses(list_ip):
    pings,notpings=[],[]
    for ip in list_ip:
        result=subprocess.run('ping {} -c 3 -n'.format(ip))
        if result.returncode == 0:
            pings.append(ip)
        else:
            notpings.append(ip)

    return (pings,notpings)
