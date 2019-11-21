import sqlite3
import sys
from pprint import pprint

def show_data(db_filename):
    conn = sqlite3.connect(db_filename)
    print('\n Detailed information all base dhcp')
    result = conn.execute('select * from dhcp')
    active,passive=[],[]
    for host in result:
        if host[5]==1:
            active.append(host)
        elif host[5]==0:
            passive.append(host)
    print('Active hosts:')
    pprint(active)
    if passive:
        print('Passive hosts:')
        pprint(passive)

def show_data_2arg(db_filename,kluch,znach):
    conn = sqlite3.connect(db_filename)
    #Позволяет далее обращаться к данным в колонках, по имени колонки
    #conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))
    ress = result.fetchall()
    act,pas=[],[]

    print('Acrive hosts:')
    for row in ress:
        if row[5]==1:
            print(row)
        elif row[5]==0:
            pas.append(row)
    if pas:
        print('Passive hosts:')
        for k in pas:
            print(k)
        print('-' * 40)


if __name__=='__main__':
    if len(sys.argv)==1:
        show_data('dhcp_snooping.db')
    elif len(sys.argv)==3:
        key, value = sys.argv[1:]
        keys = ['mac', 'ip', 'vlan', 'interface','switch']
        keys.remove(key)
        show_data_2arg('dhcp_snooping.db',keys,(value,))
    else: 
        print('2 or 0 argumets are expected')


