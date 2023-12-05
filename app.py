from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'unicartagena'
 
mysql = MySQL(app)

@app.route("/")
def consulta():
    return render_template("index.html")

@app.route("/pregunta7")
def pregunta7():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT estudiante.nombre AS NOMBRE_ESTUDIANTE , asignatura.nombre AS NOMBRE_ASIGNATURA FROM matricula                    JOIN ESTUDIANTE ON matricula.codigoe = ESTUDIANTE.CODIGOE JOIN ASIGNATURA ON MATRICULA.CODIGOA = ASIGNATURA.CODIGOA")
    
    resultado = cursor.fetchall()

    return render_template("pregunta7.html", raw=resultado)

@app.route("/pregunta8")
def respuesta8():
    cursor = mysql.connection.cursor()

    cursor.execute("UPDATE matricula set promedio = 0.3*nota1 + 0.3*nota2 + 0.4*nota3")
    cursor.execute("SELECT estudiante.nombre FROM estudiante JOIN matricula ON estudiante.codigoe = matricula.codigoe WHERE matricula.promedio > 4")
    
    response = cursor.fetchall()

    return render_template("pregunta8.html", response=response)

@app.route("/pregunta9")
def respuesta9():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT estudiante.nombre, matricula.promedio from estudiante join matricula on estudiante.codigoe = matricula.codigoE order by matricula.promedio desc LIMIT 1;")
    
    response = cursor.fetchall()

    return render_template("pregunta9.html", response9=response[0])

@app.route("/extra")
def extra():
    return render_template("extra.html")

app.run(host="localhost", port=5000)
