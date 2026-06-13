import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        temperatura = float(request.form["temperatura"])
        humedad = float(request.form["humedad"])
        lluvia = float(request.form["lluvia"])

        if humedad < 30 and lluvia < 50:
            resultado = "Se recomienda REGAR"
        else:
            resultado = "No es necesario regar"

    return render_template(
    "index.html",
    resultado=resultado,
    request=request
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
