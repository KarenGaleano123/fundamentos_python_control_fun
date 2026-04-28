# Crear una matriz de multiplicación 3x3 usando bucles anidados

# Bucle externo: recorre las filas (valores de i del 1 al 3)
for i in range(1, 4):
    
    # Bucle interno: recorre las columnas (valores de j del 1 al 3)
    for j in range(1, 4):
        # Se imprime la multiplicación en formato tabla
        # end="\t" agrega un espacio tipo tabulación en la misma línea
        print(f"{i} × {j} = {i*j}", end="\t")
    
    # Salto de línea después de terminar cada fila
    print()