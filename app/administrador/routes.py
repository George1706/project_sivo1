from flask import redirect, render_template, request
from sqlalchemy import null
import app
#from app.models import producto
from . import adminsitrador_blueprint
# Definir rutas

# Ruta para editar un cliente (UPDATE)
@adminsitrador_blueprint.route('/actualizarAdministrador/<int:id>', methods=['GET', 'POST'])
def actualizar_Administrador(id):
    usuario = app.models.Usuario.query.get(id)

    if request.method == 'POST':
        usuario.codigoUsuario = request.form['codigoUsuarioActualizar']
        usuario.correoUsuario = request.form['correoUsuarioActualizar']
        usuario.nombreUsuario = request.form['nombreUsuarioActualizar']
        usuario.claveUsuario = request.form['claveUsuarioActualizar']

        app.db.session.commit()
        
        return redirect('/Administrador/actualizarAdministrador')
    
    return render_template('menuAdministrador.html', usuario=usuario)

    
