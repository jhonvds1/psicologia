from flask import render_template, Blueprint, request
from database.models.blog import Blog

home_route=Blueprint('home',__name__)

@home_route.route("/")
def homepage():
    return render_template("main.html")

@home_route.route("/inserir_blog")
def home_blog():
    return render_template('inserir_blog.html')


@home_route.route("/ques_blog", methods=['POST'])
def inserir_blog():
    titulo=request.form.get('titulo')
    autor=request.form.get('autor')
    materia=request.form.get('conteudo')
    Blog.create(Titulo=titulo, Autor=autor, Materia=materia)
    return '<a href="inserir_blog" class="voltar">Fazer outro post</a>'


@home_route.route("/blog")
def mostrar_blog():
    posts=Blog.select()
    return render_template('blog.html', posts=posts)

#@home_route.route('/listar_materias')
#def listar_materias():
 #   materias=Blog.select()
  #  materia_html="<ul>"
   # for materia in Blog:
   #     materia_html+=f"<li>{materia.Titulo} - {materia.Autor} - {materia.Materia} </li>"
   # materia_html+="</ul>"
   # return materia_html

