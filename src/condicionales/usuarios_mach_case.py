# Se crea una lista de diccionarios llamada 'usuarios'
# Cada diccionario representa un usuario con su nombre y rol
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

# Se recorre la lista de usuarios usando un bucle for
for usuario in usuarios:
    # Se utiliza 'match' para evaluar el contenido del diccionario
    match usuario:
        # Caso 1: si el rol del usuario es "admin"
        case {"rol": "admin"}:
            # Se muestra un mensaje indicando permisos de administrador
            print(f"{usuario['nombre']} tiene permisos de administrador.")

        # Caso 2: si el rol es "moderador"
        case {"rol": "moderador"}:
            # Se muestra un mensaje indicando que puede moderar
            print(f"{usuario['nombre']} puede moderar contenidos.")

        # Caso 3: si el rol es "usuario"
        case {"rol": "usuario"}:
            # Se muestra un mensaje indicando que es un usuario normal
            print(f"{usuario['nombre']} es un usuario regular.")

        # Caso por defecto: si no coincide con ninguno de los anteriores
        case _:
            # Se muestra un mensaje indicando rol desconocido
            print(f"Rol de {usuario['nombre']} desconocido.")