# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4, но функция convert_config_to_dict должна поддерживать еще один уровень вложенности.
При этом, не привязываясь к конкретным разделам в тестовом файле.
Функция должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

При записи команд в словарь, пробелы в начале строки надо удалить.

Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Секция итогового словаря на примере interface Ethernet0/3.100:

'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}

Примеры других секций словаря можно посмотреть в тесте к этому заданию.
Тест проверяет не весь словарь, а несколько разнотипных секций.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ignore_l = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    for ign in ignore:
        if ign in command or command.startswith('!'):
            return True
    return False
def convert_config_to_dict(config_filename):
    with open(config_filename) as f:
        conf={}
        for line in f:
            if not ignore_command(line,ignore_l):
                if not line.startswith('  '):
                    if not line.startswith(' '):
                        a=line.strip()
                        conf[line.strip()]=[]
                    else:
                        conf[a].append(line.strip())
                        c=line.strip()
                        mark=True
                else:
                    if mark:
                        conf[a]=dict((k,[]) for k in conf[a])
                        conf[a][c].append(line.strip())
                        mark=False
                    else:
                        conf[a][c].append(line.strip())
    return conf

print(convert_config_to_dict('config_r1.txt'))

