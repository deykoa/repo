# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''

import netmiko
import yaml

command = 'sh ip int br'

def send_show_command(device,command):
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
    except netmiko.ssh_exception.NetMikoAuthenticationException as err1:
        print('oshubka',err1)
        result='wrong pass or login'
    except netmiko.ssh_exception.NetMikoTimeoutException as err2:
        print('oshubka',err2)
        result='wrong ip or interface down'
    return result

with open('devices.yaml') as f:
    devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device,command))
        print('-'*20)

