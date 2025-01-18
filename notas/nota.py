import usuarios.conexion as conexion

#Conexion a base de datos
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota():
    """
    Clase para gestionar notas de los usuarios.

    Attributes:
        usuario_id (int): ID del usuario propietario de las notas.
        titulo (str): Título de la nota. (opcional)
        descripcion (str): Contenido de la nota. (opcional)
    """
    
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        """
        Inicializa una nueva instancia de la clase Nota.

        Args:
            usuario_id (int): ID del usuario propietario de la nota.
            titulo (str, opcional): Título de la nota. Por defecto es una cadena vacía.
            descripcion (str, opcional): Contenido de la nota. Por defecto es una cadena vacía.
        """
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
    
    def guardar(self):
        """
        Guarda la nota actual en la base de datos.

        Returns:
            tuple: Una tupla con el número de filas afectadas (int) y la instancia actual de la clase Nota.
        """
        
        #Consulta SQL para insertar una nueva nota
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        #Ejecutar consulta
        cursor.execute(sql, nota)
        database.commit()
        
        #Retornar el resultado
        return(cursor.rowcount, self)
    
    def listar(self):
        """
        Lista todas las notas del usuario actual.

        Returns:
            list: Una lista de tuplas donde cada tupla representa una nota.
        """
        # Consulta SQL para seleccionar todas las notas del usuario
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        
        #Ejecutar la consola
        cursor.execute(sql)
        result = cursor.fetchall()
        
        #Retornar los resultados
        return result
    
    def eliminar(self, usuario):
        """
        Elimina una nota específica del usuario actual basándose en el título.

        Returns:
            list: Una lista con el número de filas afectadas (int) y la instancia actual de la clase Nota.
        """
        # Consulta SQL para eliminar una nota específica del usuario
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"
        
        #Ejecutar la consulta
        cursor.execute(sql)
        database.commit()
        
        #Retornar el resultado
        return [cursor.rowcount, self]