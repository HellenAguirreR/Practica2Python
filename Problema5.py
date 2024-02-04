def contar_digitos_en_numero(numero, digito):
    # 
    numero_str = str(numero)

    # Contar la cantidad de veces que aparece el dígito en el número
    cantidad = numero_str.count(str(digito))

    return cantidad

# Ejemplo de uso
numero_ingresado = 15789000
digito_a_contar = 0

cantidad_resultante = contar_digitos_en_numero(numero_ingresado, digito_a_contar)

print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_a_contar}")
print(f"Cantidad de veces {digito_a_contar} en el número: {cantidad_resultante}")
