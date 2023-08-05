import string
import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    longitud = int(request.form['longitud'])
    
    caracteres = ""
    if 'minusculas' in request.form:
        caracteres += string.ascii_lowercase
    if 'mayusculas' in request.form:
        caracteres += string.ascii_uppercase
    if 'numeros' in request.form:
        caracteres += string.digits
    if 'especiales' in request.form:
        caracteres += string.punctuation
    
    if not caracteres:
        return "Debe seleccionar al menos un tipo de caracter."
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return render_template('index.html', contraseña=contraseña)

if __name__ == "__main__":
    app.run(debug=True)