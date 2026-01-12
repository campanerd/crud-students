#importando dependencias do tkinter
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import Label
from tkinter.ttk import Frame
from tkinter import Button
import tkinter as tk
from tkinter import ttk, messagebox, filedialog as fd
from openpyxl import Workbook


#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


#importando VIEW
from view import *

# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#e5e5e5" # grey
co3 = "#00a095" # Verde
co4 = "#403d3d" # letra
co5 = "#003452" # azul
co6 = "#ef5350" # vermelho
co7 = "#038cfc" # azul
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde


#criando janela
janela = tk.Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(bg=co1)
janela.resizable(width=False, height=False )

style = Style(janela)
style.theme_use("clam")

#criando frames (dividindo)
frame_logo = tk.Frame(janela, width=850, height=52, bg=co8)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky="nsew")

ttk.Separator(janela, orient="horizontal").grid(row=1, columnspan=1, ipadx=680)

frame_dados = tk.Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky="nsew")

ttk.Separator(janela, orient="horizontal").grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = tk.Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky="nsew")

frame_tabela = tk.Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky="nsew")


#=======trabalhando no frame logo=========

app_lg = Image.open('logo alunos.png')
app_lg = app_lg.resize((50, 50), Image.Resampling.LANCZOS)
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text= "Cadastro de Alunos", width=850, compound="left", relief="raised", anchor="nw", font=("Ivy", 15, "bold"), bg=co5, fg=co1)
app_logo.place(x=0, y=0)


