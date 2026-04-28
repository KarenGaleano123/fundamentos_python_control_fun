# Se evalúa una condición lógica combinando 'or' y 'and'
# 'and' tiene mayor prioridad que 'or', pero aquí también se usan paréntesis

# (acceso_registrado and True) → siempre será igual a 'acceso_registrado'
# porque cualquier valor AND True da el mismo valor

if acceso_permitido or (acceso_registrado and True):
    # Si alguna de las condiciones es verdadera, se ejecuta este bloque
    print("Acceso concedido.")