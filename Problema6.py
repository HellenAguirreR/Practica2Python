def fibonacci_hasta_limite(limite):
    # Los primeros dos términos de la serie de Fibonacci
    a, b = 0, 1

    # Almacenar la serie de Fibonacci
    serie_fibonacci = []

    # Generar la serie de Fibonacci hasta alcanzar o superar el límite
    while a <= limite:
        # Agregar el término actual a la lista
        serie_fibonacci.append(a)
        
        # Calcular el siguiente término de la serie
        a, b = b, a + b

    return serie_fibonacci

# Serie de Fibonacci hasta 50
serie_resultante = fibonacci_hasta_limite(50)

print("Serie de Fibonacci hasta 50:", serie_resultante)
