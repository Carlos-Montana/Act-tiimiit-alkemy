# Actividad Testing II

### Utilizando los conceptos aprendidos en el módulo 11 - Testing II, resolver el siguiente ejercicio.

    Tomando como base el ejercicio práctico de la unidad 10
    (Test-Calculadora):
        1- Implementar la librería docs-from-test para incorporar un diagrama
        de la secuencia del test.
        2- Implementar un registro de los resultados tests en formato txt.

### Resolución
****
`Para la primera implementación ejecutamos:`
```bash
python3 -m virtualenv env
source /env/bin/activate
pip install docs-from-test
```
`Despues ingresamos a la carpeta docs-from-test y luego tests y ejecutamos`
```bash
python test.py
```
`En la carpeta docs se genera el diagrama.md`

`Para la segunda implementación ejecutamos:`
```bash
python test_calculadora.py
```
`En la misma carpeta se genera el archivo .txt`
```bash
deactivate (desactivar el entorno virtual)
```
****

[Volver](../README.md)