import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def registro(self):
        print("\nOk, vamos a registrarte !!")
        
        nombre    = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email     = input("Ingresa tu email: ")
        password  = input("Ingresa tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nRegistro para {registro[1].nombre} se ha realizado correctamente con el email {registro[1].email}!!!!")
        else:
            print("No se ha registrado correctamente !!!")
    
    def login(self):
        print("\nIngresa usuario y contraseña: ")
        
        email = input("Ingresa tu email: ")
        password  = input("Ingresa tu contraseña: ")
        
        usuario = modelo.Usuario('', '', email, password)
        login = usuario.identificar()
        
        if login:
            if email == login[3]:
                print(f"\nBienvenido {login[1]} estas registrado desde {login[5]}")
                self.proximasAcciones(login)  
    
    def proximasAcciones(self, usuario):
        print("\nQue accion quieres realizar ?")
        
        print("""\n
            Acciones disponibles:
            - Crear una nota (crear)
            - Mostrar una nota (mostrar)
            - Eliminar una nota (eliminar)
            - Salir (salir)
              """)
        
        accion = input("Que quieres hacer ? : ")
        hazEl = notas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == 'salir':
            print(f"Hasta pronto {usuario[1]}")
            exit()