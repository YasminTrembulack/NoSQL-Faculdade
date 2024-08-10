from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = quote_plus('yasminagostinho012')
password = quote_plus('aaaaa')

uri = f'mongodb+srv://{username}:{password}@clusterfaculdade.glgbt.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFaculdade'

client = MongoClient(uri, server_api = ServerApi('1'))

# Criar o banco de dados
database_name = 'UniSenai'
db = client[database_name]

# Criando coleção(tabela)
collection_name = 'disciplinas'
collection = db[collection_name]

# Criando o documento(linha)
document = {
    "nome": "Banco de Dados",
    "codigo": "BD01",
    "descricao": "Disciplina de Banco de Dados",
    "professor": "Paulo Moreira",
    "horario": "Sexta-feira 19h-22h"
}

# Inserindo documento
collection.insert_one(document)

print(f"Banco de dados '{database_name}' e coleção '{collection_name}' criados com sucesso!")
