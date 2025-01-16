import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! vamos a crear una nueva nota ... ")
        
        titulo = input("Ingresa titulo para esta nota: ")
        descripcion = input("Ingresa el contenido: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f"Se ha guardado la nota {nota.titulo} correctamente !!!")
        else:
            print(f"{usuario[1]} no se ha guardado la nota")
            
    def mostrar(self, usuario):
        print(f"\nHola {usuario[1]} estas son tus notas: ")
        
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n-----------------------")
            print(nota[2])
            print(nota[3])