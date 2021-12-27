from flask import Flask, jsonify, request
from flask_cors import CORS
from math import sqrt


app = Flask(__name__)
try:
    app.app_context()
except RuntimeError:
    raise RuntimeError("Error al iniciar la API")

CORS(app, resourser={r"/*": {"origins": "*"}}, supports_credentials=True)


@app.route("/operacion/cuadratica", methods=["POST"])
def rest_cuadratica():
    try:
        valor_a: int = request.json["valor_a"]
        valor_b: int = request.json["valor_b"]
        valor_c: int = request.json["valor_c"]

        result = cuadratica(a=valor_a, b=valor_b, c=valor_c)
        return result

    except ValueError as ve:
        return jsonify({"error": "Error al procesar los valores: {}".format(ve)}), 400


@app.route("/operacion/fibonacci", methods=["POST"])
def rest_fibonacci():
    try:
        valor_n: int = request.json["valor_n"]
        valores = []
        i = 0
        while len(valores) < valor_n:
            result = fibonacci(i)
            valores.append(result)
            i += 1

        return jsonify({"result": valores})
    except ValueError as ve:
        return jsonify({"error": "Error al procesar los valores: {}".format(ve)}), 400


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def cuadratica(a: int, b: int, c: int):
    determinante = b ** 2 - 4 * a * c

    if determinante > 0:
        x1 = -b + sqrt(determinante) / (2 * a)
        x2 = -b - sqrt(determinante) / (2 * a)
        return jsonify({"x1": x1, "x2": x2})
    elif determinante == 0:
        x1 = -b / (2 * a)
        return jsonify({"x": x1})
    else:
        return jsonify({"Operacion": "No tiene solucion"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
