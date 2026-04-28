# Se evalúa si el acceso está permitido directamente
if acceso_permitido:
    # Si es True, se concede el acceso
    print("Acceso concedido.")
else:
    # Si no tiene acceso permitido, se verifica si está registrado
    if acceso_registrado:
        # Si está registrado, también se concede el acceso
        print("Acceso concedido.")