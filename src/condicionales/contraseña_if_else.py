# Se solicita al usuario que ingrese una contraseña
contrasena = input("Introduce la contraseña: ")

# Se verifica si la contraseña ingresada es igual a "secreta123"
if contrasena == "secreta123":
    # Si la condición se cumple, se muestra mensaje de acceso permitido
    print("Acceso concedido.")
else:
    # Si la condición no se cumple, se muestra mensaje de error
    print("Contraseña incorrecta. Acceso denegado.")