import json
import string
import random

def generar(event, context):
    if event['httpMethod'] != 'POST':
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Método no permitido'})
        }

    data = json.loads(event['body'])
    longitud = int(data['longitud'])
    minusculas = data.get('minusculas', False)
    mayusculas = data.get('mayusculas', False)
    numeros = data.get('numeros', False)
    especiales = data.get('especiales', False)

    caracteres = ''
    if minusculas:
        caracteres += string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    if not caracteres:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Debe seleccionar al menos un tipo de caracter.'})
        }

    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    return {
        'statusCode': 200,
        'body': json.dumps({'contraseña': contraseña})
    }
