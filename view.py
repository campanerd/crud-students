# importando sqlLite3
import sqlite3 as lite

# criando conexao
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o banco de dados realizada com sucesso!')
except lite.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

# ========= tabela de cursos ==========================================================
#criar cursos (Create [criar] C) Crud
def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query, i)

#criar_cursos (['Python', 'Semanas', 50])

#ver todos os curso (Read [selecionar] R) cRud
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#atualizar os cursos (Update U) crUd
def atualizar_curso_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)



#deletar os cursos (Delete D) cruD
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos Where id=?"
        cur.execute(query, i)

#edletar_curso([1])


# ========= tabela de turmas ==========================================================

#Criar Turmas (inserir)
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turma (nome, curso_nome, data_inicio) VALUES (?,?,?)"
        cur.execute(query, i)

#ver todas as turmas (Read [selecionar] R) cRud
def ver_turma():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turma')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#atualizar as turmas (Update U) crUd
def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turma SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)


#deletar as Turmas (Delete D) cruD
def deletar_turma(i):
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Turma WHERE id = ?", (i,))
        con.commit()

# ========= tabela de alunos =============================================================

#Criar Alunos (inserir)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


#ver todos os Alunos (Read [selecionar] R) cRud
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#atualizar os Alunos (Update U) crUd
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Alunos SET nome=?,email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?,cpf=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)


#deletar os Alunos (Delete D) cruD
def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos Where id=?"
        cur.execute(query, i)

def procurar_aluno(nome):
    with con:
        cur = con.cursor()
        query = """
        SELECT id, nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome
        FROM Alunos
        WHERE nome LIKE ?
        """
        cur.execute(query, (f"%{nome}%",))
        return cur.fetchall()

def relatorio_alunos():
    with con:
        cur = con.cursor()
        query = """
        SELECT 
            nome, id, email, telefone, sexo, 
            data_nascimento, cpf, turma_nome
        FROM Alunos
        ORDER BY nome
        """
        cur.execute(query)
        return cur.fetchall()