#==============funcao cadastro de aluno=================
def aluno():

    #funcao novo aluno
    def novo_aluno():
        #==========funcao para escolher imagem
        global imagem, imagem_string, l_imagem

    
        nome = e_nome.get().strip() 
        email = e_email.get().strip()
        telefone = e_telefone.get().strip()
        sexo = c_sexo.get().strip()
        data = data_nascimento.get().strip()
        cpf = e_cpf.get().strip()
        turma = c_turma.get().strip()

       
        imagem = imagem_string if 'imagem_string' in globals() and imagem_string else ''

        obrigatorios = {"Nome": nome,  "Email": email, "Telefone": telefone, "Sexo": sexo, "Data": data, "CPF": cpf, "Turma": turma}

        for campo, valor in obrigatorios.items():
            if valor is None or str(valor).strip() == "" or valor == "Selecione":
                messagebox.showerror(
            'Erro',
            f'Preencha corretamente o campo: {campo}'
                )
                return



        lista = [nome, email, telefone, sexo, imagem, data, cpf, turma]
        # inserindo dados em um banco de dados
        criar_alunos(lista)

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
    
        #limpando os campos
        e_nome.delete(0, tk.END)
        e_email.delete(0, tk.END)
        e_telefone.delete(0, tk.END)
        c_sexo.set('')
        data_nascimento.delete(0, tk.END)
        e_cpf.delete(0, tk.END)
        c_turma.set('')


        #mostrando os valores na tabela
        mostrar_alunos()


    #funcao atualizar aluno
    def update_aluno():
        #==========funcao para escolher imagem
        global imagem, imagem_string, l_imagem

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']
         
            valor_id = tree_lista[0]

            #limpando os campos
            e_nome.delete(0, tk.END)
            e_email.delete(0, tk.END)
            e_telefone.delete(0, tk.END)
            c_sexo.set('')
            data_nascimento.delete(0, tk.END)
            e_cpf.delete(0, tk.END)
            c_turma.set('')

            #limpando os campos
            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            e_telefone.insert(0, tree_lista[3])
            c_sexo.set(tree_lista[4])
            data_nascimento.insert(0, tree_lista[6])
            e_cpf.insert(0, tree_lista[7])
            c_turma.set(tree_lista[8])

            imagem = tree_lista[5]
            imagem_string = imagem

            #abrindo imagem
            imagem = Image.open(imagem_string)
            imagem = imagem.resize((130, 130), Image.Resampling.LANCZOS)
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co1)
            l_imagem.place(x=300, y=10)

            def update():

                nome = e_nome.get().strip() 
                email = e_email.get().strip()
                telefone = e_telefone.get().strip()
                sexo = c_sexo.get().strip()
                data = data_nascimento.get().strip()
                cpf = e_cpf.get().strip()
                turma = c_turma.get().strip()

            
                imagem = imagem_string if 'imagem_string' in globals() and imagem_string else ''

                obrigatorios = {"Nome": nome,  "Email": email, "Telefone": telefone, "Sexo": sexo, "Data": data, "CPF": cpf, "Turma": turma}

                for campo, valor in obrigatorios.items():
                    if valor is None or str(valor).strip() == "" or valor == "Selecione":
                        messagebox.showerror(
                    'Erro',
                    f'Preencha corretamente o campo: {campo}'
                        )
                        return



                lista = [nome, email, telefone, sexo, imagem, data, cpf, turma, valor_id]
                # atualizando os dados em um banco de dados
                atualizar_alunos(lista)

                # mostrando mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
            
                #limpando os campos
                e_nome.delete(0, tk.END)
                e_email.delete(0, tk.END)
                e_telefone.delete(0, tk.END)
                c_sexo.set('')
                data_nascimento.delete(0, tk.END)
                e_cpf.delete(0, tk.END)
                c_turma.set('')


                #mostrando os valores na tabela
                mostrar_alunos()

                #destruindo botao_update apos usar
                l_imagem.destroy()
                botao_update.destroy()

            botao_update = Button(frame_detalhes, command=update, anchor="center", text="Salvar atualização".upper(), width=17, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
            botao_update.place(x=720, y=120)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos da tabela')


    #funcao deletar aluno
    def deletar_aluno():
        try: 
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']



            valor_id = tree_lista[0]

            #=========deletando os dados no banco de dados========
            deletar_alunos([valor_id])


            # mostrando mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            #mostrando os valores na tabela
            mostrar_alunos()


        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos da tabela')


     # Função ver aluno
    
    def ver_aluno():
        #==========funcao para escolher imagem
        global imagem, imagem_string, l_imagem

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']
         
            valor_id = tree_lista[0]

            #limpando os campos
            e_nome.delete(0, tk.END)
            e_email.delete(0, tk.END)
            e_telefone.delete(0, tk.END)
            c_sexo.set('')
            data_nascimento.delete(0, tk.END)
            e_cpf.delete(0, tk.END)
            c_turma.set('')

            #limpando os campos
            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            e_telefone.insert(0, tree_lista[3])
            c_sexo.set(tree_lista[4])
            data_nascimento.insert(0, tree_lista[6])
            e_cpf.insert(0, tree_lista[7])
            c_turma.set(tree_lista[8])

            imagem = tree_lista[5]
            imagem_string = imagem

            #abrindo imagem
            imagem = Image.open(imagem_string)
            imagem = imagem.resize((130, 130), Image.Resampling.LANCZOS)
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co1)
            l_imagem.place(x=300, y=10)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um aluno da tabela')

    def buscar_aluno():
        nome = e_nome_procurar.get().strip()

        # limpa a tabela antes de mostrar o resultado
        for item in tree_aluno.get_children():
            tree_aluno.delete(item)

        # busca no banco
        resultados = procurar_aluno(nome)

        if not resultados:
            messagebox.showinfo('Aviso', 'Nenhum aluno encontrado')
            return

        for aluno in resultados:
            tree_aluno.insert('', 'end', values=aluno)


    #criando campos de entrada
    l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome = tk.Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome.place(x=7, y=40)

    l_email = Label(frame_detalhes, text="Email *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_email.place(x=4, y=70)
    e_email = tk.Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email.place(x=7, y=100)

    l_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_telefone.place(x=4, y=130)
    e_telefone = tk.Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_telefone.place(x=7, y=160)

    l_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_sexo.place(x=190, y=130)
    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=("Ivy", 8))
    c_sexo['values'] = ("Masculino", "Feminino")
    c_sexo.place(x=190, y=160)

    l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_data_nascimento.place(x=446, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, background='darkblue', foreground='white', borderwidth=2, year=2025)
    data_nascimento.place(x=450, y=40)

    l_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_cpf.place(x=446, y=70)
    e_cpf = tk.Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf.place(x=446, y=100)
   
    l_turma = Label(frame_detalhes, text="Turma *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_turma.place(x=446, y=130)
    c_turma = ttk.Combobox(frame_detalhes, width=18, font=("Ivy", 8))

   #==========pegando as turmas=================
    turmas = ver_turma()
    turma = []

    for i in turmas:
        turma.append(i[1])

    c_turma['values'] = turma
    c_turma.place(x=446, y=158)


    #==========funcao para escolher imagem
    global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem


        imagem = fd.askopenfilename()
        imagem_string = imagem

        #abrindo imagem
        imagem = Image.open(imagem_string)
        imagem = imagem.resize((130, 130), Image.Resampling.LANCZOS)
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co1)
        l_imagem.place(x=300, y=10)


    botao_carregar = Button(frame_detalhes,command=escolher_imagem, text= "Carregar Foto".upper(), width=20, compound="center",anchor="center", overrelief= "ridge", font=("Ivy", 7), bg=co1, fg=co0)
    botao_carregar.place(x=300, y=160)

    #========linha separatoria========

    l_linha = Label(frame_detalhes, relief="groove", text="h", width=1, height=100, anchor="nw", font=("Ivy", 1), bg=co4, fg=co0)
    l_linha.place(x=610, y=10)
    l_linha = Label(frame_detalhes, relief="groove", text="h", width=1, height=100, anchor="nw", font=("Ivy", 1), bg=co9, fg=co0)
    l_linha.place(x=608, y=10)

    l_nome = Label(frame_detalhes, text="Procurar Aluno [Entra o nome]", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_nome.place(x=627, y=10)
    e_nome_procurar = tk.Entry(frame_detalhes, width=17, justify='left', relief='solid', font=('Ivy', 10))
    e_nome_procurar.place(x=630, y=35)

    botao_procurar = Button(frame_detalhes, command=buscar_aluno, text= "Procurar", width=9, overrelief= "ridge", font=("Ivy", 7), bg=co1, fg=co0)
    botao_procurar.place(x=757, y=35)

    #=========botoes=========
    botao_carregar = Button(frame_detalhes, command=novo_aluno, anchor="center", text="Salvar".upper(), width=9, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
    botao_carregar.place(x=627, y=110)

    botao_atualizar = Button(frame_detalhes, command=update_aluno, anchor="center", text="Atualizar".upper(), width=9, overrelief="ridge", font=("Ivy", 7 ),bg=co7, fg=co1)
    botao_atualizar.place(x=627, y=135)

    botao_deletar = Button(frame_detalhes, command=deletar_aluno, anchor="center", text="Deletar".upper(), width=9, overrelief="ridge", font=("Ivy", 7 ),bg=co6, fg=co1)
    botao_deletar.place(x=627, y=160)

    botao_ver = Button(frame_detalhes, command=ver_aluno, anchor="center", text="Ver".upper(), width=9, overrelief="ridge", font=("Ivy", 7 ),bg=co1, fg=co0)
    botao_ver.place(x=727, y=160)

    #=============================Tabela====================================
    #Tabela Alunos
    def mostrar_alunos():
        
        app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1,pady=0, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

        #creating a treeview with dual scrollbars
        list_header = ['id','Nome','email',  'Telefone','sexo', 'imagem', 'Data', 'CPF','Turma']

        df_list = ver_alunos()



        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

        #vertical scrollbar
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        #horizontal scrollbar
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd=["nw","nw","nw","center","center","center","center","nw","nw"]
        h=[30,130,150,70,70,70,80,60,140]
        n=0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor="nw")
            #adjust the column's width to the header string
            tree_aluno.column(col, width=h[n],anchor=hd[n])

            n+=1

        for item in df_list:
            tree_aluno.insert('', 'end', values=item)

    mostrar_alunos()



#==============funcao add cursos e turmas=================
def adicionar():
    #criando frames para tabela
    frame_tabela_curso = tk.Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=5, sticky="nsew")

    frame_tabela_linha = tk.Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky="nsew")

    frame_tabela_turma = tk.Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky="nsew")


