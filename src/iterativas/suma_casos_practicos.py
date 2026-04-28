# Se define la cantidad de números a sumar
n = 10

# Se inicializa la variable 'suma' en 0
suma = 0

# Se recorre desde 1 hasta n (incluyéndolo)
# range(1, n+1) genera: 1, 2, 3, ..., n
for i in range(1, n+1):
    # En cada iteración se va acumulando el valor de 'i'
    suma += i  # Equivale a: suma = suma + i

# Se imprime el resultado final
print(f"La suma de los primeros {n} números es: {suma}")  # 55