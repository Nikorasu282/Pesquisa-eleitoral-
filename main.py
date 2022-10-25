
from flask import Flask, render_template, request 
import dao

app=Flask(__name__)

@app.route('/')
def abrir_index():
    return render_template('index.html')
@app.route('/abrir_cadastro')
def abrir_cadastro():
    return render_template('cadastro.html')
@app.route('/cadastro',methods=['POST'])
def coleta_dados_cadastro():
    nome=request.form['nome']
    data=request.form['data_nascimento']
    cpf=request.form['cpf']
    dao.insert_cadastro(nome,data,cpf)
    return render_template('index.html')

@app.route('/abrir_votos')
def abrir_votos():
    return render_template('votos.html',lista_candidatos=dao.select_votos())
    
@app.route('/votar',methods=['POST'])
def coletar_votos():
    votos=request.form['candidato']
    dao.votar(votos,)
    return render_template('index.html')

@app.route('/abrir_relatorio')
def abrir_relatorio():
    return render_template("relatorios.html",relatorio=dao.select_relatorio())
app.run(debug=True)
