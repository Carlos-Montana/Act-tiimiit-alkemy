# prueba de archivo de conf con base de datos

import mysql.connector
from os import getenv
from dotenv import load_dotenv, find_dotenv

# extrayendo datos del .env
load_dotenv(find_dotenv())
host = getenv('HOST')
user = getenv('USER_DB')
passwd = getenv('USER_PASS')
db = getenv('DB')

# conexion a la base de datos mysql
conect = mysql.connector.connect(host=host, user=user, passwd=passwd, db=db)
print(f'Server info -> {conect.get_server_info()}')
print(f'Server version -> {conect.get_server_version()}')
cur = conect.cursor()
cur.execute("select Host, User from user")
for host, userr in cur.fetchall():
    print(f'Host -> {host} :: User -> {userr}')
