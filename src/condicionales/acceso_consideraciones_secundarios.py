# Se crean dos variables booleanas
acceso_registrado = True    # Indica que el acceso ya fue registrado
acceso_permitido = False    # Indica que no tiene permiso directo

# Se evalúa la condición usando el operador 'or'
# 'or' significa que al menos una de las condiciones debe ser verdadera
if acceso_permitido or acceso_registrado:
    # Si alguna de las dos condiciones es True, se ejecuta este bloque
    print("Acceso concedido.")