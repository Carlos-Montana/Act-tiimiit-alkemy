# Actividad Loguear Eventos en Airflow

## Utilizando los conceptos aprendidos en el módulo 5 - Loguear Eventos en Airflow, resolver el siguiente ejercicio.
    En el siguiente link se encuentra un DAG que realiza una consulta a
    una URL y descarga un dataset de medallas olímpicas. Luego
    contabiliza el top ten de países con más medallas y guarda los
    resultados en un archivo en formato Excel.
    Para utilizar este DAG, se deberá descargar y copiar en la carpeta
    DAGs de Airflow.
    A partir del DAG propuesto, completar las partes comentadas, a fin de
    agregar un logger personalizado que realice las siguientes tareas:
        1) Indicarnos si la descarga del dataset se y procesamiento se realizó
        correctamente
        2) Indicarnos si la tarea anterior fue fallida.
        3) Mostrar el logging por consola y también guardarlo en un archivo.

### Resolución

****
`En este ejercicio cree un logger custom y otro de airflow que se ejecuta cuando ejecutamos el dag`
`Importante tener instalado Airflow en local o por medio de docker`<br>
*En local* <br>
[Instalacion en local](https://airflow.apache.org/docs/apache-airflow/stable/start.html)
> En mi caso use la instalación local
```bash
Ejecutar los siguientes comando para arrancarlo:
airflow webserver
airflow scheduler
```
> Luego en el navegador ingresar a http://localhost:8080 e iniciar el dag, los archivos logs se crearan en sus respectivos lugares.

*En docker* <br>
[Instalacion desde docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
****

[Volver](../README.md)