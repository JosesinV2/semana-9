import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

cola = []

# Acepta de una a cuatro palabras compuestas por letras.
# Permite tildes, espacios, guiones y apóstrofos.
PATRON_NOMBRE = re.compile(
    r"[^\W\d_]+(?:[ '-][^\W\d_]+){0,3}",
    re.UNICODE
)


def validar_nombre(nombre):
    if not isinstance(nombre, str):
        return False

    nombre = nombre.strip()

    if not nombre or len(nombre) > 60:
        return False

    return bool(PATRON_NOMBRE.fullmatch(nombre))


def encolar(queue, elemento):
    if not validar_nombre(elemento):
        raise ValueError("Introduce un nombre válido.")

    queue.append(elemento.strip())


def desencolar(queue):
    if not queue:
        return None

    return queue.pop(0)


def esta_vacia(queue):
    return len(queue) == 0


def mostrar_cola(queue):
    return queue.copy()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/api/cola", methods=["GET"])
def obtener_cola():
    return jsonify({
        "cola": mostrar_cola(cola),
        "cantidad": len(cola)
    })


@app.route("/api/encolar", methods=["POST"])
def agregar_nombre():
    datos = request.get_json(silent=True) or {}
    nombre = datos.get("nombre")

    if not validar_nombre(nombre):
        return jsonify({
            "error": (
                "Introduce un nombre de 1 a 4 palabras, "
                "con letras únicamente. Puedes usar tildes, "
                "guiones y apóstrofos."
            )
        }), 400

    encolar(cola, nombre)

    return jsonify({
        "mensaje": f"{nombre.strip()} se agregó a la cola.",
        "cola": mostrar_cola(cola),
        "cantidad": len(cola)
    })


@app.route("/api/desencolar", methods=["POST"])
def quitar_nombre():
    if esta_vacia(cola):
        return jsonify({
            "error": "La cola está vacía."
        }), 400

    nombre = desencolar(cola)

    return jsonify({
        "mensaje": f"Se atendió a {nombre}.",
        "nombre": nombre,
        "cola": mostrar_cola(cola),
        "cantidad": len(cola)
    })


@app.route("/api/vaciar", methods=["POST"])
def vaciar_cola():
    cola.clear()

    return jsonify({
        "mensaje": "La cola se ha vaciado.",
        "cola": mostrar_cola(cola),
        "cantidad": len(cola)
    })


if __name__ == "__main__":
    app.run(debug=True)