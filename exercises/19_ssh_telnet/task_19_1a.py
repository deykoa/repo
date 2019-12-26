# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''

import netmiko
import yaml

command = 'sh ip int br'

def send_show_command(device,command):
    try:
        with netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_command(command)
    except netmiko.ssh_exception.NetMikoAuthenticationException as err:
        print('oshubka',err)
        result='wrong pass or login'
    return result

with open('devices.yaml') as f:
    devices = yaml.safe_load(f)
    for device in devices:
        print(send_show_command(device,command))
        print('-'*20)

