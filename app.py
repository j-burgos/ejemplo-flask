from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

#Instancia de la aplicacion
app = Flask(__name__)

#Configuracion de string de conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#Instancia de la conexion a la base de datos asociada a esta aplicacion
db = SQLAlchemy(app)

#Modelo de base de datos
# internamente se termina convirtiendo en una tabla
class Persona(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(100))

	def __init__(self, nombre):
		self.nombre = nombre

	def __repr__(self):
		return '<Persona: {}>'.format(self.nombre)

	def __str__(self):
		return self.nombre

#Esta instruccion crea el esquema de la base de datos
db.create_all()

#Decorador para indicar una ruta
@app.route('/')
#Funcion/controlador asociado a la ruta
def index():
	nombre = 'Nombre'
	numeros = [persona.nombre for persona in Persona.query.all()]
	#Generar el template
	return render_template('index.html',
		numeros=numeros,
		nombre=nombre)

#Decorador( con ruta con un parametro
@app.route('/param/<int:parametro>')
#En la funcion se recibe con el mismo nombre
def con_param(parametro):
	return 'Venia el parametro: {} en la ruta'.format(parametro)

#Ruta que solo acepta requests por metodo POST
@app.route('/action', methods=['POST'])
def action():
	#Obtener un valor del request mediante POST
	nombre = request.form['nombre']
	#Agregar y realizar el insert en la base de datos
	db.session.add(Persona(nombre))
	db.session.commit()

	return index()

#Decorador para indicar que hacer en dado caso de un codigo de error
@app.errorhandler(404)
#Controlador del codigo de error
def not_found(error):
	return 'Not found'

@app.errorhandler(500)
def server_error(error):
	return 'Internal server error... Sorry about that'

#Si se llama a la aplicacion con 'python app.py'
#el valor __name__ se le asigna un valor de "__main__" y se inicia el servidor
#Pero si este archivo se importa como modulo, entonces no
if __name__ == "__main__":
	app.run(debug=True)