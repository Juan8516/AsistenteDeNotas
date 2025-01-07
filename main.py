#Preguntas del asistente
print("""
      - registro
      - login
      """)

accion = input("Que quieres hacer ?: ")

if accion == "registro":
    print("\nOk, vamos a registrarte !!")
    nombre    = input("Ingresa tu nombre: ")
    apellidos = input("Ingresa tus apellidos: ")
    email     = input("Ingresa tu email: ")
    password  = input("Ingresa tu contraseña: ")
    
elif accion == "login":
    print("Ingresa usuario y contraseña: ")
    email     = input("Ingresa tu email: ")
    password  = input("Ingresa tu contraseña: ")