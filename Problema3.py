numeros_ingresados = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta == "SI":
        try:
            # Solicitar al usuario que ingrese un número y agregarlo a la lista
            numero = int(input("Ingrese el número: "))
            numeros_ingresados.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif respuesta == "NO":
        
        break
    else:
        print("Por favor, ingrese una respuesta válida (SI/NO).")


print("Números ingresados:", numeros_ingresados)

# Cantidad de números pares e impares
numeros_pares = sum(1 for num in numeros_ingresados if num % 2 == 0)
numeros_impares = len(numeros_ingresados) - numeros_pares

print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
