# Se crea una lista de números
numeros = [0, 0, 1, 0]

# Se usa la función 'any()'
# any(numeros) devuelve True si al menos un elemento de la lista es verdadero (distinto de 0)
if any(numeros):
    # Si existe al menos un valor distinto de 0, se ejecuta este bloque
    print("Al menos un número es no cero.")