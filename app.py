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
    app.run(debug=True)