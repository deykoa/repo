import sqlite3
import sys
from pprint import pprint

def show_data(db_filename):
    conn = sqlite3.connect(db_filename)
    print('\n Detailed information all base dhcp')
    result = conn.execute('select * from dhcp')
    pprint(result.fetchall())

def show_data_2arg(db_filename,kluch,znach):
    conn = sqlite3.connect(db_filename)
    #Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query = 'select * from dhcp where {} = ?'.format(key)
    result = conn.execute(query, (value, ))

    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
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


