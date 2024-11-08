from flask import Blueprint, request, render_template
from database.models.usuario import Usuario

usuario_route=Blueprint('usuario', __name__)

@usuario_route.route('/inserir_usuario', methods=['POST'])
def inserir_usuario():
    nome=request.form.get('nome')
    email=request.form.get('email')
    Usuario.create(Nome=nome, Email=email)
    return "ok"

@usuario_route.route('/listar_usuarios')
def listar_usuarios():
    usuario=Usuario.select()
    usuario_html="<ul>"
    for usuario in Usuario:
        usuario_html+=f"<li>{usuario.Nome} - {usuario.Email}</li>"
    usuario_html+="</ul>"
    return usuario_html




