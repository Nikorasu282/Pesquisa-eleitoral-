from os import curdir
import mysql.connector as banco
insert='insert into candidatos(nome,data_nascimento,cpf) values(%s,%s,%s)'
select='select * from candidatos'
insert_votos='insert into votos(id_candidato) values(%s)'
select_relato='select  candidatos.nome, count(id_votos) as quantidade_votos from votos,candidatos where id_candidato = id group by id_candidato order by quantidade_votos DESC '
def insert_cadastro(nome,data,cpf):
    meubanco= banco.connect(host='localhost',
                            user='root',
                            password='admin',
                            database='instituto')
    cursor=meubanco.cursor()
    valores=(nome,data,cpf)
    cursor.execute(insert,valores)
    meubanco.commit()
def select_votos():
    meubanco= banco.connect(host='localhost',
                            user='root',
                            password='admin',
                            database='instituto')
    cursor=meubanco.cursor()
    cursor.execute(select)
    return cursor.fetchall()
def votar(votos):
    meubanco= banco.connect(host='localhost',
                            user='root',
                            password='admin',
                            database='instituto')
    cursor=meubanco.cursor()
    valores=(votos,)
    cursor.execute(insert_votos,valores)
    return meubanco.commit()

def select_relatorio():
    meubanco= banco.connect(host='localhost',
                            user='root',
                            password='admin',
                            database='instituto')
    cursor=meubanco.cursor()
    cursor.execute(select_relato)
    return cursor.fetchall()
    
    
                            
