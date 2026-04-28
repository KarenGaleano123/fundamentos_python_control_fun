# Se crean dos listas:
# 'temperaturas' contiene las temperaturas de cada día
# 'dias' contiene los nombres de los días de la semana
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# ----------------------------------------
# Encontrar el día más caluroso
# ----------------------------------------

# Se obtiene la temperatura máxima de la lista
max_temp = max(temperaturas)

# Se busca el índice (posición) de esa temperatura máxima
indice_max = temperaturas.index(max_temp)

# Se usa ese índice para obtener el día correspondiente
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")


# ----------------------------------------
# Calcular la temperatura promedio
# ----------------------------------------

# Se suman todas las temperaturas y se dividen entre la cantidad de días
promedio = sum(temperaturas) / len(temperaturas)

# Se imprime el promedio con 1 decimal
print(f"Temperatura promedio: {promedio:.1f}°C")


# ----------------------------------------
# Días con temperatura superior al promedio
# ----------------------------------------

# Se recorre la lista usando índices
for i in range(len(dias)):
    # Se verifica si la temperatura de ese día es mayor al promedio
    if temperaturas[i] > promedio:
        # Se imprime el día y su temperatura
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")