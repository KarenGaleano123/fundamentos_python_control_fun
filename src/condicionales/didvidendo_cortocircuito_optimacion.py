# Se crean dos variables: 'dividendo' y 'divisor'
dividendo = 10
divisor = 0

# Se evalúan dos condiciones usando 'and':
# 1. divisor != 0 → verifica que no sea cero (evita error)
# 2. dividendo / divisor > 1 → verifica si el resultado es mayor que 1
# IMPORTANTE: la segunda condición solo se evalúa si la primera es verdadera
if divisor != 0 and dividendo / divisor > 1:
    # Si ambas condiciones se cumplen, se muestra este mensaje
    print("El resultado de la división es mayor que 1.")
else:
    # Si el divisor es 0 o no se cumple la condición, se muestra este mensaje
    print("No es posible dividir entre cero.")