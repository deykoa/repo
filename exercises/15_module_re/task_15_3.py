# -*- coding: utf-8 -*-
'''
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
'''
import re

def convert_ios_nat_to_asa(ios_conf,asa_conf):
    with open(ios_conf) as f, open(asa_conf,'w') as wr_f:
        matches=re.finditer(r'static (\S+) (\S+) (\d+) .+ (\d+)',f.read())
        for match in matches:
            wr_f.write(f'object network LOCAL_{match.group(2)}\n'
                       f' host {match.group(2)}\n'
                       f' nat (inside,outside) static interface service {match.group(1)} {match.group(3)} {match.group(4)}\n')

if __name__=='__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt','cisco_nat_asa.txt')



