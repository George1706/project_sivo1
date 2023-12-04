from flask import redirect, render_template, request, flash
from sqlalchemy import null
import app
import os
#from app.models import producto
from . import producto_blueprint
from werkzeug.utils import secure_filename
from random import sample

# Directorio donde se guardarán las imágenes
UPLOAD_FOLDER = 'static/imagenes_producto'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    #Definir rutas



# Ruta para agregar un nuevo producto (CREATE)
@producto_blueprint.route('/registrarProducto', methods=['GET', 'POST'])
def registrar_producto():
    if request.method == 'POST':
        nombreProducto = request.form['nombre']
        precioVentaProducto = request.form['precio']
        unidadMedidaProducto = request.form['unidad']
        stockProducto  = request.form['cantidad']
        descripcionProducto = request.form['descripcion']

        if 'imagen' in request.files:
            file = request.files['imagen']
            if file and allowed_file(file.filename):
                nuevoNombreFile = recibeFoto(file)
                producto = app.models.Producto(nombreProducto=nombreProducto, imagenProducto=nuevoNombreFile,precioVentaProducto=precioVentaProducto,
                            unidadMedidaProducto=unidadMedidaProducto, stockProducto=stockProducto, 
                            descripcionProducto = descripcionProducto)

        app.db.session.add(producto)
        app.db.session.commit()
        # Mensaje de registro exitoso
        flash('Producto registrado correctamente', 'success')

        return redirect('/Producto/consultarProducto')

    return render_template('registrarProducto.html')
@producto_blueprint.route('/consultarProducto')
def consultar_producto():
    producto = app.models.Producto.query.all()
    return render_template('consultarProducto.html', productos=producto)

        # Ruta para editar un producto (UPDATE)
@producto_blueprint.route('/actualizarProducto/<int:id>', methods=['GET', 'POST'])
def actualizar_producto(id):
    producto = app.models.Producto.query.get(id)
    
    if request.method == 'POST':
        producto.codigoProducto = request.form['codigoActualizar']
        producto.nombreProducto = request.form['nombreActualizar']
        producto.precioVentaProducto = request.form['precioActualizar']
        producto.unidadMedidaProducto = request.form['unidadActualizar']
        producto.stockProducto = request.form['stockActualizar']
        producto.descripcionProducto = request.form['descripcionActualizar']
        
        if 'imagenProducto' in request.files:
            file = request.files['imagenProducto']
            if file:
                filename = secure_filename(file.filename)
                if filename:
                    basepath = os.path.dirname(__file__)  # La ruta donde se encuentra el archivo actual
                    nuevoNombreFile = recibeFoto(file)
                    producto.imagenProducto = nuevoNombreFile
        app.db.session.commit()
        # Mensaje de actualizado exitoso
        flash(f'Producto con id:{producto.codigoProducto} actualizado correctamente', 'success')
        return redirect('/Producto/consultarProducto')
    
    return render_template('actualizarProducto.html', producto=producto)


# Ruta para eliminar un producto (DELETE)
@producto_blueprint.route('/eliminarProducto/<int:id>')
def eliminar_producto(id):
    producto = app.models.Producto.query.get(id)
    
    if producto:
        app.db.session.delete(producto)
        app.db.session.commit()
        flash(f'Producto con id:{producto.codigoProducto} actualizado correctamente', 'success')
    return redirect('/Producto/consultarProducto')


def recibeFoto(file):
    basepath = os.path.dirname(__file__)  # La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename)  # Nombre original del archivo

    extension = os.path.splitext(filename)[1]  # Capturando extensión del archivo
    nuevoNombreFile = stringAleatorio() + extension

    upload_path = os.path.join(basepath, './../' + UPLOAD_FOLDER, nuevoNombreFile)
    file.save(upload_path)

    return nuevoNombreFile

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud = 20
    secuencia = string_aleatorio.upper()
    resultado_aleatorio = sample(secuencia, longitud)
    string_aleatorio = "".join(resultado_aleatorio)
    return string_aleatorio