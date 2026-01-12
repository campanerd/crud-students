# 📚 Sistema de Cadastro de Alunos (CRUD)

Este projeto é um sistema de **Cadastro de Alunos** desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** como banco de dados.  
O sistema permite realizar operações completas de **CRUD (Create, Read, Update e Delete)**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (Interface gráfica)
- **SQLite3** (Banco de dados)
- **Pillow (PIL)** (Manipulação de imagens)
- **ttk** (Widgets avançados do Tkinter)

---

## 🧠 Organização do Código

- **main.py**
  - Interface gráfica (Tkinter)
  - Eventos dos botões
  - Validação dos campos
  - Integração com a tabela (Treeview)

- **view.py**
  - Criação das tabelas
  - Funções de inserção, leitura, atualização e exclusão
  - Consultas SQL (SELECT, INSERT, UPDATE, DELETE)
    
- **criarbd.py**
  - Criação e inicialização do banco de dados SQLite
  - Definição das tabelas e relacionamentos
  - Garantia da estrutura correta do banco antes da execução do sistema
---

## 💾 Banco de Dados

O sistema utiliza **SQLite**, com tabelas relacionadas para alunos e turmas.  
Os dados são persistidos localmente, garantindo simplicidade e eficiência para projetos acadêmicos e de pequeno porte.

---

## ✅ Cadastro de alunos com:
-  Busca de alunos pelo nome
-  Atualização de dados cadastrados
-  Exclusão de alunos
-  Listagem de alunos em tabela (Treeview)
-  Upload e exibição de imagem do aluno
-  Integração com banco de dados SQLite
-  Interface gráfica simples e intuitiva

---

## 🎓 Referências

Este projeto teve como base um tutorial desenvolvido por **João Futi Muanda | Dev**, que serviu como apoio para a compreensão da estrutura do sistema, implementação das tabelas, operações de CRUD e lógica da interface.

A referência foi utilizada exclusivamente como material de estudo e adaptação durante o desenvolvimento do projeto.

