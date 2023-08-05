import string
import random

def generar_contrasena():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    
    caracteres = ""
    if input("¿Incluir caracteres en minúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_lowercase
    if input("¿Incluir caracteres en mayúsculas? (s/n): ").lower() == "s":
        caracteres += string.ascii_uppercase
    if input("¿Incluir números? (s/n): ").lower() == "s":
        caracteres += string.digits
    if input("¿Incluir caracteres especiales? (s/n): ").lower() == "s":
        caracteres += string.punctuation
    
        print("Debe seleccionar al menos un tipo de caracter.")
        return
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    print("Contraseña generada:", contraseña)

if __name__ == "__main__":
    generar_contrasena()