__version__ = "1.0"
__author__ = "Julian Camilo Builes Serrano"

import re
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
from components.models import Sucursal, Tecnico, ElementoXTecnico, Elemento

app = Flask(__name__)
CORS(app)
app.config[
    "SECRET_KEY"
] = "1dafafghsdsf5378167uevsbg423)(dfghj98797781234741arfcshzgwffzgnssaerASXMHMRMDwefsrvs8945)(/%#"
app.secret_key = "test_secret"


@app.route("/get_tecnicos", methods=["GET"])
def get_tecnicos():
    """solicitud para obtener la información de todos los tecnicos

    Returns:
        json: estructura con la información de los tecnicos
    """
    tecnicos = Tecnico.get_all()
    response = []
    for tecnico in tecnicos:
        response.append(dict(tecnico))
    return make_response(jsonify(response))


@app.route("/get_todos_los_elementos", methods=["GET"])
def get_todos_los_elementos():
    """funcion que trae todos los elementos que se
    encuntran en el sistema

    Returns:
        json: todos los elementos
    """
    elementos = Elemento.get_todos_los_elementos()
    response = []
    for elemento in elementos:
        response.append(dict(elemento))
    return make_response(jsonify(response))
    pass


@app.route("/get_sucursales", methods=["GET"])
def get_sucurlsales():
    """trae todas las sucursales que estan en el
    sistema
    """
    scursales = Sucursal.get_all()
    response = []
    for sucursal in scursales:
        response.append(dict(sucursal))
    return make_response(jsonify(response))

    return


@app.route("/get_elementos", methods=["POST"])
def get_elementos():
    """se encarga de buscar los elementos
    asignanos para un tecnico
    """
    tecnico = request.json["tecnico"]
    elementos = Tecnico.get_elementos(tecnico)
    response = []
    for elemento in elementos:
        response.append(dict(elemento))
    return make_response(jsonify(response), 200)


@app.route("/insert_elemento_to_tecnico", methods=["POST"])
def insert_elemento():
    """funcion para insertar un elemento a una tecnico, por
    defecto se deja en 1

    tecnico : {
        id:id,
        elemento_id:id
    }
    """
    tecnico = request.json["tecnico"]
    status = ElementoXTecnico.insert_elemento(tecnico)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 200)
    return make_response(jsonify({"response": "ok"}), 200)


@app.route("/insert_tecnico", methods=["POST"])
def insert_tecnicos():
    """insesion de un nuevo tecnico
    estructura base:
    tecnico : {
        id:id,
        nombre:nombre,
        sueldo:salario,
        sucursal_id:sucursal_id
        elementos:[
            {id_elemento_1:cantidad_herramienta<1-10>},
            ...,
            {id_elemento_n:cantidad_herramienta<1-10>}
        ]
    }

    Returns:
        response: json con el status de la solicitud
    """
    tecnico = request.json["tecnico"]
    # generar la validacion de la estructura del id
    id = tecnico["id"]
    if not re.match("^[a-zA-Z0-9]*$", id):
        return make_response(jsonify({"error": "id en formato incorrecto"}), 400)
    if len(tecnico["elementos"]) == 0:
        return make_response(
            jsonify({"error": "tiene que tener minimo un elemento asignado"}), 400
        )
    else:
        for elemento in tecnico["elementos"]:
            elemento_id = elemento["id"]
            cantidad = elemento["cantidad"]
            if cantidad > 10:
                return make_response(
                    jsonify(
                        {
                            "error": "el elemnto {} no puede tener mas de 10 asignaciones".format(
                                elemento_id
                            )
                        }
                    ),
                    400,
                )

    status = Tecnico.instert(tecnico=tecnico)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 200)
    return make_response(jsonify({"response": "ok"}), 200)


@app.route("/update_tecnico", methods=["PUT"])
def update_tecnico():
    """actualizacion de los datos de un tecnico
    estructura de entrada:
    tecnico : {
        id:id,
        nombre:nombre,
        sueldo:salario,
        sucursal_id:sucursal_id
        elementos:[
            {id_elemento_1:cantidad_herramienta<1-10>},
            ...,
            {id_elemento_n:cantidad_herramienta<1-10>}
        ]
    }
    """
    app.logger.info(request.json)
    tecnico = request.json["tecnico"]

    status = Tecnico.update(tecnico, app)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 400)

    return make_response(jsonify({"response": "ok"}), 200)


@app.route("/drop_element", methods=["DELETE"])
def dropElement():
    """funcion para eliminar un elemento a una persona

    tecnico : {
        id:id,
        elemento_id:id
    }
    """
    tecnico = request.json["tecnico"]
    app.logger.info(request.json)
    status = ElementoXTecnico.drop_element(tecnico, app)
    if status != "ok":
        return make_response(jsonify({"response": str(status)}), 400)
    return make_response(jsonify({"response": "ok"}), 200)


@app.route("/delete_tecnico", methods=["DELETE"])
def delete_tecnico():
    """funcion encargada de eliminar un tecnico
    tecnico : {
        id:id
    }
    """
    tecnico = request.json["tecnico"]

    Tecnico.delete(tecnico)

    return make_response(jsonify({"response": "ok"}), 200)


if __name__ == "__main__":
    app.run(port="5001", host="0.0.0.0", debug=True)
