# Se crean dos variables: 'dividendo' y 'divisor'
dividendo = 10
divisor = 0

# Se utiliza un operador ternario para evitar un error de división por cero
# Si el divisor es diferente de 0 → realiza la división
# Si el divisor es 0 → devuelve un mensaje de advertencia
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"

# Se imprime el resultado
print(resultado)