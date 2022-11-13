# Archivo con todas las configuraciones necesarias
from decouple import config

HOST = config('HOST')
DB = config('DB')
USER_DB = config('USER_DB')
PASSWORD_DB = config('PASSWORD_DB')
DIALECTO = config('DIALECTO')
PORT = config('PORT')
