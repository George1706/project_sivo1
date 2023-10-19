#Dependencia de flask
from flask import Flask, render_template, request, redirect, url_for, session, flash,jsonify
from flask_login import LoginManager
#Dependencia de configuración
from .config import Config
#dependencia de modelo
from flask_sqlalchemy import SQLAlchemy
#dependencia para las migraciones 
from flask_migrate import Migrate


#crear el objeto flask
app = Flask(__name__)
#Configuracion del objeto flask
app.config.from_object(Config)
#Importar el modulo venta
from app.venta import venta_blueprint
#Vincular submodulos del proyecto
app.register_blueprint(venta_blueprint)
#Importar el modulo producto
from app.producto import producto_blueprint
#Vincular submodulos del proyecto
app.register_blueprint(producto_blueprint)
#Importar el modulo cliente
from app.cliente import cliente_blueprint
from app.usuarios import usuario_blueprint
#Vincular submodulos del proyecto
app.register_blueprint(cliente_blueprint)
app.register_blueprint(usuario_blueprint)
from app.administrador import adminsitrador_blueprint
app.register_blueprint(adminsitrador_blueprint)

#Crear el objetto de Moldelos
db = SQLAlchemy(app)

#Crear objeto de migración
migrate = Migrate(app,db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
    return render_template('index.html' )

@app.route('/verProducto')
def verProducto():
    return render_template('verProducto.html' )
@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html' )
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html' )
@app.route('/productos')
def productos():
    return render_template('productos.html' )
@app.route('/farolas')
def farolas():
    return render_template('farolas.html' )
@app.route('/espejos')
def espejos():
    return render_template('espejos.html' )
@app.route('/puertas')
def puertas():
    return render_template('puertas.html' )
@app.route('/guardafangos')
def guardafangos():
    return render_template('guardafangos.html' )
@app.route('/forros')
def forros():
    return render_template('forros.html' )
@app.route('/radiadores')
def radiadores():
    return render_template('radiadores.html' )


#importar los modelos  de .models
from .models import Producto,Usuario,Cliente,Venta,Administrador

@login_manager.user_loader
def load_user(user_id):
    # Implementa la lógica para cargar un usuario basado en el user_id proporcionado
    try:
        return Usuario.query.get(int(user_id))
    except Exception as e:
        return None 
    
