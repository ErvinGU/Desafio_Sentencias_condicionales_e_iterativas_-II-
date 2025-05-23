from string import ascii_lowercase
import itertools

def fuerza_bruta(objetivo):
    abecedario = ascii_lowercase 

    intentos = 0

    for longitud in range(1, len(objetivo) + 1):
        for combinacion in itertools.product(abecedario, repeat=longitud):
            primer_intento = "".join(combinacion)
            intentos += 1

            if primer_intento == objetivo:
                print(f"Contraseña encontrada: {objetivo} en {intentos} intentos")
                return None
    
        print("No se encontró la contraseña")

if __name__ == "__main__":
    clave = input("Ingresa la contraseña a descifrar (solo letras minúsculas): ").strip().lower()
    fuerza_bruta(clave)


