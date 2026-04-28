# Se crea una lista de nombres
nombres = ["Ana", "Carlos", "Elena"]

# Se recorre la lista usando índices con range(len(...))
# len(nombres) devuelve la cantidad de elementos de la lista (3)
for i in range(len(nombres)):
    # 'i' representa la posición (índice) de cada elemento
    # nombres[i] accede al elemento en esa posición
    print(f"Posición {i}: {nombres[i]}")