import pymongo
import dns
from datetime import date
import time



class Database:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://maria:MariOli2005@sandbox.sn9l7.mongodb.net/IoT?retryWrites=true&w=majority")
        self.database = self.client.IoT
    
    def all(self):
        print(self.client.list_database_names())
        
    def insert(self, col, dic):
        col = self.database[col]
        col.insert_one(dic)
        
    def select(self, col):
        col = self.database[col]
        for dato in col.find():
            print(dato)
    
    def delete(self, col, dic):
        col = self.database[col]
        col.delete_one(dic)




# ASI FUNCIONA PARA SACAR LA FECHA ACTUAL
# today = date.today()
# time = time.strftime("%H:%M:%S")
# fecha = str(today) + ' ' + str(time)
# print(fecha)


# EJEMPLO DE INSERTAR EN TABLA SENSORES_TIPOS
# db = Database()
# coleccion = "sensores_tipos"
# diccionario = {"tipo":"pir"}
# db.insert(coleccion, diccionario )
# db.select(coleccion)


# EJEMPLO DE INSERTAR EN TABLA SENSORES_REGISTRADOS
# coleccion = "sensores_registrados"
# diccionario = {"nombre":"pir_sala", "tipo_id":1}
# db.insert(coleccion, diccionario )
# db.select(coleccion)


# EJEMPLO DE INSERTAR EN TABLA HISTORIAL
# coleccion = "historial"
# diccionario = {"sensor_id": 1, "valor_bool":1, "fecha_tiempo":fecha}
# db.insert(coleccion, diccionario )
# db.select(coleccion)



# EJEMPLO DE ELIMINAR
# coleccion = "historial"
# diccionario = {"sensor_id":1}
# db.delete(coleccion, diccionario)
# db.select(coleccion)  

