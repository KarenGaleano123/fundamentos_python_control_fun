# Se evalúan varias condiciones usando 'and'
# Todas deben ser verdaderas para ejecutar la operación

if usuario_esta_autenticado and tiene_permiso_avanzado and realizar_operacion_cara():
    # Este bloque solo se ejecuta si:
    # 1. El usuario está autenticado
    # 2. Tiene permisos avanzados
    # 3. La función 'realizar_operacion_cara()' devuelve True
    # (y además se ejecuta esa función)
    
    # Ejecutar operación
    print("Operación ejecutada.")