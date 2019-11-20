import sqlite3
import os

db_exists = os.path.exists('dhcp_snooping.db')
conn = sqlite3.connect('dhcp_snooping.db')

if not db_exists:
    print('Creating schema...')
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print("Done")
    conn.close()
else:
    print('Base already exist')
