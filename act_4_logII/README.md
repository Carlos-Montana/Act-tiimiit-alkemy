# Actividad 4 Loguear Eventos 2

### Utilizando los conceptos aprendidos en el módulo 4 - Loguear Eventos II, resolver el siguiente ejercicio.

    Una editorial de cuentos cortos infantiles, que recibe las propuestas
    de los escritores en formato txt, requiere de un programa que realice
    las siguientes funciones al procesar el texto.
    1. Leer un archivo de texto, que se puede descargar en este link.
    2. Contar la cantidad de renglones que tiene el texto.
    3. Contar la cantidad de palabras que tiene cada renglón.
    El programa debe generar 2 archivos de logs que se almacenen en
    la carpeta Logs
    ● En el primero se debe registrar si se pudo leer el archivo o no.
    Utilizar el formato con el que se detalla a continuación.
    ● El segundo archivo de log debe contener:
        ○ nombre del archivo y cantidad de renglones
        ○ nombre del archivo, renglón [nro] y cantidad letras [nro]
    El programa debe tener la siguiente estructura de carpetas y archivos.
    editorial
    |---- main.py
    |---- functions.py
    |---- log_config_file.conf
    |---- cuento.txt
    |---- Logs (folder)
    Pasos a seguir:
    1. Crear el archivo log_config_file.conf: El mismo debe tener 2 loggers
    a. Logger main
    b. Logger functions
    2. Cada logger debe tener 2 handlers:
    a. Para imprimir los mensajes en consola
    b. Para generar los archivos .log en la carpeta Logs.
    3. Utilizar el archivo main.py para abrir el cuentotxt y generar los logs
    utilizando el logger main para indicar si se está procesando o no el
    cuento.txt.
    4. Utilizar el functions.py para crear los 2 loggers y también para procesar
    el cuento.txt con el logger functions, indicando la cantidad de filas y
    palabras por cada una de ellas.

### Resolucíon
****
`En esta actividad desarrolle toda la logica en el script main ejecutando --> python3 /editorial/main.py`
****

[Volver](../README.md)