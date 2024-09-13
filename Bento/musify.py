from pymongo import MongoClient
import os, time

uri = "mongodb+srv://yasminagostinho012:N9357iG1m8ifKn5K@clusterfaculdade.glgbt.mongodb.net/"

client = MongoClient(uri)

print(client.list_database_names())

db = client['Musify']

# print(db.list_collection_names())

collection = db['Musica']

# print(collection.find_one())

document = {
    "titulo": "Título da Música",                                       # Título da música
    "cantor": "Artista ou Banda que Interpreta a Música",               # Artista ou banda que interpreta a música
    "duração": "Duração da Música (formato minutos:segundos)",          # Duração da música
    "ano": 0000,                                                        # Ano de lançamento da música
    "compositor": ["Nome do Compositor 1", "Nome do Compositor 2"],     # Lista de compositores
    "genero": ["Gênero Musical 1", "Gênero Musical 2"],                 # Lista de gêneros musicais
    "letra": "Letra da Música",                                         # Letra da música
    "gravadora": "Nome da Gravadora",                                   # Gravadora responsável pelo lançamento
    "album": "Título do Álbum",                                         # Álbum ao qual a música pertence
    "produção": ["Nome do Produtor 1", "Nome do Produtor 2"]            # Lista de produtores
}

# result = collection.insert_one(document)

def Menu():
    os.system('cls')
    print("-------- Menu --------")
    print("1 - Adicionar Musica")
    print("2 - Buscar Musica")
    print("3 - Listar Musica")
    print("4 - Deletar Musica")
    print("0 - Sair")
    op = input("Selecione uma opção:")
    
    if op == "0" : return
    elif op == "1" : return AddMusica()
    elif op == "2" : return BuscarMusica()
    elif op == "3" : return ListarMusicas()
    elif op == "4" : return DeleteMusica()
    else : return Menu()
    

def ListarMusicas():
    os.system('cls')
    print("-------- Lista de Músicas --------")
    
    musicas = collection.find()
    
    if collection.count_documents({}) == 0:
        print("Nenhuma música encontrada.")
        return Menu()

    for musica in musicas:
        print(f"Título: {musica.get('titulo', 'N/A')}")
        print(f"Cantor: {musica.get('cantor', 'N/A')}")
        print(f"Duração: {musica.get('duração', 'N/A')}")
        print(f"Ano: {musica.get('ano', 'N/A')}")
        print(f"Compositores: {(musica.get('compositor', []))}")
        print(f"Gêneros: {', '.join(musica.get('genero', []))}")
        print(f"Letra: {musica.get('letra', 'N/A')}")
        print(f"Gravadora: {musica.get('gravadora', 'N/A')}")
        print(f"Álbum: {musica.get('album', 'N/A')}")
        print(f"Produção: {musica.get('produção', [])}")
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
