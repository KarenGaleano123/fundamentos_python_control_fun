# Se solicita al usuario que introduzca el nombre de una fruta
fruta = input("Introduzca una fruta: ")

# Se utiliza la estructura 'match' para evaluar el valor ingresado
match fruta:
    # Caso 1: si la fruta es "manzana"
    case "manzana":
        # Se muestra el mensaje correspondiente
        print("La fruta es una manzana.")

    # Caso 2: si la fruta es "naranja"
    case "naranja":
        # Se muestra el mensaje correspondiente
        print("La fruta es una naranja.")

    # Caso 3: si la fruta es "plátano"
    case "plátano":
        # Se muestra el mensaje correspondiente
        print("La fruta es un plátano.")

    # Caso por defecto: si no coincide con ninguno de los anteriores
    case _:
        # Se muestra un mensaje indicando que no se reconoce la fruta
        print("Fruta desconocida.")