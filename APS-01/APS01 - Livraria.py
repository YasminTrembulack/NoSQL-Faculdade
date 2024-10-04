# Bibliotecas
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import json
import os, time
from datetime import datetime

# Carregar e ler o arquivo JSON
with open('./config.json') as config_file:
  config = json.load(config_file)

# Credenciais e URI base
username = config['MONGO_USERNAME']
password = config['MONGO_PASSWORD']

# Escape o nome de usuário e a senha
username = quote_plus(username)
password = quote_plus(password)

# URI de conexão
uri = f"mongodb+srv://{username}:{password}@clusterfaculdade.glgbt.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFaculdade"

# Criar novo cliente e conectar-se ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))

try:
  client.admin.command('ping')
  print("You successfully connected to MongoDB!")
  time.sleep(2)
except Exception as e:
  print("Error connect to MongoDB...")
  print(e)

# Definir o nome do banco de dados
database_name = 'Livraria'
db = client[database_name]

# Definir as tabelas do banco de dados
collectionLivro = db['Livro']
collectionUser = db['User']
collectionEmprestimo = db['Emprestimo']

# Definir o atributos das coleção
livro_data = {
  '_id' : 'ISBN - Codigo unico', 
  'titulo': 'Titulo do livro', 
  'autor': 'Autor do livro', 
  'genero' : 'Digite os generos separados por virgula', 
  'ano_publicacao': 'Ano de publicação', 
  'qtd': 'Quantidade de exemplares no estoque'
}

usuario_data = {
  '_id': 'CPF do usuario',
  'nome' : 'Nome completo', 
  'email': 'Email para login', 
  'nascimento': 'Data de nascimento'
}

emprestimo_data = {
  'livro': 'ISBN do Livro emprestado', 
  'user' : 'CPF do Usuario responsável pelo emprestimo', 
  'data_emprestado': 'Data de emprestimo', 
  'data_entrega': 'Data prevista de devolução', 
  'data_devolvido': 'Data de devolução'
}


def Menu():
  os.system("cls")
  print("--------- Menu ---------")
  print("1. User")
  print("2. Livro")
  print("3. Emprestimo")
  print("0. Sair")
  print("------------------------")
  op = input("Digite a opção desejada: ")
  if op == "1":
    return MenuUser()
  elif op == "2":
    return MenuLivro()
  elif op == "3":
    return MenuEmprestimo()
  elif op == "0":
    return
  else:
    print("Opção inválida. Tente novamente...")
    time.sleep(2)
    return Menu()

def MenuUser():
  os.system("cls")
  print("--------- Menu User ---------")
  print("1. Cadastrar User") # OK
  print("2. Deletar User")
  print("3. Atualizar User")
  print("4. Relatórios Users")
  print("5. Emprestimos User")
  print("0. Voltar")
  print("-----------------------------")

  op = input("Digite a opção desejada: ")
  if op == "1":
    return CadastrarUser()
  elif op == "2":
    return DeletarUser()
  elif op == "3":
    return AtualizarUser()
  elif op == "4":
    return RelatoriosUser()
  elif op == "5":
    return EmprestimoUser()
  elif op == "0":
    return Menu()
  else:
    print("Opção inválida. Tente novamente...")
    time.sleep(2)
    return MenuUser()

def MenuLivro():
  os.system("cls")
  print("--------- Menu Livro ---------")
  print("1. Cadastrar Livro") # OK
  print("2. Deletar Livro")
  print("3. Atualizar Livro")
  print("4. Listar Livro Disponiveis")
  print("5. Relatórios Livros")
  print("0. Voltar")
  print("------------------------------")

  op = input("Digite a opção desejada: ")
  if op == "1":
    return CadastrarLivro()
  elif op == "2":
    return DeletarLivro()
  elif op == "3":
    return AtualizarLivro()
  elif op == "4":
    return ListarLivrosDisponiveis()
  elif op == "5":
    return RelatorioLivros()
  elif op == "0":
    return Menu()
  else:
    print("Opção inválida. Tente novamente...")
    time.sleep(2)
    return MenuLivro()

