import mysql.connector

def conectar():
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="basedatos_asistente",
        port=3306
    ) 
    cursor = dataBase.cursor(buffered=True)
    
    return [dataBase, cursor]