import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

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
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            print(f"Error al registrar el usuario: {e}")
            result = [0, self]
        return result
        
    def identificar(self):
        
        #Consultar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #Cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        #Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result