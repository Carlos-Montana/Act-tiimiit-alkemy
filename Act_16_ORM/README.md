# Actividad Acceso a Base de Datos - ORM(objet relational mapper) - SqlAlchemy

### Para esta actividad voy a seguir la guia practica y tambien voy a complementarle algunas cosas.

- Crear usuarios y roles
- Crar base de datos de practica llamada test
- Insertar datos
- Poder vizualizarlos con python por medio de SQLAlchemy
    1. Crear un archivo que contenga toda la config de la base de datos (.env)
    2. Crear un acrchivo que contenga la config del orm (db.py)
    3. Crear un archivo que contenga los modelos (clases que representan las tablas) para luego poder realizar consultas, etc. (models.py)
    4. Crear un main.py para poder realizar diferente operaciones(insert, update, delete, select).
### Lógica de archivos
- **Archivos de configuracion de base de datos**
    * .env
    * cfg.py
    * db.py
- **Archivos de configuración de logs**
    * logs.conf
- **Archivo para modelar las tablas en clases**
    * models.py
- **Script para iniciar**
    * main.py
### Resolución

> `Para iniciar la base de datos puede ser local o con docker, en este caso explico con docker`

> `Abrir una terminal nueva y luego empezar con:`
```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres123456 -p 5432:5432 postgres:14 
```
> `Luego entramos al container de postgres y creamos la base de datos e insertamos los datos`

> docker exec -it postgres bash (para entrar al container)

> psql postgres postgres (para entra al motor con base de datos y usuario postgres)

> create database test;

> \c test; (cambiar a la base de datos creada)

> create table customer (
	id serial primary key,
	name TEXT,
	age INTEGER,
	email CHARACTER(255),
	address CHARACTER(400),
	zip_code CHARACTER(20)
);

> INSERT INTO customer(_name,_age,email,address,zip_code)
VALUES
('Paul',23,'paul@gmail.com','address from paul','2321LL'),
('Felipe',32,'felipegarcia@gmail.com','address from felipe','3413MS'),
('Teddy',90,'teddy@gmail.com','address from teddy','3423PO'),
('Mark',17,'mark@gmail.com','address from mark','9423MA'),
('David',35,'david@gmail.com','address from david','2341DA'),
('Allen',56,'allen@gmail.com','address from allen','3423PO'),
('James',56,'james@gmail.com','address from james','3423PO');<br>

**Finalizado la parte de postgres**

> `Para iniciar ejecución del script de python:`
```bash
python3 -m virtualenv env (crear el entorno virtual)
source /env/bin/activate (activar entorno virtual)
pip install -r requirements.txt (instala modulos necesarios)
python main.py
deactivate (cerrar el entorno virtual)
```


[Volver](../README.md)