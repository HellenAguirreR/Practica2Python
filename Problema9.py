def omitir_vocales(cadena):
    # Cadena nueva sin las vocales
    resultado = ''.join(caracter for caracter in cadena if caracter.lower() not in 'aeiouAEIOU')
    return resultado

# Solicitar una cadena de texto
texto_ingresado = input("Ingrese una cadena de texto: ")

resultado_final = omitir_vocales(texto_ingresado)

print("Resultado con vocales omitidas:", resultado_final)
