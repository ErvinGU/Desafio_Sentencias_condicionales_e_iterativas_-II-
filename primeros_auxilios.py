
def primeros_auxilios():
    print("Bienvenidos a la sala de Urgencias")
    situacion = input("Paciente desmayado, ¿responde a estímulos? (si/no): ").lower()

    if situacion == "si":
        print("Ver la opción de llevar al paciente al hospital más cercano")

    else:
        print("Abrir vía aérea")
        respiracion = input("¿la persona puede respirar? (si/no): ").lower()

        if respiracion == "si":
            print("Permitirle posición de suficiente respiración")
        else:
            print("Administrar 5 ventilaciones y llamar ambulancia")
            signos_vitales = input("¿La persona tiene signos de vida? (si/no): ").lower

        if signos_vitales == "si":
            print("Reevaluar a la espera de ambulacia")

        else:
            print("Administrar compresiones teráxicas hasta que llegue la ambulancia")

    print("Fin del procedimiento")
            
if __name__ == "__main__":
    primeros_auxilios()


