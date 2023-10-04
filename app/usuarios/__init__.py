#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
usuario_blueprint = Blueprint ('usuario_blueprint', __name__, url_prefix ='/usuario', template_folder = 'templates')

from . import routes