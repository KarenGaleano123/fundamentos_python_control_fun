# Se crean dos variables: 'saldo' (dinero disponible) y 'retiro' (dinero a retirar)
saldo = 300
retiro = 500

# Se verifica si el saldo es suficiente para realizar el retiro
if saldo >= retiro:
    # Si hay suficiente dinero, se descuenta el monto del retiro
    saldo -= retiro  # Equivale a: saldo = saldo - retiro

    # Se muestra un mensaje de éxito
    print("Retiro exitoso.")

    # Se muestra el nuevo saldo después del retiro
    print(f"Nuevo saldo: {saldo}")
else:
    # Si no hay suficiente dinero, se muestra un mensaje de error
    print("Fondos insuficientes.")

    # Se muestra el saldo actual sin cambios
    print(f"Saldo actual: {saldo}")