from flask import Flask, render_template

app = Flask(__name__ )
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/produtos.html")
def produtos():
    return render_template("produtos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuraios.html",nome_usuario=nome_usuario)


if __name__ == "__main__":
    app.run(debug=True)