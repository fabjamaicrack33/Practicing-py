import pymongo

# Conéctate a tu instancia de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Reemplaza con tu URI de conexión si es necesario

# Selecciona la base de datos que deseas mostrar
database_name = "colegio"
db = client[database_name]

# Lista todas las colecciones en la base de datos
colecciones = db.list_collection_names()

# Recorre las colecciones y muestra los documentos
for coleccion in colecciones:
    print(f"=== Colección: {coleccion} ===")
    # Encuentra todos los documentos en la colección
    documentos = db[coleccion].find()
    for documento in documentos:
        print(documento)

# Cierra la conexión
client.close()
