# Bibliotecas
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import json
import os, time
from datetime import datetime, timedelta

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
except Exception as e:
  print("Error connect to MongoDB...")
  time.sleep(2)

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
  
  if   op == "1": return MenuUser()
  elif op == "2": return MenuLivro()
  elif op == "3": return MenuEmprestimo()
  elif op == "0": return
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
  
  if   op == "1": return CadastrarUser()
  elif op == "2": return DeletarUser()
  elif op == "3": return AtualizarUser()
  elif op == "4": return RelatoriosUser()
  elif op == "5": return EmprestimoUser()
  elif op == "0": return Menu()
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
  
  if   op == "1": return CadastrarLivro()
  elif op == "2": return DeletarLivro()
  elif op == "3": return AtualizarLivro()
  elif op == "4": return ListarLivrosDisponiveis()
  elif op == "5": return RelatorioLivros()
  elif op == "0": return Menu()
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
  
  if   op == "1": return EmprestarLivro()
  elif op == "2": return DevolverLivro()
  elif op == "3": return EmprestimosVencidos()
  elif op == "4": return BuscarEmprestimoData()
  elif op == "0": return Menu()
  else:
    print("Opção inválida. Tente novamente...")
    time.sleep(2)
    return MenuEmprestimo()




# ------------------------- Livro -------------------------
def CadastrarLivro():
  os.system("cls")
  
  livro_data_local = livro_data.copy()
  
  for chave in livro_data:
    novo_valor = input(f"Insira o valor para {chave} ({livro_data_local[chave]}): ")

    if chave in ['ano_publicacao', 'qtd']:
      novo_valor = int(novo_valor) 
    elif chave == 'genero':
      novo_valor = [item.strip() for item in novo_valor.split(',')]  

    livro_data_local[chave] = novo_valor
  try:
    collectionLivro.insert_one(livro_data_local)
    print("Livro adicionado com sucesso!")
  except Exception as e:
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
  
  usuario_data_local = usuario_data.copy()
  
  for chave in usuario_data:
    novo_valor = input(f"Insira o valor para {chave} ({usuario_data_local[chave]}): ")

    usuario_data_local[chave] = novo_valor
  try:
    collectionUser.insert_one(usuario_data_local)
    print("Usuário adicionado com sucesso!")
  except Exception as e:
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
  
  emprestimo_data_local = emprestimo_data.copy()
  
  # Atualizando as datas
  data_atual = datetime.now()
  emprestimo_data_local['data_emprestado'] = data_atual
  emprestimo_data_local['data_entrega'] = data_atual + timedelta(days=7)
  emprestimo_data_local['data_devolvido'] = None

  # Coletando informações do livro e do usuário
  for chave in ['livro', 'user']:
      busca = input(f"Insira o valor para {chave} ({emprestimo_data_local[chave]}): ")
      
      # Buscando o livro ou o usuário na coleção
      novo_valor = findInCollection('Livro' if chave == 'livro' else 'User', '_id', busca)

      # Verificando se o livro está disponível
      if chave == 'livro':
          if novo_valor['qtd'] == 0:
              print("Livro sem exemplares disponíveis.")
              time.sleep(2)
              return MenuEmprestimo()

      if novo_valor is None:
          print(f"{chave.capitalize()} não encontrado.")
          time.sleep(2)
          return MenuEmprestimo()

      emprestimo_data_local[chave] = novo_valor

  # Registrando o empréstimo
  try:
    collectionEmprestimo.insert_one(emprestimo_data_local)
    
    # Atualiza a quantidade do livro
    collectionLivro.update_one(
      {'_id': emprestimo_data_local['livro']['_id']},  # Usando o ISBN diretamente
      {'$inc': {'qtd': - 1}}  # Decrementa a quantidade em 1
    )
    
    print("Empréstimo realizado com sucesso!")
  except Exception as e:
    print(f"Erro ao emprestar livro: {e}")

  time.sleep(2)
  return MenuEmprestimo()


