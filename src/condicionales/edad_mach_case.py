# Se crea una variable llamada 'edad' y se le asigna el valor 20
edad = 20

# Se utiliza la estructura 'match' para evaluar diferentes casos según la edad
match edad:
    # Caso 1: si la edad es menor a 18
    case edad if edad < 18:
        # Se muestra el mensaje correspondiente
        print("Eres menor de edad.")

    # Caso 2: si la edad está entre 18 y 64
    case edad if edad >= 18 and edad < 65:
        # Se muestra el mensaje correspondiente
        print("Eres adulto.")

    # Caso 3: si la edad es 65 o más
    case edad if edad >= 65:
        # Se muestra el mensaje correspondiente
        print("Eres adulto mayor.")