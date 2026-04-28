# Se crea una lista de valores booleanos
condiciones = [True, True, False, True]

# Se usa la función 'all()'
# all(condiciones) devuelve True solo si TODOS los elementos son True
if all(condiciones):
    # Este bloque se ejecuta si todas las condiciones son verdaderas
    print("Todas las condiciones son verdaderas.")
else:
    # Este bloque se ejecuta si al menos una condición es falsa
    print("Al menos una condición es falsa.")