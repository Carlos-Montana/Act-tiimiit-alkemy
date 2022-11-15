# Actividad 17 - Apis REST - Uso de Flask

### En esta actividad se hace un repaso sobre la sintaxis basica del modulo flask de python, el cual nos sirve para crear apis tipo REST

`Para este ejemplo básico, cree una api que devuelve algo de info de la petición y un lista de prueba`

### Usaremos python, un entorno vitual, el modulo flask y una terminal o navegador para visualizar los resultados obtenidos.

```bash
# Iniciamos el entorno vitual e instalamos flask
python3 -m virtualenv env
source /env/bin/activate
pip install flask

# Levantamos el servidor flask desde main.py
python main.py
```
> Servidor en: http://localhost:5000

### *Accediendo a los diferentes endpoints o urls donde se pueden vizualizar la info y lista.*
<br>

```bash
# Pagina raiz
> Terminal o cmd: curl http://localhost:5000/
> Navegador web : http://localhost:5000/

# Pagina info --> metodo GET
> Terminal o cmd: curl http://localhost:5000/info
> Navegador web : http://localhost:5000/info

# Pagina de info --> metodo POST
> Terminal o cmd : curl -X POST http://localhost:5000/info
> Navegador web  : http://localhost:5000/info

# Pagina listar cadenas de un archivo -- metodo GET
> Terminal o cmd : curl http://localhost:5000/listar
> Navegador web  : http://localhost:5000/listar
```