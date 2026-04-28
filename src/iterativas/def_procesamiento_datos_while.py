# Función que calcula el factorial de un número
def calcular_factorial(n):
    # Se inicializa la variable 'resultado' en 1
    # (el factorial siempre empieza multiplicando desde 1)
    resultado = 1

    # Se ejecuta el bucle mientras 'n' sea mayor que 0
    while n > 0:
        # Se multiplica el resultado por el valor actual de 'n'
        resultado *= n  # Equivale a: resultado = resultado * n

        # Se disminuye 'n' en 1 en cada iteración
        n -= 1

    # Se devuelve el resultado final
    return resultado


# Se define el número del cual se quiere calcular el factorial
numero = 5

# Se imprime el resultado usando la función
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120