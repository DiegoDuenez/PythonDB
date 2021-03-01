import mysql.connector as mysql


mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="IoT"
    )
print(mydb)


mycursor = mydb.cursor()


class Database:

    def all(self):
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    
    def insert(self, tabla, valores):
        t = valores.get('temperatura')
        h = valores.get('humedad')
        p = valores.get('pir')
        d = valores.get('distancia')
        mycursor.execute('INSERT INTO %s (temperatura, humedad, pir, distancia) values ("%s", "%s", "%s", "%s")' % (tabla, t, h, p, d))
        mydb.commit()   
        
    def select(self, tabla):
        mycursor.execute('SELECT * FROM %s' % (tabla))
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        
    def delete(self, tabla, valores):
        for clave, x in valores.items():  
            columna = clave
        valor = valores.get(col)
        mycursor.execute('DELETE FROM %s where %s = "%s"' % (tabla, columna , valor))
        mydb.commit()     
        


# EJEMPLO DE INSERTAR
# db = Database()
# tabla = "historial"
# valores = {"temperatura": 20, "distancia":30}
# db.insert(tabla, valores )
# db.select(tabla)


# EJEMPLO DE ELIMINAR
# db = Database()
# tabla = "historial"
# valores = {"temperatura":20}
# db.delete(tabla, valores)
# db.select(tabla)  
