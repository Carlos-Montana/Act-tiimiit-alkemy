# Actividad Docstrings con Sphinx en Python
### Utilizando los conceptos aprendidos en el módulo 7 - Docstrings, resolver el siguiente ejercicio.

    Desarrollar un módulo que tenga una clase denominada Empleados
    con las siguientes características.
    Atributos:
        ● nombre
        ● apellido
        ● fecha_nacimiento
        ● nro_dni
    Funciones método:
        ● edad: devuelve la edad en función a la fecha de nacimiento
        ● presentación: devuelve un string donde presenta al empleado:
            ○ Ejemplo: “Hola, soy Juan Pérez. Nací el 01/01/1986 y ni DNI
            es 12345678”
    Documentar el módulo y las funciones utilizando Docstring y de ser
    posible implementar Sphinx para documentar el mismo.

### Resolución

`Para resolver esta actividad cree un entorno virtual, luego lo active, instale la libreria sphinx para poder crear documentación ayudado por los docstring dentro de mi codigo.`

```bash
python3 -m virtualenv env
source /env/bin/activate (activa el entorno virtual)
pip install sphinx
Luego segui los pasos para crear la documentación correspondiente que se encuentra en 
"/docstring-sphinx/_build/html/index.html"
Despues podemos correr el script
python /docstring-sphinx/source/main.py
deactivate (para desactivar el entorno virtual)
```

[Volver](../)