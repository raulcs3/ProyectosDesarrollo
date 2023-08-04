from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_caracteres_especiales=True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_caracteres_especiales:
        caracteres += string.punctuation
    caracteres += string.digits

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para generar la contraseña
@app.route('/generar_contraseña', methods=['POST'])
def generar():
    longitud = int(request.form['longitud'])
    usar_mayusculas = 'mayusculas' in request.form
    usar_minusculas = 'minusculas' in request.form
    usar_caracteres_especiales = 'caracteres_especiales' in request.form

    contraseña_generada = generar_contraseña(
        longitud,
        incluir_mayusculas=usar_mayusculas,
        incluir_minusculas=usar_minusculas,
        incluir_caracteres_especiales=usar_caracteres_especiales
    )

    return contraseña_generada

if __name__ == "__main__":
    app.run(debug=True, port=5000)