#====================detalhes do curso===========

    #=====================funçao novo curso==============
    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()

        lista = [nome, duracao, preco]


        #==========verifica vazio=========
        for i in lista:
            if i=="":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # inserindo dados 
        criar_cursos(lista)

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nome_curso.delete(0, tk.END)
        e_duracao.delete(0, tk.END)
        e_preco.delete(0, tk.END)

        # atualizando tabela sem recriar o Treeview
        for item in tree_curso.get_children():
            tree_curso.delete(item)
        for dados in ver_cursos():
            tree_curso.insert('', 'end', values=dados)

        def atualizar_combobox_cursos():
            cursos = ver_cursos()

            # pega só o nome do curso (posição 1 da tupla)
            nomes = [curso[1] for curso in cursos]

            c_curso['values'] = nomes
            c_curso.set('')
        atualizar_combobox_cursos()

    #=====================funçao atualizar curso==============
    def atualizar_curso_tabela():
        try: 
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]


            #inserindo valores nas entries
            e_nome_curso.insert(0, tree_lista[1])
            e_duracao.insert(0, tree_lista[2])
            e_preco.insert(0, tree_lista[3])

            #==============funcao atualizar=======
            def update():


                nome = e_nome_curso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()

                lista = [nome, duracao, preco, valor_id]


                #==========verifica vazio=========
                for i in lista:
                    if i=="":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return

                # inserindo dados 
                atualizar_curso_dados(lista)

                # mostrando mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                e_nome_curso.delete(0, tk.END)
                e_duracao.delete(0, tk.END)
                e_preco.delete(0, tk.END)

                    # ✅ atualizando tabela sem recriar o Treeview
                for item in tree_curso.get_children():
                    tree_curso.delete(item)
                for dados in ver_cursos():
                    tree_curso.insert('', 'end', values=dados)

                # força a atualização imediata da interface
                tree_curso.update_idletasks()

                def atualizar_combobox_cursos():
                    cursos = ver_cursos()

                    # pega só o nome do curso (posição 1 da tupla)
                    nomes = [curso[1] for curso in cursos]

                    c_curso['values'] = nomes
                    c_curso.set('')
                atualizar_combobox_cursos()

                #destruindo botao salvar apos usar
                botao_salvar.destroy()


            botao_salvar = Button(frame_detalhes, command=update, anchor="center", text="Salvar Atualização".upper(), width=17, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
            botao_salvar.place(x=227, y=130)

        except IndexError:
                messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')
        


    #===========funçao deletar curso============
    def deletar_curso_dados():
        try: 
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']



            valor_id = tree_lista[0]

            #=========deletando os dados no banco de dados========
            deletar_curso([valor_id])


            # mostrando mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # ✅ atualizando tabela sem recriar o Treeview
            for item in tree_curso.get_children():
                tree_curso.delete(item)
            for dados in ver_cursos():
                tree_curso.insert('', 'end', values=dados)


        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')

        def atualizar_combobox_cursos():
            cursos = ver_cursos()

            # pega só o nome do curso (posição 1 da tupla)
            nomes = [curso[1] for curso in cursos]

            c_curso['values'] = nomes
            c_curso.set('')
        atualizar_combobox_cursos()

    


    l_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_curso = tk.Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = tk.Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_preco.place(x=4, y=130)
    e_preco = tk.Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)

    botao_carregar = Button(frame_detalhes, command=novo_curso, anchor="center", text="Criar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)

    botao_atualizar = Button(frame_detalhes, command=atualizar_curso_tabela, anchor="center", text="Atualizar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co7, fg=co1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes, command=deletar_curso_dados, anchor="center", text="Deletar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co6, fg=co1)
    botao_deletar.place(x=267, y=160)

#=============tabela de cursos===============
    def mostrar_cursos():
    # Label de título
        app_nome = Label(
        frame_tabela_curso, text="Tabela de Cursos",
        height=1, anchor="w",
        font=('Ivy 10 bold'), bg=co1, fg=co0
    )
        app_nome.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Cabeçalhos da tabela
    list_header = ['ID', 'Curso', 'Duração', 'Preço']

    # Criando o Treeview
    global tree_curso
    tree_curso = ttk.Treeview(
        frame_tabela_curso, selectmode="extended",
        columns=list_header, show="headings"
    )
    vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
    hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)
    tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree_curso.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')

    frame_tabela_curso.grid_rowconfigure(2, weight=1)
    frame_tabela_curso.grid_columnconfigure(0, weight=1)

    app_nome = Label(
    frame_tabela_curso, text="Tabela de Cursos",
    height=1, anchor="w",
    font=('Ivy 10 bold'), bg=co1, fg=co0
    )
    app_nome.grid(row=0, column=0, columnspan=2, pady=(5, 2), sticky="nsew")

   

