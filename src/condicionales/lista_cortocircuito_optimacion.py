# Se crea una lista vacía
lista = []

# Se evalúan dos condiciones:
# 1. 'lista' → verifica si la lista NO está vacía (True si tiene elementos)
# 2. 'lista[0] == "Python"' → verifica si el primer elemento es "Python"
# Gracias al operador 'and', la segunda condición solo se evalúa si la lista tiene elementos
if lista and lista[0] == 'Python':
    # Si ambas condiciones se cumplen, se muestra el mensaje
    print("El primer elemento es 'Python'.")