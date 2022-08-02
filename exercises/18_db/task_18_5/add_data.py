import sqlite3
import yaml
import glob
import re
import os
from pprint import pprint
import time

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

def data_for_snoop():
    snoops=glob.glob('sw*')
    result=[]
    for sw in snoops:
            with open(sw) as f:
                snoop = f.read()
                matches=re.findall('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)',snoop)
                for match in matches:
                    match=list(match)
                    match.append(sw.split('_')[0])
                    match.append(1)
                    match.append('Null')
                    result.append(match)
    return result

def add_data_to_dhcp(list_of_hosts):

    with conn:
        curs=conn.execute('select * from dhcp')
        tab=curs.fetchall()
        print('Inserting DHCP Snooping data')
        if tab:
            for i in tab:
                for j in list_of_hosts:
                    if list(i)==list(j):
                        pass
                    else:
                        if i[0]==j[0]:
                            conn.execute('replace into dhcp values {}'.format(tuple(j)))
                        else:
                            if i[0] not in [k[0] for k in list_of_hosts]:
                                i=list(i)
                                i[5]=0

                                print(f'''update dhcp  set ip={i[1]}, vlan={i[2]}, interface={i[3]}, switch={i[4]}, active={i[5]}, last_active=datetime('now') where mac={i[0]}''')
                                conn.execute(f'''update dhcp  set ip='{i[1]}', vlan='{i[2]}', interface='{i[3]}', switch='{i[4]}', active={i[5]}, last_active=datetime('now') where mac='{i[0]}' ''')
                            else:
                                try:
                                    conn.execute('insert into dhcp values {}'.format(tuple(j)))
                                except sqlite3.IntegrityError as e:
                                    print('oshubka',e)
        else:
            for host in list_of_hosts:
                query = '''insert into dhcp (mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, ?)'''
                conn.execute(query, host)

if __name__=='__main__':
    if os.path.exists('dhcp_snooping.db'):
        conn = sqlite3.connect('dhcp_snooping.db')
        add_data_to_dhcp((data_for_snoop()))
        add_data_to_switch('switches.yml')
        conn.close()
    else:
        print('db not exist')
