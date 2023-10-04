#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
cliente_blueprint = Blueprint ('cliente_blueprint', __name__, url_prefix ='/Cliente', template_folder = 'templates')

from . import routes