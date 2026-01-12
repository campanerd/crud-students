# importando sqlLite3
import sqlite3

# criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:', e)


# criando tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL
        )""")
        
        print('Tabela Cursos criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar a tabela cursos:', e)


# criando tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Turma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES Cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        
        print('Tabela Turmas criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar a tabela turmas:', e)


    # criando tabela de alunos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES Turma (nome) ON DELETE CASCADE
        )""")
        
        print('Tabela Alunos criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar a tabela alunos:', e)


