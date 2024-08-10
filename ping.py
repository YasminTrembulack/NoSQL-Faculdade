#Importando bibliotecas
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

# Escape do nome do usuário e da senha
username = quote_plus('yasminagostinho012')
password = quote_plus('N9357iG1m8ifKn5K')

# URL de conexão
uri = f'mongodb+srv://{username}:{password}@clusterfaculdade.glgbt.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFaculdade'

# Criar cliente de conexão ao servidor
client = MongoClient(uri, server_api = ServerApi('1'))

#Enviar uma solicitção e confirmar a conexão
try:
    client.admin.command('ping')
    print('Sucesso ao implementar o banco!')
except Exception as e:
    print(f'ERRO: {e}')

