import mysql.connector

dataBase = mysql.connector.cursor(
    host="localhost",
    user="root",
    passw="",
    database="basedatos_asistente",
    port=127.0
) 

cursor = database.cursor(buffered=True)

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre    = nombre
        self.apellidos = apellidos
        self.email     = email
        self.password  = password
        
    def registrar(self):
        return self.nombre
 
    def identificar(self):
        return self.nombre