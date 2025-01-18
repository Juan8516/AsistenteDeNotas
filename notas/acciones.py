import notas.nota as modelo

class Acciones:
    """
    Clase Acciones:
    Define las operaciones que los usuarios pueden realizar con sus notas:
    - Crear una nueva nota.
    - Mostrar todas las notas de un usuario.
    - Eliminar una nota específica.
    """
    
    def crear(self, usuario):  
        """
        Permite crear una nueva nota para un usuario.

        Args:
            usuario (tuple): Tupla que contiene la información del usuario. 
                Ejemplo: (id, nombre, email, ...).

        Solicita al usuario ingresar un título y descripción para la nota.
        Guarda la nota en la base de datos utilizando el método `guardar` del modelo `Nota`.

        Prints:
            Mensaje indicando si la nota fue guardada correctamente o no.
        """
        print(f"\nOk {usuario[1]}!! vamos a crear una nueva nota ... ")
        
        #Solicitar informacion de la nota
        titulo = input("Ingresa titulo para esta nota: ")
        descripcion = input("Ingresa el contenido: ")
        
        #Crear y guardar nota
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        #Confirmar el resultado
        if guardar[0] >= 1:
            print(f"Se ha guardado la nota {nota.titulo} correctamente !!!")
        else:
            print(f"{usuario[1]} no se ha guardado la nota")
            
    def mostrar(self, usuario):
        """
        Muestra todas las notas creadas por un usuario.

        Args:
            usuario (tuple): Tupla con la información del usuario. 
                Ejemplo: (id, nombre, email, ...).

        Recupera y lista las notas utilizando el método `listar` del modelo `Nota`.

        Prints:
            Lista de notas del usuario, mostrando el título y contenido de cada una.
        """
        print(f"\nHola {usuario[1]} estas son tus notas: ")
        
        #Recuperar notas del usuario
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        #Mostrar cada nota
        for nota in notas:
            print("\n-----------------------")
            print(nota[2])
            print(nota[3])
    
    def borrar(self, usuario):
        """
        Elimina una nota del usuario proporcionado.

        Args:
            usuario (tuple): Información del usuario (id, nombre, ...).

        Solicita al usuario el título de la nota a eliminar,
        intenta borrarla de la base de datos y confirma si el proceso fue exitoso.
        """
        print(f"Hola {usuario[1]} vamos a eliminar notas")
        
        #Solicitar el titulo de la nota a eliminar
        titulo = input("Ingresa titulo de la nota a eliminar: ")
        
        #Eliminar la nota
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar(titulo)
        
        #Confirmar el resultado
        if eliminar[0] >= 1:
            print(f"Se ha eliminado la nota {nota.titulo}")
        else:
            print("No se ha eliminado la nota comprueba el titulo a eliminar")