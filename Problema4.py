lista_alumnos = []

# Cantidad de alumnos
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Ingresar datos de cada alumno
for i in range(1, num_alumnos + 1):
    # Solicitar el nombre del alumno
    nombre_alumno = input(f"Ingrese el nombre del alumno {i}: ")

    # Solicitar las calificaciones del alumno
    calificaciones = []
    for j in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {j} del alumno {i}: "))
                calificaciones.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese una calificación válida.")

    # Crear un diccionario con la información del alumno
    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}

    # Agregar el diccionario a la lista de alumnos
    lista_alumnos.append(alumno)

# Listado completo de los alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
