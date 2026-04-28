# Se crea una lista de nombres
nombres = ["Ana", "Carlos", "Elena"]

# Se recorre la lista usando 'enumerate()'
# 'enumerate()' devuelve pares (índice, valor) en cada iteración
for indice, nombre in enumerate(nombres):
    # 'indice' es la posición (0, 1, 2)
    # 'nombre' es el valor correspondiente en la lista
    print(f"Posición {indice}: {nombre}")