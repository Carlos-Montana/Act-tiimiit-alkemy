# Actividad Testing II

### Utilizando los conceptos aprendidos en el módulo 11 - Testing II, resolver el siguiente ejercicio.

    Tomando como base el ejercicio práctico de la unidad 10
    (Test-Calculadora):
        1- Implementar la librería docs-from-test para incorporar un diagrama
        de la secuencia del test.
        2- Implementar un registro de los resultados tests en formato txt.

### Resolución
****
`Para las implementaciones ejecutamos:`
```bash
python3 -m virtualenv env
source /env/bin/activate
pip install docs-from-test
```
> **Primera Implementación**

`Despues ingresamos a la carpeta docs-from-test y luego tests y ejecutamos`
```bash
python test.py
```
`En la carpeta docs se genera el diagrama.md el cual puedes ver `[pinchando aqui](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5DYWxjdWxhZG9yYS5hZGQ6IGNhbGxzIHgxCiAgQ2FsY3VsYWRvcmEuYWRkLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5DYWxjdWxhZG9yYS5tdWx0aXBsaWNhdGlvbjogY2FsbHMgeDEKICBDYWxjdWxhZG9yYS5tdWx0aXBsaWNhdGlvbi0tPj5zdGFydDogcmV0dXJucyBmbG9hdAogIHN0YXJ0LT4+Q2FsY3VsYWRvcmEuc3Vic3RyYWN0OiBjYWxscyB4MgogIENhbGN1bGFkb3JhLnN1YnN0cmFjdC0tPj5zdGFydDogcmV0dXJucyBmbG9hdAogIHN0YXJ0LT4+Q2FsY3VsYWRvcmEuZGl2aWRlOiBjYWxscyB4MQogIENhbGN1bGFkb3JhLmRpdmlkZS0tPj5zdGFydDogcmV0dXJucyBmbG9hdAo=)

> **Segunda Implementación**

`Para la segunda implementación ejecutamos:`
```bash
python test_calculadora.py
```
`En la misma carpeta se genera el archivo .txt, puedes verlo `[pinchando aqui](./docs-from-test/tests/testing.txt)

>*Recomendación*: **Abrir links en pestaña nueva.**

```bash
deactivate (desactivar el entorno virtual)
```
****

[Volver](../README.md)