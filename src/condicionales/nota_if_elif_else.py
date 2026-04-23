# Se crea una variable llamada 'nota' y se le asigna el valor 87
nota = 87

# Se verifica si la nota es mayor o igual a 90
if nota >= 90:
    # Si se cumple, se muestra la calificación más alta
    print("Calificación: Sobresaliente")

# Si no es sobresaliente, se verifica si es mayor o igual a 80
elif nota >= 80:
    # Si se cumple, se muestra la calificación correspondiente
    print("Calificación: Notable")

# Si no es notable, se verifica si es mayor o igual a 70
elif nota >= 70:
    # Si se cumple, se muestra la calificación de aprobado
    print("Calificación: Aprobado")

# Si no cumple ninguna de las condiciones anteriores
else:
    # Se muestra que la calificación es suspenso
    print("Calificación: Suspenso")