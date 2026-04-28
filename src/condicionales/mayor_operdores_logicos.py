# Se asume que las variables 'a', 'b' y 'c' ya tienen valores asignados

# Se inicializa la variable 'mayor' con el valor de 'a'
mayor = a

# Se compara si 'b' es mayor que el valor actual de 'mayor'
if b > mayor:
    # Si se cumple, 'mayor' toma el valor de 'b'
    mayor = b

# Se compara si 'c' es mayor que el valor actual de 'mayor'
if c > mayor:
    # Si se cumple, 'mayor' toma el valor de 'c'
    mayor = c

# Se imprime el resultado final
print(f'El número mayor es {mayor}.')