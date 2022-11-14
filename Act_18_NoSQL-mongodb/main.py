'''
En este script se utilizara de forma basica el modulo pymongo
para realizar diferentes operaciones sobre la base de datos de mongo
'''
from pymongo import MongoClient
from pprint import pprint
from time import sleep

# Uri de mongo
URI = 'mongodb://localhost:27017/'
try:
    # Conectando
    print('Conectando con Mongo\n')
    cliente = MongoClient(URI)
    sleep(2)
except Exception:
    raise ('No se pudo crear conexión con mongodb')

# Creando Base de Datos
print('Creando base de datos\n')
db = cliente.test_python
print(f'Base de datos {db.name} creada correctamente\n')
sleep(2)

# Creando Colección
print('Creando Coleccion\n')
alumnos = db.alumnos
sleep(2)

# Insertando un documento
print('Insertando un documento y varios documentos\n')
datos_alumno1 = {"nombre": "Mike",
                 "edad": "17",
                 "materias": ["programación", "python", "mysql"]}
alumnos_id = alumnos.insert_one(datos_alumno1).inserted_id

# Insertando varios documentos
datos_alumnos = [
    {'name': 'honguito', 'edad': '16', 'materias':
        ['matematica', 'lengua', 'programacion']},
    {'name': 'pepito', 'edad': '17', 'materias':
        ['programacion', 'geografia', 'quimica']},
    {'name': 'fulanito', 'edad': '15', 'materias':
        ['matematica', 'programacion', 'robotica']}
]
results = alumnos.insert_many(datos_alumnos).inserted_ids

# pprint(alumnos.find_one())  # Mostrando documentos
# pprint(db.list_collection_names())  # Mostrando colecciones
sleep(2)

print('Motrando todos los documentos de la colección\n')
sleep(2)
for alumno in alumnos.find():
    pprint(alumno)
