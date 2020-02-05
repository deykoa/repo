# -*- coding: utf-8 -*-
'''
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
'''

commands = {'192.168.100.1': 'sh ip int br',
            '192.168.100.2': 'sh arp',
            '192.168.100.3': 'sh ip int br'}


from concurrent.futures import ThreadPoolExecutor
import yaml
import netmiko
from itertools import repeat

def send_show(device,show):
    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        strip=ssh.send_command('\n', strip_prompt = False)
        result = ssh.send_command(show,expect_string='#', strip_command=False)
        return str(strip+result)

def send_show_command_to_devices(devices,command_dict,filename,limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        res=executor.map(send_show,devices,command_dict.values())
        with open(filename,'w') as fwr:
            for device,output in zip(devices,res):
                fwr.write(output+'\n')


if __name__=='__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        send_show_command_to_devices(devices,commands,'1.txt')

