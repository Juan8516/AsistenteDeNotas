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
        
        try:
            email     = input("Ingresa tu email: ")
            password  = input("Ingresa tu contraseña: ")
            
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            
            if login:
                if email == login[3]:
                    print(f"\nBienvenido {login[1]} estas registrado desde {login[5]}")
                    self.proximasAcciones(login)
                
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Usuario y/o contraseña incorrecta intentalo de nuevo !!!!")        
    
    def proximasAcciones(self, usuario):
        print("Que accion quieres realizar ?")
        
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
            print("vamos a crear nota")
            self.proximasAcciones()
        elif accion == "mostrar":
            print("vamos a ver tus notas")
            self.proximasAcciones()
        elif accion == "eliminar":
            print("selecciona una nota para eliminar")
            self.proximasAcciones()
        elif accion == 'salir':
            print(f"Hasta pronto {usuario[1]}")
            exit()