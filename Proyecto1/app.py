import string
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generar', methods=['POST'])
def generar():
    data = request.get_json()
    longitud = int(data['longitud'])
    
    caracteres = ""
    if 'minusculas' in data:
        caracteres += string.ascii_lowercase
    if 'mayusculas' in data:
        caracteres += string.ascii_uppercase
    if 'numeros' in data:
        caracteres += string.digits
    if 'especiales' in data:
        caracteres += string.punctuation
    
    if not caracteres:
        return jsonify({"error": "Debe seleccionar al menos un tipo de caracter."}), 400
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return jsonify({"contraseña": contraseña}), 200
