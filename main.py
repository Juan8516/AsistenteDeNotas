from usuarios import acciones 

# Programa principal: permite al usuario registrarse o iniciar sesión.

"""
Función principal del programa.
Muestra un menú con las opciones disponibles (registro y login)
y ejecuta la acción seleccionada por el usuario.
"""

#Mostrar opciones al usuario
print("""
      - registro
      - login
      """)

hazEl = acciones.Acciones() #Instancia de la clase Acciones
accion = input("\nQue quieres hacer ?: ").strip().lower() #Solicitar opcion al usuario

if accion == "registro":
    hazEl.registro()

    
elif accion == "login":
    hazEl.login()