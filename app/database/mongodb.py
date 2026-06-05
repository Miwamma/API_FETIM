from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["fetin_db"]

#conexão com o banco do mongo NÃO SE MEXE AQUI, SE PRECISAR MUDAR O NOME DO BANCO, MUDA AQUI E PRONTO, NÃO SE PREOCUPE COM O RESTO DO CÓDIGO, ELE VAI FUNCIONAR NORMALMENTE.
#Quando precisar criar algo como collection no banco usa o ex de users collection_name["dsadsa"] no próprio repository do banco