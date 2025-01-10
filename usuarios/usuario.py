import mysql.connector
import datetime
import hashlib

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basedatos_asistente",
    port=3306
) 

cursor = dataBase.cursor(buffered=True)

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre    = nombre
        self.apellidos = apellidos
        self.email     = email
        self.password  = password
        
    def registrar(self):
        fecha = datetime.datetime.now()
        
        #Cifrado de contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        sql = ("INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)")
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario)
            dataBase.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
        
        return [cursor.rowcount, self]
    
    def identificar(self):
        return self.nombre