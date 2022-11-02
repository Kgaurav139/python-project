# Connection config variable ---> Can ignore it on git push
import mysql.connector as sql_connect
db_host = "localhost"
db_port = "3307"
db_user = "root"
db_password = "admin"
db_database = "prakum"

# Final Connection variable
conn = sql_connect.connect(host = db_host, port = db_port, user = db_user, password = db_password, database = db_database)