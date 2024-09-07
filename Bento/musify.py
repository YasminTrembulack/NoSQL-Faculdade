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
    "titulo": "",
    "cantor": "",
    "duração": "",
    "ano": 00,
    "compositor": ["Adam Levine", "Benny Blanco"],
    "genero": ["Pop", "Rock", "Dance"],
    "letra": "I'm at a payphone, trying to call home All of my change I spent on you...",
    "gravadora": "Interscope Records",
    "album": "Overexposed",
    "produção": ["Benny Blanco","Shellback"]
}

# result = collection.insert_one(document)

def Menu():
    os.system('cls')
    print("-------- Menu --------")
    print("1 - Adicionar Musica")
    print("2 - Buscar Musica")
    print("3 - Deletar Musica")
    print("0 - Sair")
    op = input("Selecione uma opção:")
    
    if op == "0" : return
    elif op == "1" : return AddMusica()
    elif op == "2" : return BuscarMusica()
    elif op == "3" : return DeleteMusica()
    else : return Menu()
    
    
    
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

    
    
        
def DeleteMusica():
    pass

os.system('cls')
print("Bem vindo ao Musify!")
time.sleep(2)
Menu()

db.close()