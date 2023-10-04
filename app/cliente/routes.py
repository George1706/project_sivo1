from flask import redirect, render_template, request
from sqlalchemy import null
import app
#from app.models import producto
from . import cliente_blueprint
# Definir rutas

@cliente_blueprint.route('/consultarCliente')
def consultar_cliente():
    cliente = app.models.Cliente.query.all()
    return render_template('consultarCliente.html', cliente=cliente)

# Ruta para agregar un nuevo cliente (CREATE)
@cliente_blueprint.route('/registrarCliente', methods=['GET', 'POST'])
def registrar_Cliente():
    if request.method == 'POST':
        identificacionCliente = request.form['identificacionCliente']
        tipoIdentificacionCliente = request.form['tipoIdentificacionCliente']
        nombreCliente = request.form['nombreCliente']
        telefonoCliente = request.form['telefonoCliente']
        direccionCliente = request.form['direccionCliente']
        telefono2Cliente = request.form['telefono2Cliente']
        correoCliente = request.form['correoCliente']
        codigoUsuarioFK = request.form['codigoUsuarioFK']
        cliente = app.models.Cliente(identificacionCliente=identificacionCliente, 
                                 tipoIdentificacionCliente=tipoIdentificacionCliente, nombreCliente=nombreCliente,
                                 telefonoCliente=telefonoCliente,direccionCliente=direccionCliente,telefono2Cliente=telefono2Cliente,
                                 correoCliente=correoCliente,codigoUsuarioFK=codigoUsuarioFK)
        
        app.db.session.add(cliente)
        app.db.session.commit()
        return redirect('/Cliente/consultarCliente')

    return render_template('registrarCliente.html')

# Ruta para editar un cliente (UPDATE)
@cliente_blueprint.route('/actualizarCliente/<int:id>', methods=['GET', 'POST'])
def actualizar_Cliente(id):
    cliente = app.models.Cliente.query.get(id)

    if request.method == 'POST':
        cliente.codigoCliente = request.form['codigoClienteActualizar']
        cliente.identificacionCliente = request.form['identificacionClienteActualizar']
        cliente.tipoIdentificacionCliente = request.form['tipoIdentificacionClienteActualizar']
        cliente.nombreCliente = request.form['nombreClienteActualizar']
        cliente.telefonoCliente = request.form['telefonoClienteActualizar']
        cliente.direccionCliente = request.form['direcionClienteActualizar']
        cliente.telefono2Cliente = request.form['telefono2ClienteActualizar']
        cliente.correoCliente = request.form['correoClienteActualizar']
        cliente.codigoUsuarioFK = request.form['codigoUsuarioFKActualizar']

        app.db.session.commit()
        
        return redirect('/Cliente/consultarCliente')
    
    return render_template('actualizarCliente.html', cliente=cliente)

# Ruta para eliminar un cliente (DELETE)
@cliente_blueprint.route('/eliminarCliente/<int:id>')
def eliminar_Cliente(id):
    cliente = app.models.Cliente.query.get(id)
    
    if cliente:
        app.db.session.delete(cliente)
        app.db.session.commit()
    
    return redirect('/Cliente/consultarCliente')
    
