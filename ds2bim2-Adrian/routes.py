from flask import Flask, redirect, url_for, render_template, request, session, flash
from usuario import Usuario
from usuariodao import UsuarioDao
from ideia import Ideia
from ideiadao import IdeiaDao
import datetime
app = Flask(__name__)
app.env='development'

app.secret_key = '1234 not a good password'

@app.before_request
def before_request():
    if not session['logged_in'] and request.path == '/ideia/listar' :
        return redirect(url_for('logar'))
    elif not session['logged_in'] and request.path == '/ideia/buscar' :
        return redirect(url_for('logar'))
    elif not session['logged_in'] and request.path == '/ideia/salvar' :
        return redirect(url_for('logar'))
    elif not session['logged_in'] and request.path == '/ideia/inserir' :
        return redirect(url_for('logar'))
    elif not session['logged_in'] and request.path == '/ideia/alterar' :
        return redirect(url_for('logar'))
    elif not session['logged_in'] and request.path == '/ideia/excluir' :
        return redirect(url_for('logar'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/logar')
def logar():
    return render_template("login.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    error = None
    usuario = Usuario(login = request.form["login"], senha = request.form["senha"])
    daoU = UsuarioDao()
    u = daoU.buscar(usuario)
    if(u == None):
        error = "Login ou senha incorretos!"
        return render_template('login.html', error=error)
    else:
        session['logged_in'] = True
        session['login'] = request.form["login"]
        session['senha'] = request.form["senha"]
        session['nome'] = u._nome
        session['codU'] = u._cod
        return redirect('index')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('logar')

@app.route('/ideia/listar')
def listar():
    daoI = IdeiaDao()
    lista = daoI.listar(100,0)
    usuario = Usuario(login = session['login'], senha = session['senha'])
    daoU = UsuarioDao()
    u = daoU.buscar(usuario)
    return render_template("listar.html", ideias = lista, usuario = u)

@app.route('/ideia/inserir')
def inserir():
    return render_template("salvar.html")

@app.route('/ideia/alterar')
def alterar():
    cod = int(request.values["cod"])
    dao = IdeiaDao()
    ideia = dao.buscar(cod)
    return render_template('salvar.html', ideia = ideia)

@app.route('/ideia/salvar', methods = ['POST', 'GET'])
def salvar():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    dthoraatt = request.form["dthoraatt"]
    codu = session['codU']
    User = Usuario(cod = codu)
    ideia = Ideia(titulo = titulo, descricao = descricao, usuario=User, datahoraatualizacao = dthoraatt)
    dao = IdeiaDao()
    if(request.values.has_key("cod") == True):
        cod = int(request.values["cod"])
        ideia.cod = int(cod)
    dao.salvar(ideia)
    return redirect(url_for('listar'))

@app.route('/ideia/buscar')
def buscar():
    cod = int(request.values["cod"])
    dao = IdeiaDao()
    buscando = dao.buscar(cod)
    return render_template("buscar.html", buscando = buscando)

@app.route('/ideia/excluir')
def excluir():
    cod = int(request.values["cod"])
    dao = IdeiaDao()
    ideia = Ideia(cod = cod)
    dao.excluir(ideia)
    return redirect(url_for('listar'))

if (__name__ == "__main__"):
    app.run(debug=True, port=5000)