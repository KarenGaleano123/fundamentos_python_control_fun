# Se crea una variable llamada 'edad' y se le asigna el valor 45
edad = 45

# Se verifica si la edad es menor a 18
if edad < 18:
    # Si se cumple, se muestra este mensaje
    print("Eres menor de edad.")

# Si no es menor de edad, se verifica si está entre 18 y 64 años
elif 18 <= edad < 65:
    # Si se cumple, se considera adulto
    print("Eres adulto.")

# Si no cumple ninguna de las condiciones anteriores
else:
    # Significa que tiene 65 años o más
    print("Eres mayor de 65 años.")