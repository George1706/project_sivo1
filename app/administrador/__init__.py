#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
adminsitrador_blueprint = Blueprint ('adminsitrador_blueprint', __name__, url_prefix ='/Administrador', template_folder = 'templates')

from . import routes