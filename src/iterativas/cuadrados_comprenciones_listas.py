# Crear una lista con los cuadrados de los números del 1 al 5
# range(1, 6) genera los números: 1, 2, 3, 4, 5
# x**2 calcula el cuadrado de cada número
cuadrados = [x**2 for x in range(1, 6)]

# Se imprime la lista resultante
print(cuadrados)  # [1, 4, 9, 16, 25]


# Filtrar elementos usando una condición
# range(10) genera los números del 0 al 9
# x % 2 == 0 selecciona solo los números pares
pares = [x for x in range(10) if x % 2 == 0]

# Se imprime la lista de números pares
print(pares)  # [0, 2, 4, 6, 8]