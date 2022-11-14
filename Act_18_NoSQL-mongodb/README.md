# Actividad 18 Base de datos No Relacioneales NoSQL - Mongodb

### Utilizando los conceptos aprendidos en el módulo 18- Bases de datos no relacionales, se pide resolver los siguientes puntos:

    ● Instalar MongoDB y Compass
    ● Acceder desde compass y crear una base de datos
    ● Acceder a MongoDB desde PowerShell
    ● Acceder a la base de datos del paso 2
    ● Crear dos colecciones
    ● Insertar 1 documentos
    ● Insertar varios documentos con un solo comando
    ● Listar los documentos existentes en una colección
    ● Listar un documento específico dentro de la colección
    ● Realizar un update en un registro
    ● Realizar un update a varios registros de forma simultánea

### Resolución
****
*A continucación motrare 2 formas en las que resolvi esta practica, la primera es como se pide en el apunte por medio de la terminal y el software campass, y la segunda por medio de python con el modulo pymongo* <br>

> ACLARACIÓN: USO SISTEMA LINUX

`Primera implementación, utilize una imagen de docker para correr mongo en mi sistema y luego la terminal realize todos puntos que se pide, y en compass chequeaba que este todo bien.`

```bash
# Iniciando Mongo con Docker
docker run --name mongodb -p 27017:27017 mongo:latest

# Entrando al contenedor de mongo
docker exec -it mongodb bash

# Una vez dentro iniciamos mongo y luego creamos la db
> mongo
> use test;

# Creando colecciones e insertando un documento
> db.firstcollection.insertOne(
                    {name:'honguito', edad:30});

# Insertando varios documentos
> db.firstcollection.insertMany([
        {name:'fulano', edad:16},
        {name:'mengano', edad:58},
        {name:'sultano', edad:26}]);

# Listar documentos existentes de una colección
> db.firstcollection.find();

# Lista documento especifico
> db.firstcollection.find({name:{$eq:'carlos'}});

# Actualizar un registro
> db.firstcollection.updateOne({name:'fulano'},
                                {$set:{edad:26}})

# Actualizar varios registro
> db.firstcollection.updateMany({edad:$eq 26},
                                 {$set:{edad:30}})

```
`Segunda implementación es atraves de python, la parte de docker es la misma, una vez que tenga docker andando, procedo a ejecutar el script de python`

```bash
# Desde un terminal levantamos un entorno virtual e instalamos pymongo
python3 -m virtualenv env

source /env/bin/activate

pip install pymongo

python main.py

# Desactivamos el entorno
deactivate
```


[Volver](../README.md)