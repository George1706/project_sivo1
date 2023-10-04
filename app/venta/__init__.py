#Dependencia para hacer un blueprint/paquete
from flask import Blueprint

#Definir paquete de ventas
venta_blueprint = Blueprint ('venta_blueprint', __name__, url_prefix ='/Venta', template_folder = 'templates')

from . import routes