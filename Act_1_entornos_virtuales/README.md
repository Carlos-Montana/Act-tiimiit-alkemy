# Actividad Entornos Virtuales

### Utilizando los conceptos aprendidos en el módulo 1- Entorno virtuales,resolver el siguiente ejercicio:
<br>

    1- Instalar Anaconda
    2- Crear un directorio para proyectos python
    3- Instalar el módulo “venv”.
    4- Crear 2 ambientes virtuales (Ambiente 1 y ambiente 2)
    5- Instalar la última versión de pandas y la de matplotlib en el
    ambiente 1
    6 - Instalar la versión inmediata anterior a la última versión de pandas
    y la de matplotlib en el ambiente 2
    7- Generar el archivo requeriments.txt en cada uno de los ambientes
    8- Verificar el contenido del archivo generado en cada uno de los
    ambientes.
### Resolución

****
- Cree dos entornos virtuales con:
```bash
pip install virtualenv
python3 -m virtualenv env1
python3 -m virtualenv env2
```
- Instale los versiones pedidas y cree el requirements.txt de cada entorno<br>
*activar/desactivar entorno virtual e instalar modulos y luego crear requirements.txt*
```bash
*Desde una consola bash*
source env1/bin/activate (activa el enorno)
pip install pandas matplotlib
pip freeze > requirements-env1.txt
deactivate (desactiva el enorno)
```
```bash
*Desde una consola bash*
source env2/bin/activate (activa el enorno)
pip install pandas==1.5.0 matplotlib==3.5
pip freeze > requirements-env2.txt
deactivate (desactiva el entorno)
```
****

[Volver](../README.md)