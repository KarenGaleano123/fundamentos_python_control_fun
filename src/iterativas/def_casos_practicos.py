# Función que verifica si un número es primo
def es_primo(num):
    # Si el número es menor que 2, no es primo
    if num < 2:
        return False
    
    # Se recorre desde 2 hasta la raíz cuadrada del número
    # Esto optimiza el proceso de verificación
    for i in range(2, int(num**0.5) + 1):
        # Si el número es divisible por i, no es primo
        if num % i == 0:
            return False
    
    # Si no se encontraron divisores, es primo
    return True


# Se crea una lista vacía para almacenar los números primos
primos = []

# Se recorren los números del 2 al 19
for num in range(2, 20):
    # Se verifica si el número es primo usando la función
    if es_primo(num):
        # Si es primo, se agrega a la lista
        primos.append(num)

# Se imprime la lista de números primos encontrados
print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]