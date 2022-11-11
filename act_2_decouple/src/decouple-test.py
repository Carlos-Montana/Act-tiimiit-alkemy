# prueba de archivo de conf con base de datos

import mysql.connector
from decouple import config

# extrayendo datos del .env
host = config('HOST')
user = config('USER_DB')
passwd = config('USER_PASS')
db = config('DB')

# conexion a la base de datos mysql
conect = mysql.connector.connect(host=host, user=user, passwd=passwd, db=db)
print(f'Server info -> {conect.get_server_info()}')
print(f'Server version -> {conect.get_server_version()}')
cur = conect.cursor()
cur.execute("select Host, User from user")
for host, userr in cur.fetchall():
    print(f'Host -> {host} :: User -> {userr}')
