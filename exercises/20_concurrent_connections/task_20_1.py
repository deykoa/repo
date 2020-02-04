# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import subprocess

def ping_subprocess(ip):
    res = subprocess.Popen(['ping', '-c', '3', '-n', ip],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    return res

def ping_ip_addresses(ip_list,limit=3):
    reachable = []
    unreachable = []
    result = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        pings = executor.map(ping_subprocess,ip_list)

    for ip, output in zip(ip_list, pings):
        returncode = output.wait()
        if returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(['8.8.8.8','127.0.0.1','8.8.4.4', '192.168.100.22', '10.10.10.10','192.168.100.2']))
