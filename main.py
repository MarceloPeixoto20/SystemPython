from flask import Flask, jsonify, render_template, request, url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__ )
app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'jana90le.'
app.config['MYSQL_DB'] = 'project_system'

mysql = MySQL(app)

@app.route("/", methods=["GET","POST"])
def homepage():
    
    return render_template("homepage.html")

@app.route("/produtos.html", methods=["GET","POST"])
def produtos():
    my_cursor = mysql.connection.cursor()
    my_cursor.execute("SELECT * FROM produtos")
    dados = my_cursor.fetchall()
    if request.method == "POST":

        nproduto = request.form["nproduto"]
        dproduto = request.form["dproduto"]

        
        my_cursor.execute("INSERT INTO produtos (nome_produto,descricao_produto) VALUES (%s,%s)", (nproduto, dproduto))
        mysql.connection.commit()    
        
    my_cursor.close()
    return render_template("produtos.html", produtos=dados)

   
    
    
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    my_cursor = mysql.connection.cursor()
    if request.method == "POST":

        nproduto = request.form["nproduto"]
        dproduto = request.form["dproduto"]

        
        my_cursor.execute("INSERT INTO produtos (nome_produto,descricao_produto) VALUES (%s,%s)", (nproduto, dproduto))
        mysql.connection.commit()
        my_cursor.close()
        return redirect(url_for("produtos"))



@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):

    return render_template("usuraios.html",nome_usuario=nome_usuario)

@app.route("/sucess")
def sucess():
    return 'Logado com sucesso'


if __name__ == "__main__":
    app.run(debug=True)
