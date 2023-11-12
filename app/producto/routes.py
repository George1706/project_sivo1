from flask import redirect, render_template, request, flash
from sqlalchemy import null
import app
#from app.models import producto
from . import producto_blueprint

#Definir rutas
@producto_blueprint.route('/consultarProducto')
def consultar_producto():
    producto = app.models.Producto.query.all()
    return render_template('consultarProducto.html', producto=producto)

# Ruta para agregar un nuevo producto (CREATE)
@producto_blueprint.route('/registrarProducto', methods=['GET', 'POST'])
def registrar_producto():
    if request.method == 'POST':
        nombreProducto = request.form['nombre']
        precioVentaProducto = request.form['precio']
        unidadMedidaProducto = request.form['unidad']
        stockProducto  = request.form['cantidad']
        descripcionProducto = request.form['descripcion']
        producto = app.models.Producto(nombreProducto=nombreProducto, precioVentaProducto=precioVentaProducto,
                            unidadMedidaProducto=unidadMedidaProducto, stockProducto=stockProducto, 
                            descripcionProducto = descripcionProducto)

        app.db.session.add(producto)
        app.db.session.commit()
        # Mensaje de registro exitoso
        flash('Producto registrado correctamente', 'success')

        return redirect('/Producto/consultarProducto')

    return render_template('registrarProducto.html')

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