#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de productos
producto_blueprint = Blueprint ('producto_blueprint', __name__, url_prefix ='/Producto', template_folder = 'templates')

from . import routes