import string
import random

def generar_contrasena():
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser mayor que cero.")
            return None

        caracteres = ""
        if input("¿Incluir caracteres en minúsculas? (s/n): ").lower() == "s":
            caracteres += string.ascii_lowercase
        if input("¿Incluir caracteres en mayúsculas? (s/n): ").lower() == "s":
            caracteres += string.ascii_uppercase
        if input("¿Incluir números? (s/n): ").lower() == "s":
            caracteres += string.digits
        if input("¿Incluir caracteres especiales? (s/n): ").lower() == "s":
            caracteres += string.punctuation

        if not caracteres:
            print("Debe seleccionar al menos un tipo de caracteres.")
            return None

        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        return contraseña

    except ValueError:
        print("Por favor, ingrese una longitud válida (número entero).")
        return None

if __name__ == "__main__":
    contraseña_generada = generar_contrasena()
    if contraseña_generada:
        print("Contraseña generada:", contraseña_generada)