def MenuEmprestimo():
  os.system("cls")
  print("--------- Menu Emprestimo ---------")
  print("1. Emprestar Livro")
  print("2. Devolver Livro")
  print("3. Emprestimos Vencidos")
  print("4. Buscar Emprestimos Data")
  print("0. Voltar")
  print("-----------------------------------")

  op = input("Digite a opção desejada: ")
  if op == "1":
    return EmprestarLivro()
  elif op == "2":
    return DevolverLivro()
  elif op == "3":
    return EmprestimosVencidos()
  elif op == "4":
    return BuscarEmprestimoData()
  elif op == "0":
    return Menu()
  else:
    print("Opção inválida. Tente novamente...")
    time.sleep(2)
    return MenuEmprestimo()




# ------------------------- Livro -------------------------
def CadastrarLivro():
  os.system("cls")
  for chave in livro_data:
    novo_valor = input(f"Insira o valor para {chave} ({livro_data[chave]}): ")

    if chave in ['ano_publicacao', 'qtd']:
      novo_valor = int(novo_valor) 
    elif chave == 'genero':
      novo_valor = [item.strip() for item in novo_valor.split(',')]  

    livro_data[chave] = novo_valor
  try:
    collectionLivro.insert_one(livro_data)
    print("Livro adicionado com sucesso!")
  except error:
    print("Erro ao adicionar livro.")
  time.sleep(2)
  return MenuLivro()


def DeletarLivro():
  os.system("cls")
  pass


def AtualizarLivro():
  os.system("cls")
  pass

def ListarLivrosDisponiveis():
  # • Listar livros disponíveis para empréstimo
  os.system("cls")
  pass

def RelatorioLivros():
  # • Relatório de todos os livros cadastrados
  os.system("cls")
  pass



# ------------------------- User -------------------------
def CadastrarUser():
  os.system("cls")
  for chave in usuario_data:
    novo_valor = input(f"Insira o valor para {chave} ({usuario_data[chave]}): ")

    usuario_data[chave] = novo_valor
  try:
    collectionUser.insert_one(usuario_data)
    print("Usuário adicionado com sucesso!")
  except error:
    print("Erro ao adicionar usuário.")
  time.sleep(2)
  return MenuUser()


def DeletarUser():
  os.system("cls")
  pass


def AtualizarUser():
  os.system("cls")
  pass


def RelatoriosUser():
   # • Relatório de todos os usuários cadastrados
  os.system("cls")
  pass


def EmprestimoUser():
   # • Consultar os empréstimos em aberto de um usuário específico
  os.system("cls")
  pass


# ------------------------- Emprestimo -------------------------
def EmprestarLivro():
  os.system("cls")
  for chave in emprestimo_data:
    if chave == 'data_emprestado':
      emprestimo_data[chave] = datetime.now()
      continue
      
    
    busca = input(f"Insira o valor para {chave} ({emprestimo_data[chave]}): ")
    if chave == 'livro':
      novo_valor = findInCollection('Livro', '_id', busca)
      
    emprestimo_data[chave] = novo_valor
  try:
    collectionUser.insert_one(emprestimo_data)
    print("Usuário adicionado com sucesso!")
  except error:
    print("Erro ao adicionar usuário.")
  time.sleep(2)
  return MenuUser()
  # • Verificar se há exemplares disponíveis do livro
  # • Registrar o empréstimo, associando o livro ao usuário
  # • Atualizar a quantidade de exemplares disponíveis
  # • Registrar a data do empréstimo e a data prevista de devolução
  pass


def DevolverLivro():
  os.system("cls")
  # • Atualizar a quantidade de exemplares disponíveis do livro
  # • Registrar a data de devolução.
  pass


def EmprestimosVencidos():
  # • Consultar usuários com empréstimos vencidos
  os.system("cls")
  pass
  

def BuscarEmprestimoData():
  # • Relatório de todos os empréstimos realizados em um período de tempo específico
  os.system("cls")
  pass


def findInCollection(collection, coluna, value):
  # Obter a collection
  collection = db[collection_name]

  # Criar consulta para buscar o valor em um campo específico
  query = {field_name: value}
  
  # Procurar o primeiro documento que corresponda à consulta
  result = collection.find_one(query)

  # Verificar se encontrou o resultado
  if result:
    return result
  else:
    return None

Menu()