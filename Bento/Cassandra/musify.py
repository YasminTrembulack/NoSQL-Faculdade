# https://docs.datastax.com/en/astra-api-docs/_attachments/python-client/astrapy/client.html
# https://dontpad.com/eng_soft_4_b

from astrapy import DataAPIClient
import os, time

# Inicializar o cliente com seu token de aplicação
client = DataAPIClient("AstraCS:ZwCdaeZNkaWHywLvkZbAvAEI:f381fa048e4c40aff8903031163454ba4437a70b751ab531bd9b8a249912f0b8")

# Conectar ao banco de dados usando o endpoint fornecido
db = client.get_database_by_api_endpoint(
  "https://8c44f30f-9729-42fa-9f71-302c0a6c7cd4-us-east1.apps.astra.datastax.com"
)

# Verificar a conexão e listar as coleções/tabelas
print(f"Conectado ao Astra DB: {db.list_collection_names()}")


collection = db.get_collection("musicas")


document = ["titulo", "cantor", "genero", "ano", "album"]
    

def Menu():
    os.system('cls')
    print("-------- Menu --------")
    print("1 - Adicionar Musica")
    print("2 - Visualizar Musica")
    print("3 - Buscar Musica")
    print("4 - Deletar Musica")
    print("5 - Alterar Musica")
    print("0 - Sair")
    op = input("Selecione uma opção:")
    
    if op == "0" : return
    elif op == "1" : return AddMusica()
    elif op == "2" : return ListarMusicas()
    elif op == "3" : return BuscarMusica()
    elif op == "4" : return DeleteMusica()
    elif op == "5" : return AlterarMusica()
    else : return Menu()

def AlterarMusica():
    pass
    

def ListarMusicas():
    os.system('cls')
    print("-------- Lista de Músicas --------")
    
    musicas = collection.find()
    
    if collection.count_documents() == 0:
        print("Nenhuma música encontrada.")
        return Menu()

    for musica in musicas:
        print(f"Título: {musica.get('titulo', 'N/A')}")
        print(f"Cantor: {musica.get('cantor', 'N/A')}")
        print(f"Gêneros: {musica.get('genero', 'N/A')}")
        print(f"Ano: {musica.get('ano', 'N/A')}")
        print(f"Álbum: {musica.get('album', 'N/A')}")
        print("-" * 40)
    
    input("Pressione Enter para voltar ao menu.")
    return Menu()

    
def AddMusica():
    os.system('cls')
    for chave in document:
        novo_valor = input(f"Insira o valor para {chave} ({document[chave]}): ")
        
        if chave in ['ano']:
            novo_valor = int(novo_valor) 
        elif chave in ['compositor', 'genero', 'produção']:
            novo_valor = [item.strip() for item in novo_valor.split(',')]  
      
        document[chave] = novo_valor
    try:
        collection.insert_one(document)
        print("Musica adicionada com sucesso!")
    except:
        print("Erro ao adicionar musica.")
    return

def BuscarMusica():
    os.system('cls')
    for chave in document: print(f"{chave}")
    chave_input = input("Deseja buscar musica por qual campo: ")
    
    if chave_input not in collection.find_one().keys():
        print("Chave inválida")
        return BuscarMusica()
    
    if chave_input == 'ano': value = int(input(f"Digite o valor de {chave_input} que deseja buscar: "))
    else : value = input(f"Digite o valor de {chave_input} que deseja buscar: ")
    
    if chave_input in ['compositor', 'genero', 'produção']:
        value_list = [item.strip() for item in value.split(',')]
        query = {chave_input: {'$in': value_list}}
    else:
        query = {chave_input: value}
    
    result = collection.find(query)

    for musica in result:
        print(musica)
    else:
        print("Nenhuma música encontrada com o valor fornecido.")
    time.sleep(2)
    return Menu()

    
        
def DeleteMusica():
    os.system('cls')
    print("Selecionar por qual campo deseja deletar:")
    print("1 - Album")
    print("2 - Titulo")
    print("3 - Cantor")
    escolha = input("Selecione uma opção: ")

    campo = ''
    if escolha == '1':
        campo = 'album'
    elif escolha == '2':
        campo = 'titulo'
    elif escolha == '3':
        campo = 'cantor'
    else:
        print("Opção inválida.")
        return DeleteMusica()

    valor = input(f"Digite o valor do {campo} para deletar: ")

    # Confirmar exclusão
    confirma = input(f"Você tem certeza que deseja excluir os documentos com {campo} = '{valor}'? (s/n): ").lower()
    if confirma != 's':
        print("Exclusão cancelada.")
        return Menu()

    query = {campo: valor}
    result = collection.delete_many(query)
    if result.deleted_count > 0:
        print(result)
        print(f"{result.deleted_count} documento(s) deletado(s) com sucesso!")
    else:
        print("Nenhum documento encontrado para deletar.")
    time.sleep(2)
    return Menu()
    


os.system('cls')
print("Bem vindo ao Musify!")
time.sleep(2)
Menu()
