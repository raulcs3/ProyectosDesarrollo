import string
import random

def generar_contrasena():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    
    # Caracteres a utilizar

    caracteres = ""
    if input("¿Incluir caracteres en minúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_lowercase
    if input("¿Incluir caracteres en mayúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_uppercase
    if input("¿Incluir números? (s/n): ").lower() == "s":
        caracteres += string.digits
    if input("¿Incluir caracteres especiales? (s/n): ").lower() == "s":
        caracteres += string.punctuation
    
    # Verificar que el usuario haya seleccionado al menos un tipo de caracter

    if not caracteres:
        print("Debe seleccionar al menos un tipo de caracter.")
        return
    
    # Generar la contraseña aleatoria

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    print("Contraseña generada:", contraseña)

if __name__ == "__main__":
    generar_contrasena()