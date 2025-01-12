import usuarios.usuario as modelo

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
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]} estas registrado desde {login[5]}")
                
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Usuario y/o contraseña incorrecta intentalo de nuevo !!!!")        
        