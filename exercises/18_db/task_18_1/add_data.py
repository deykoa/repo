import sqlite3
import yaml
import glob
import re
import os

def add_data_to_switch(filename_yaml):
    result = []
    with open(filename_yaml) as f:
        swit = yaml.safe_load(f)
        print('add data to table swithes...')
        for sw in swit['switches'].items():
            try:
                with conn:
                    zapros='''insert into switches (hostname,location) values (?,?)'''
                    conn.execute(zapros,sw)
            except sqlite3.IntegrityError as e:
                print('oshubka',e)

def add_data_to_dhcp():
    snoops=glob.glob('sw*')
    print('Inserting DHCP Snooping data')
    for sw in snoops:
        with open(sw) as f:
            snoop = f.read()
            matches=re.findall('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)',snoop)
            for match in matches:
                match=list(match)
                match.append(sw.split('_')[0])
                try:
                    with conn:
                        query = 'insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'
                        conn.execute(query, match)
                except sqlite3.IntegrityError as e:
                    print('oshubka ', e)

if __name__=='__main__':
    if os.path.exists('dhcp_snooping.db'):
        conn = sqlite3.connect('dhcp_snooping.db')
        add_data_to_switch('switches.yml')
        add_data_to_dhcp()
        conn.close()
    else:
        print('db not exist')