#  Cabeçalhos e largura
    hd_heading = ["center","w","center","center"]   # títulos alinhados à esquerda
    hd_column  = ["center","w","center","center"]  # dados: ID centralizado, Curso à esquerda, etc
    h = [30, 160, 80, 60]

    for n, col in enumerate(list_header):
# título da coluna
        tree_curso.heading(col, text=col.title(), anchor=hd_heading[n])
    # conteúdo da coluna
        tree_curso.column(col, width=h[n], anchor=hd_column[n])

 # Pegando os dados do banco e inserindo na tabela
    df_list = ver_cursos()

    for item in df_list:
        tree_curso.insert('', 'end', values=item)

#========linha separatoria========

    l_linha = Label(frame_detalhes, relief="groove", text="h", width=1, height=100, anchor="nw", font=("Ivy", 1), bg=co4, fg=co0)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief="groove", text="h", width=1, height=100, anchor="nw", font=("Ivy", 1), bg=co9, fg=co0)
    l_linha.place(x=372, y=10)
    
#========linha separatoria tabela========

    l_linha = Label(frame_tabela_linha, relief="groove", text="h", width=1, height=140, anchor="nw", font=("Ivy", 1), bg=co4, fg=co0)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief="groove", text="h", width=1, height=140, anchor="nw", font=("Ivy", 1), bg=co9, fg=co0)
    l_linha.place(x=4, y=10)
    
