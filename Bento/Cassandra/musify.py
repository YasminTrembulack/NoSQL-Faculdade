# https://docs.datastax.com/en/astra-api-docs/_attachments/python-client/astrapy/client.html


from astrapy import DataAPIClient

# Inicializar o cliente com seu token de aplicação
client = DataAPIClient("AstraCS:ZwCdaeZNkaWHywLvkZbAvAEI:f381fa048e4c40aff8903031163454ba4437a70b751ab531bd9b8a249912f0b8")

# Conectar ao banco de dados usando o endpoint fornecido
db = client.get_database_by_api_endpoint(
  "https://8c44f30f-9729-42fa-9f71-302c0a6c7cd4-us-east1.apps.astra.datastax.com"
)

# Verificar a conexão e listar as coleções/tabelas
print(f"Conectado ao Astra DB: {db.list_collection_names()}")

# Criar uma tabela de músicas (coleção)
collection = db.create_collection("musicas")
print("Tabela 'musicas' criada com sucesso!")


# Inserir uma nova música
musica = {
    "id": "1",  # Use um identificador único
    "nome": "Bohemian Rhapsody",
    "artista": "Queen",
    "genero": "Rock"
}

collection.insert_one(musica)
print("Música inserida com sucesso!")

# Consultar todas as músicas
for musica in collection.find():
    print(musica)
    
# Atualizar o gênero da música
collection.update_one(
    {"id": "1"},  # Filtro pelo ID da música
    {"$set": {"genero": "Opera Rock"}}
)
print("Música atualizada com sucesso!")

# Deletar uma música
collection.delete_one({"id": "1"})
print("Música deletada com sucesso!")