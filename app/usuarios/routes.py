from flask import Blueprint, render_template, redirect, url_for, flash,request
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, logout_user, current_user


import app
#from app.models import Material
from . import usuario_blueprint
from flask import flash, url_for, render_template

import app

@usuario_blueprint.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombreUsuario = request.form['nombreUsuario']
        correoUsuario = request.form['correoUsuario']
        claveUsuario = request.form['contrasenaUsuario']

        # Verificar si el correo ya está en uso
        usuario_existente = app.models.Usuario.query.filter_by(correoUsuario=correoUsuario).first()

        if usuario_existente:
            flash('El correo electrónico ya está registrado. Por favor, utiliza otro correo.', 'danger')
        else:
            nuevo_usuario = app.models.Usuario(nombreUsuario=nombreUsuario,correoUsuario=correoUsuario,claveUsuario=claveUsuario,  rol_id=2)
            app.db.session.add(nuevo_usuario)
            app.db.session.commit()
           
    return render_template('register.html')

@usuario_blueprint.route('/registroAdmin', methods=['GET', 'POST'])
def registroAdmin():
    if request.method == 'POST':
        nombreUsuario = request.form['nombreUsuario']
        correoUsuario = request.form['correoUsuario']
        claveUsuario = request.form['contrasenaUsuario']

        # Verificar si el correo ya está en uso
        usuario_existente = app.models.Usuario.query.filter_by(correoUsuario=correoUsuario).first()

        if usuario_existente:
            flash('El correo electrónico ya está registrado. Por favor, utiliza otro correo.', 'danger')
        else:
            nuevo_usuario = app.models.Usuario(nombreUsuario=nombreUsuario,correoUsuario=correoUsuario,claveUsuario=claveUsuario,  rol_id=1)
            app.db.session.add(nuevo_usuario)
            app.db.session.commit()
           
    return render_template('adminRegister.html')
        

#METODO PARA CERRAR SESION

@usuario_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@usuario_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correoUsuario = request.form['correoUsuario']
        claveUsuario = request.form['claveUsuario']
        usuario = app.models.Usuario.query.filter_by(correoUsuario=correoUsuario).first()

        if usuario and usuario.claveUsuario == claveUsuario:
            if usuario.is_active:
                login_user(usuario)
                flash(f'Inicio de sesión exitoso {usuario.nombreUsuario}', 'success')
                return redirect(url_for('usuario_blueprint.dashboard'))
            else:
                flash('Tu cuenta está desactivada', 'danger')
        else:
            flash('Credenciales incorrectas', 'danger')

    return render_template('login.html')

@usuario_blueprint.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol.nombre_rol == 'admin':
        return render_template('menuAdministrador.html')
    elif current_user.rol.nombre_rol == 'cliente':
        return render_template('menuClient.html')
    else:
        return "Rol no válido para el dashboard"

