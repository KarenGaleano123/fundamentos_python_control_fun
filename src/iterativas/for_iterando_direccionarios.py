# Iterando sobre pares clave-valor
# 'items()' devuelve cada par (clave, valor) del diccionario
for clave, valor in usuario.items():
    # 'clave' contiene la llave
    # 'valor' contiene el dato asociado a esa llave
    print(f"{clave}: {valor}")

# Iterando solo sobre valores
# 'values()' devuelve únicamente los valores del diccionario
for valor in usuario.values():
    # Se imprime cada valor sin mostrar la clave
    print(valor)