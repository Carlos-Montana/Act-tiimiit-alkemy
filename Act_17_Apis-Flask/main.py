'''
Este archivos voy a aplicar conceptos básico de la creación
de api rest con flask, voy a crear rutas, y consultar diferentes rutas
y con diferentes metodos
'''
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def inicio():
    '''
    Esta función define la raiz del proyecto
    '''
    return 'Accediendo a la raiz -_-'


@app.route("/info", methods=["GET", "POST"])
def info():
    '''
    Esta función que define una ruta llamada info
    devuelve info del objeto request de la petición http
    '''
    # En consola usar para el metodo GET
    # curl http://localhost:5000/info
    # En consola usar para el metodo GET
    # curl -X POST http://localhost:5000/info
    cad = ""
    cad += "URL:"+request.url+"\n"
    cad += "Método:"+request.method+"\n"

    cad += "header:\n"
    for item, value in request.headers.items():
        cad += "{}:{}\n".format(item, value)

    cad += "información en formularios (POST):\n"
    for item, value in request.form.items():
        cad += "{}:{}\n".format(item, value)

    cad += "información en URL (GET):\n"
    for item, value in request.args.items():
        cad += "{}:{}\n".format(item, value)

    cad += "Ficheros:\n"
    for item, value in request.files.items():
        cad += "{}:{}\n".format(item, value)

    return cad


@app.route("/listar")
def listar_archivo():
    '''
    Función que se define en la raiz listar, donde
    se va a mostrar un lista que se encuentra en un
    archivo texto.txt
    '''
    # En consola usar para el metodo GET
    # curl http://localhost:5000/listar
    with open('texto.txt', 'r', encoding='UTF-8') as f:
        lista_objetos = f.read()
        lista_objetos = lista_objetos
    return lista_objetos


if __name__ == '__main__':
    app.run(debug=True)
