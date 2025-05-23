import sys

# Datos de ejemplo con meses y valores asociados
datos = {
    "Enero": 25000, "Febrero": 32000, "Marzo": 18000, "Abril": 29000,
    "Mayo": 81000, "Junio": 37000, "Julio": 22000, "Agosto": 41200,
    "Septiembre": 39000, "Octubre": 28000, "Noviembre": 91000, "Diciembre": 30000
}

def filtrar_meses(umbral):
    return {mes: valor for mes, valor in datos.items() if valor > umbral}


if len(sys.argv) != 2:
    print("Usar: python mayor_a.py")
else:
    try:
        umbral = int(sys.argv[1])
        resultado = filtrar_meses(umbral)
        print(resultado)
    except ValueError:
            print("Por favor, ingrese un número válido como umbral.")
