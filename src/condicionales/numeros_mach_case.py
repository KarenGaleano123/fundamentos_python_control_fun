# Se crea una lista llamada 'numeros' con varios elementos
numeros = [1, 2, 3, 4]

# Se utiliza la estructura 'match' para analizar la forma de la lista
match numeros:
    # Caso 1: si la lista está vacía
    case []:
        print("La lista está vacía.")

    # Caso 2: si la lista tiene un solo elemento
    case [uno]:
        # 'uno' captura ese único valor
        print(f"Un solo elemento: {uno}.")

    # Caso 3: si la lista tiene exactamente dos elementos
    case [uno, dos]:
        # 'uno' y 'dos' capturan los valores
        print(f"Dos elementos: {uno} y {dos}.")

    # Caso 4: si la lista tiene uno o más elementos
    case [uno, *resto]:
        # 'uno' toma el primer elemento
        # '*resto' captura el resto de la lista como otra lista
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")