#====================detalhes da turma===========
    l_nome = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = tk.Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_turma.place(x=407, y=40)

    l_turma = Label(frame_detalhes, text="Curso *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)
    
    #==========pegando os cursos=================
    cursos = ver_cursos()
    curso = []

    for i in cursos:
        curso.append(i[1])
    
    c_curso = ttk.Combobox(frame_detalhes, width=20, font=("Ivy", 8))
    c_curso['values'] = (curso)
    c_curso.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de início *", height=1, anchor="nw", font=('Ivy', 10), bg=co1, fg=co4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidth=2, year=2025)
    data_inicio.place(x=407, y=160)

    mostrar_cursos()

    
#======================detalhando as turmas=============================
    #=====================funçao nova turma==============
    def nova_turma():
        nome = e_nome_turma.get()
        curso = c_curso.get()
        data = data_inicio.get()                                                  

        lista = [nome, curso, data]


        #==========verifica vazio=========
        for i in lista:
            if i=="":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # inserindo dados 
        criar_turma(lista)

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        e_nome_turma.delete(0, tk.END)
        c_curso.delete(0, tk.END)
        data_inicio.delete(0, tk.END)
 
        #  atualizando tabela sem recriar o Treeview
        for item in tree_turma.get_children():
            tree_turma.delete(item)
        for dados in ver_turma():
            tree_turma.insert('', 'end', values=dados)


    #=====================funçao atualizar turma==============
    #=====================funçao atualizar curso==============
    def atualizar_turma_tabela():
        try: 
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]


            #inserindo valores nas entries
            e_nome_turma.insert(0, tree_lista[1])
            c_curso.insert(0, tree_lista[2])
            data_inicio.insert(0, tree_lista[3])

            #==============funcao atualizar=======
            def update():


                nome = e_nome_turma.get()
                curso = c_curso.get()
                data = data_inicio.get()

                lista = [nome, curso, data, valor_id]

            
                #==========verifica vazio=========
                for i in lista:
                    if i=="":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return

                # inserindo dados 
                atualizar_turma(lista)

                # mostrando mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                e_nome_turma.delete(0, tk.END)
                c_curso.delete(0, tk.END)
                data_inicio.delete(0, tk.END)

                    # ✅ atualizando tabela sem recriar o Treeview
                for item in tree_turma.get_children():
                    tree_turma.delete(item)
                for dados in ver_turma():
                    tree_turma.insert('', 'end', values=dados)

                # força a atualização imediata da interface
                tree_turma.update_idletasks()
                #destruindo botao salvar apos usar
                botao_salvar.destroy()


            botao_salvar = Button(frame_detalhes, command=update, anchor="center", text="Salvar Atualização".upper(), width=17, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
            botao_salvar.place(x=407, y=130)

        except IndexError:
                messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')
    #===========funçao deletar curso============
    def deletar_turma_dados():
        try: 
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']



            valor_id = tree_lista[0]

            #=========deletando os dados no banco de dados========
            deletar_turma(valor_id)


            # mostrando mensagem de sucesso
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

            # ✅ atualizando tabela sem recriar o Treeview
            for item in tree_turma.get_children():
                tree_turma.delete(item)
            for dados in ver_turma():
                tree_turma.insert('', 'end', values=dados)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos da tabela')



    



    botao_salvar = Button(frame_detalhes, command=nova_turma, anchor="center", text="Criar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co3, fg=co1)
    botao_salvar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes,command=atualizar_turma_tabela, anchor="center", text="Atualizar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co7, fg=co1)
    botao_atualizar.place(x=582, y=160)

    botao_deletar = Button(frame_detalhes, command=deletar_turma_dados, anchor="center", text="Deletar".upper(), width=10, overrelief="ridge", font=("Ivy", 7 ),bg=co6, fg=co1)
    botao_deletar.place(x=657, y=160)

#=============tabela de turmas===============
    def mostrar_turmas():
        app_nome = Label(
            frame_tabela_turma, text="Tabela de Turmas",
            height=1, anchor="w",
            font=('Ivy 10 bold'), bg=co1, fg=co0
    )
        app_nome.grid(row=0, column=0, columnspan=2, sticky="nsew")

    

    list_header = ['ID','Nome da Turma','Curso','Início']

    #  Dados de teste para preencher a tabela
    df_list = ver_turma()

    global tree_turma

    tree_turma = ttk.Treeview(
        frame_tabela_turma, selectmode="extended",
        columns=list_header, show="headings"
    )
    #vertical
    vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
    #horizontal
    hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)
    tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree_turma.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')

    frame_tabela_turma.grid_rowconfigure(1, weight=1)
    frame_tabela_turma.grid_columnconfigure(0, weight=1)
   

#  Cabeçalhos e largura
    hd_heading = ["w","w","w","w"]   # títulos alinhados à esquerda
    hd_column  = ["center","w","center","e"]  # dados: ID centralizado, Curso à esquerda, etc
    h = [30, 130, 150, 80]
    n=0

    for n, col in enumerate(list_header):
        # título da coluna
        tree_turma.heading(col, text=col.title(), anchor=hd_heading[n])
        # conteúdo da coluna
        tree_turma.column(col, width=h[n], anchor=hd_column[n])

        # FORA do loop dos cabeçalhos

    # limpa a tabela antes de inserir
    for item in tree_turma.get_children():
        tree_turma.delete(item)

# insere os dados
    for linha in df_list:
        tree_turma.insert("", "end", values=linha)

    mostrar_turmas()


#==============funcao salvar=================
def gerar_relatorio_excel():
    dados = relatorio_alunos()

    if not dados:
        messagebox.showwarning("Aviso", "Não há dados para gerar o relatório")
        return

    # escolhe onde salvar
    caminho = fd.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Arquivo Excel", "*.xlsx")],
        title="Salvar relatório"
    )

    if not caminho:
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório de Alunos"
    # Cabeçalho
    cabecalho = [
        "Nome", "ID", "Email", "Telefone",
        "Sexo", "Data de Nascimento", "CPF", "Turma"
    ]
    ws.append(cabecalho)

    # Dados
    for aluno in dados:
        ws.append(aluno)

    wb.save(caminho)

    messagebox.showinfo(
        "Sucesso",
        "Relatório gerado com sucesso!"
    )



#==============funcao de controle=================
def control (i):
    #cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
      
        #chamando funcao aluno
        aluno()


    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
      
        #chamando funcao aluno
        adicionar()


    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
      
        #chamando funcao aluno
        salvar()

#==========criando botoes==========
app_img_cadastro = Image.open('ssonar.png')
app_img_cadastro = app_img_cadastro.resize((18, 18), Image.Resampling.LANCZOS)
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, image=app_img_cadastro,command=lambda:control('cadastro'), text= "Cadastro", width=100, compound="left", overrelief= "ridge", font=("Ivy", 11), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

app_img_adicionar = Image.open('ssonar.png')
app_img_adicionar = app_img_adicionar.resize((18, 18), Image.Resampling.LANCZOS)
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, image=app_img_adicionar,command=lambda:control('adicionar'), text= "Adicionar", width=100, compound="left", overrelief= "ridge", font=("Ivy", 11), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

app_img_salvar = Image.open('salvar.png')
app_img_salvar = app_img_salvar.resize((18, 18), Image.Resampling.LANCZOS)
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, image=app_img_salvar,command=gerar_relatorio_excel, text= "Relatório", width=100, compound="left", overrelief= "ridge", font=("Ivy", 11), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)


aluno()
janela.mainloop()

