from flask import redirect, render_template, request, url_for
import app
#from app.models import Venta
from . import venta_blueprint

#Definir rutas
@venta_blueprint.route('/consultarVenta')
def consultar_venta():
    venta = app.models.Venta.query.all()
    return render_template('consultarVenta.html', venta=venta)

# Ruta para agregar un nueva venta (CREATE)
@venta_blueprint.route('/registrarVenta', methods=['GET', 'POST'])
def registrar_Venta():
    if request.method == 'POST':
        codigoVenta = None
        fechaVenta = request.form['fecha']
        cantidadVenta = request.form['cantidad']
        totalVenta = request.form['total']
        codigoProductoFK  = request.form['codigoProductoFK']
        venta = app.models.Venta(codigoVenta=codigoVenta,fechaVenta=fechaVenta, cantidadVenta=cantidadVenta,
                            totalVenta=totalVenta, codigoProductoFK=codigoProductoFK )
        
        app.db.session.add(venta)
        app.db.session.commit()
        return redirect('/Venta/consultarVenta')

    return render_template('registrarVenta.html')

        # Ruta para editar un material (UPDATE)
@venta_blueprint.route('/actualizarVenta/<int:id>', methods=['GET', 'POST'])
def actualizar_venta(id):
    venta = app.models.Venta.query.get(id)
    
    if request.method == 'POST':
        venta.codigoVenta = request.form['codigoVentaActualizar']
        venta.fechaVenta = request.form['fechaActualizar']
        venta.cantidadVenta = request.form['cantidadActualizar']
        venta.totalVenta = request.form['totalActualizar']
        venta.codigoProductoFK = request.form['codigoProductoFKActualizar']
        
        app.db.session.commit()
        
        return redirect('/Venta/consultarVenta')
    
    return render_template('actualizarVenta.html', venta=venta)


# Ruta para eliminar un material (DELETE)
@venta_blueprint.route('/eliminarVenta/<int:id>')
def eliminar_venta(id):
    venta = app.models.Venta.query.get(id)
    
    if venta:
        app.db.session.delete(venta)
        app.db.session.commit()
    
    return redirect('/Venta/consultarVenta')