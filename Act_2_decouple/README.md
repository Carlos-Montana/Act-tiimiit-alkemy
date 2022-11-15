# Actividad Archivos de Configuración

### Utilizando los conceptos aprendidos en el módulo 1- Archivos de Configuración, resolver el siguiente ejercicio:

    1- Instalar VSC
    2- Crear un proyecto Python
    3- Crear un nuevo ambiente virtual llamado venv-decouple
    4- Instalar Decouple
    5- Generar un archivo con variables de entorno para acceder a
    una base de datos MySQL.
    6- Generar una aplicación Python para mostrar por pantalla las
    variables de entorno, utilizando Decouple y Placeholders
    7- Instalar Dotenv
    8- Modificar la aplicación Pyton desarrollada en el punto 6 para
    mostrar las variables de entorno por pantalla utilizado dotenv

### Resolución

****
`Dentro de la carpeta /src se encuentran los scripts para poder ejecutarlos, levantar el entorno con virtual env, instalar el requirements.txt. Y paralelos a esto levantar un entorno docker con mysql para que se puedan ejecutar exitosamente los scripts y listo. 
`
```bash
*Desde una consola bash*
- python3 -m virtualenv env
- source /env/bin/activate (activa el entorno)
- pip install -r requirements.txt
- python /src/docouple-test.py
- python /src/dot-env.py
- deactivate (desactiva el entorno)
```
```bash
*Desde una consola bash*
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
```
****

[Volver](../README.md)