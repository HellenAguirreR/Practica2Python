def obtener_mes_numero(mes):
    
    meses_dict = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }
    
    return meses_dict.get(mes, None)

def formatear_fecha(fecha):
    # Dividir la fecha en (mes, día, año)
    partes = fecha.split()

    # Verificar si la fecha es en formato mes-día-año
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
    # Verificar si la fecha es en formato "Mes dia, año"
    elif len(partes) == 3:
        mes, dia, anio = partes[0], partes[1].strip(','), partes[2]
    else:
        return "Formato de fecha no válido."

    # Obtener el número del mes
    mes_numero = obtener_mes_numero(mes)

    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{anio}-{mes_numero:02d}-{dia:02d}"

    return fecha_formateada

fecha_ingresada = input("Ingrese una fecha (en formato mes-día-año o 'Mes dia, año'): ")

fecha_formateada = formatear_fecha(fecha_ingresada)

print("Fecha formateada en AAAA-MM-DD:", fecha_formateada)

