import pymongo

# Reemplaza 'tu_cluster', 'tu_contraseña', y 'tu_base_de_datos' con tu información de MongoDB Atlas
cluster_uri = "mongodb+srv://proyecto_Colegio:12345@cluster0.vq2o9ro.mongodb.net/"

# Conéctate a MongoDB Atlas
client = pymongo.MongoClient(cluster_uri)

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
