# Se crea un diccionario llamado 'usuario' con varias claves y valores
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Se recorre el diccionario
# Por defecto, al iterar un diccionario se recorren sus claves
for clave in usuario:
    # 'clave' representa cada llave del diccionario
    # usuario[clave] permite acceder al valor asociado a esa clave
    print(f"Clave: {clave}, Valor: {usuario[clave]}")