def DevolverLivro():
  os.system("cls")
  # Solicitar o CPF do usuário
  cpf_usuario = input("Insira o CPF do usuário: ")

  # Buscar o usuário pelo CPF
  usuario = collectionUser.find_one({'_id': cpf_usuario})
  
  if not usuario:
    print("Usuário não encontrado.")
    time.sleep(2)
    return MenuEmprestimo()

  # Buscar empréstimos em aberto do usuário
  emprestimos_abertos = collectionEmprestimo.find({
    'user': usuario,
    'data_devolvido': None  # Apenas os empréstimos ainda não devolvidos
  })

  # Verificar se existem empréstimos em aberto
  emprestimos = list(emprestimos_abertos)
  if not emprestimos:
    print("Nenhum empréstimo em aberto encontrado para este usuário.")
    time.sleep(2)
    return MenuEmprestimo()

  # Listar os empréstimos em aberto
  print("Empréstimos em aberto:")
  for idx, emprestimo in enumerate(emprestimos):
    print(f"{idx + 1}. Livro: {emprestimo['livro']['_id']} - {emprestimo['livro']['titulo']} - {emprestimo['livro']['autor']}, Data de Entrega: {emprestimo['data_entrega']}")

  # Solicitar o número do empréstimo a ser devolvido
  indice = int(input("Escolha o número do empréstimo a ser devolvido: ")) - 1
  if indice < 0 or indice >= len(emprestimos):
    print("Opção inválida.")
    time.sleep(2)
    return DevolverLivro()

  # Obter os dados do empréstimo selecionado
  emprestimo_selecionado = emprestimos[indice]
  livro_isbn = emprestimo_selecionado['livro']['_id']

  # Atualizar a quantidade de exemplares disponíveis do livro
  try:
    collectionLivro.update_one(
      {'_id': livro_isbn},
      {'$inc': {'qtd': 1}}  # Incrementa a quantidade em 1
    )

    # Registrar a data de devolução
    collectionEmprestimo.update_one(
      {'_id': emprestimo_selecionado['_id']},
      {'$set': {'data_devolvido': datetime.now()}}  # Define a data de devolução como agora
    )

    print("Devolução registrada com sucesso!")
      
  except Exception as e:
    print(f"Erro ao devolver o livro: {e}")

  time.sleep(2)
  return MenuEmprestimo()


def EmprestimosVencidos():
  os.system("cls")
  print("--------- Empréstimos Vencidos ---------")
  
  # Obtendo a data atual
  data_atual = datetime.now()
  
  # Buscando empréstimos vencidos
  emprestimos_vencidos = collectionEmprestimo.find({
      'data_entrega': {'$lt': data_atual},
      'data_devolvido': None  # Verifica se ainda não foi devolvido
  })

  # Exibindo os resultados
  found = False
  for emprestimo in emprestimos_vencidos:
    found = True
    print(f"Livro: {emprestimo['livro']['_id']} - {emprestimo['livro']['titulo']} - {emprestimo['livro']['autor']}")
    print(f"Usuário: {emprestimo['user']['_id']} - {emprestimo['user']['nome']}")
    print(f"Data Emprestado: {emprestimo['data_emprestado']}")
    print(f"Data Entrega: {emprestimo['data_entrega']}")
    print("-----------------------------------")

  if not found:
    print("Nenhum empréstimo vencido encontrado.")

  input('Digite qualquer tecla para continuar...')
  return MenuEmprestimo()
  

def BuscarEmprestimoData():
  os.system("cls")
  
  # Solicitar datas de início e fim
  data_inicio_str = input("Insira a data de início (YYYY-MM-DD): ")
  data_fim_str = input("Insira a data de fim (YYYY-MM-DD): ")

  # Converter as strings de data para objetos datetime
  try:
    data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d')
    data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d')
  except ValueError:
    print("Formato de data inválido. Use YYYY-MM-DD.")
    time.sleep(2)
    return MenuEmprestimo()

  # Garantir que a data de início seja menor que a data de fim
  if data_inicio > data_fim:
    print("A data de início deve ser anterior à data de fim.")
    time.sleep(2)
    return MenuEmprestimo()

  # Buscar empréstimos no intervalo de datas
  emprestimos = collectionEmprestimo.find({
    'data_emprestado': {
      '$gte': data_inicio,  # Maior ou igual à data de início
      '$lte': data_fim      # Menor ou igual à data de fim
    }
  })

  # Exibir resultados
  emprestimos_list = list(emprestimos)
  if not emprestimos_list:
    print("Nenhum empréstimo encontrado no período especificado.")
  else:
    os.system("cls")
    print("--------- Empréstimos Encontrados ---------")
    for emprestimo in emprestimos_list:
      print(f"Livro: {emprestimo['livro']['_id']} - {emprestimo['livro']['titulo']} - {emprestimo['livro']['autor']},")
      print(f'Usuário: {emprestimo['user']['_id']} - {emprestimo['user']['nome']},')
      print(f"Data Emprestado: {emprestimo['data_emprestado']},")
      print(f"Data Entrega: {emprestimo['data_entrega']},")
      print(f"Data Devolvido: {emprestimo['data_devolvido']}")
      print("------------------------------------------")

      
      
  input('Digite qualquer tecla para continuar...')
  return MenuEmprestimo()


def findInCollection(collection_name, field_name, value):
  # Obter a collection
  collection = db[collection_name]

  # Criar consulta para buscar o valor em um campo específico
  query = {field_name: value}
  
  # Procurar o primeiro documento que corresponda à consulta
  result = collection.find_one(query)
  
  return result
  

Menu()