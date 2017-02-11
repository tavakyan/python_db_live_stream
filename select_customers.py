
print('Test')

import records

TABLES

LIVE_CONNECT_STRING = 'postgres://localhost:5432/live'
db = records.Database(LIVE_CONNECT_STRING)

rows = db.query('select * from customers')

print(rows)
