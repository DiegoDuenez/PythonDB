import pymongo
import dns


client = pymongo.MongoClient("mongodb+srv://diego:192712883@cluster0.o7i7b.mongodb.net/IoT?retryWrites=true&w=majority")
database = client.IoT

class Database:
    
    def all(self):
        print(client.list_database_names())
        
    def insert(self, col, dic):
        col = database[col]
        col.insert_one(dic)
        
    def select(self, col):
        col = database[col]
        for dato in col.find():
            print(dato)
    
    def delete(self, col, dic):
        col = database[col]
        col.delete_one(dic)




# EJEMPLO DE INSERTAR
# db = Database()
# coleccion = "historial"
# diccionario = {"temperatura": 20, "distancia":30}
# db.insert(coleccion, diccionario)
# db.select(coleccion)


# EJEMPLO DE ELIMINAR
# db = Database()
# coleccion = "historial"
# diccionario = {"temperatura": 20, "distancia":30}
# db.delete(coleccion, diccionario)
# db.select(coleccion)


