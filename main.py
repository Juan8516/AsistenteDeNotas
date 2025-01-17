from usuarios import acciones 

#Preguntas del asistente
print("""
      - registro
      - login
      """)

hazEl = acciones.Acciones()
accion = input("\nQue quieres hacer ?: ")

if accion == "registro":
    hazEl.registro()

    
elif accion == "login":
    hazEl.login()