# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        access,trunk,mark ={},{},0
        for line in f:
            mark+=1
            if line.startswith('interface'):
                intf=line.split()[-1]
                mark=0
            elif 'access vlan' in line:
                port=line.split()[-1]
                access[intf]=int(port)
            elif 'allowed vlan' in line:
                ports=line.split()[-1].split(',')
                trunk[intf]=[int(p) for p in ports]
            elif line.startswith(' duplex') and mark==2:
                access[intf]=1
    return access,trunk
print(get_int_vlan_map('config_sw2.txt'))
