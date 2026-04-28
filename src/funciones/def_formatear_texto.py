# Función que permite formatear un texto de múltiples formas
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):

    # ---------------------------------------
    # 1. Convertir a mayúsculas si se solicita
    # ---------------------------------------
    if mayusculas:
        texto = texto.upper()

    # ---------------------------------------
    # 2. Dividir el texto en palabras
    # ---------------------------------------
    palabras = texto.split()

    # ---------------------------------------
    # 3. Aplicar prefijo y sufijo a cada palabra
    # ---------------------------------------
    palabras_formateadas = [
        f"{prefijo}{palabra}{sufijo}"
        for palabra in palabras
    ]

    # ---------------------------------------
    # 4. Unir las palabras con el separador elegido
    # ---------------------------------------
    resultado = separador.join(palabras_formateadas)

    # Se retorna el texto final formateado
    return resultado