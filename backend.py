import mysql.connector as c
import config

# The connection has been established on config.py file
db_conn = config.conn
cur = db_conn.cursor()

sql = "INSERT INTO TABLE_NAME (name, address) VALUES (%s, %s)"
val = ("USERNAME", "BOOKING_SLOT")

cur.execute(sql,val)
db_conn.commit()
print(cur.rowcount, "record inserted.")
for x in cur:
    print(x) 
