from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash


# Rota Login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')

    form = FormularioUsuario()

    return render_template('login.html', proxima = proxima, form = form)

# Rota autenticar
@app.route('/autenticar', methods=['POST',])
def autenticar():

    form = FormularioUsuario(request.form)

    # cria a query pra resgatar do banco de dados
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nome + ' logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

# Rota Logout
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))