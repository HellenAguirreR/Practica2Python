def factorial(n):
    # Verificar si el número es no negativo
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."
    
    if n == 0:
        return 1

    # Calcular el factorial usando un bucle
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

numero_ingresado = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

resultado_factorial = factorial(numero_ingresado)

print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")
