# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
from jinja2 import Template
import yaml

def generate_config(template,data_dict):
    with open(template) as t:
        temp=t.read()
        template=Template(temp)
    with open(data_dict) as f:
        dict_vars=yaml.safe_load(f)
    return template.render(dict_vars)

if __name__=='__main__':
    print(generate_config('templates/for.txt','data_files/for.yml'))
