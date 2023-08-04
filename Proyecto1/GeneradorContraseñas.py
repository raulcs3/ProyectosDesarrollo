from flask import Flask, render_template, request
import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_caracteres_especiales=True):
    caracteres = ""

    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

if __name__ == "__main__":
    longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: "))
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    contrasena_generada = generar_contrasena(
        longitud_deseada,
        incluir_mayusculas,
        incluir_minusculas,
        incluir_numeros,
        incluir_caracteres_especiales
    )

    print("Contraseña generada:", contrasena_generada)
