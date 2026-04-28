# Se crea una lista de números
numeros = [1, 2, 3, 4, 5]

# Se crea una nueva lista llamada 'paridad' usando una comprensión de listas
# Para cada número 'n' en la lista 'numeros':
# - Si n % 2 == 0 → se agrega "par"
# - Si no → se agrega "impar"
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]

# Se imprime la lista resultante
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']