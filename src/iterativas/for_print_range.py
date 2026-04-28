# Números del 3 al 7
# range(3, 8) genera números desde 3 hasta 7 (el 8 no se incluye)
for i in range(3, 8):
    # Se imprime cada número en la misma línea separados por espacio
    print(i, end=" ")  # 3 4 5 6 7

# Se imprime un salto de línea
print()

# Números pares del 2 al 10
# range(2, 11, 2) empieza en 2, termina en 10 y avanza de 2 en 2
for i in range(2, 11, 2):
    # Se imprimen los números pares en la misma línea
    print(i, end=" ")  # 2 4 6 8 10

# Se imprime un salto de línea
print()

# Cuenta regresiva
# range(10, 0, -1) empieza en 10 y disminuye hasta 1
for i in range(10, 0, -1):
    # Se imprime la cuenta regresiva en la misma línea
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1