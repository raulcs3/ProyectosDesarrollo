import json
from app import generar

def handler(event, context):
    try:
        data = json.loads(event['body'])
        result = generar(data)
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
