import sqlite3


def criar_db():
    cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, telefone varchar, email text, data text)')


def inserir(n, t, e, d):
    cursor.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?)', (n, t, e, d,))
    conexao.commit()


conexao = sqlite3.connect('crud.db')
cursor = conexao.cursor()
