"""
Simple Temperature Converter Lambda Function
Convert Celsius to Fahrenheit
    
Expected input: {"temperature": 25}
Expected output: {"statusCode": 200, "body": 77}
"""
import json

def lambda_handler(event, context=None):
    temperature = event.get('temperature')
    
    if temperature is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: temperature field is required')
        }

    try:
        celsius = float(temperature)
    except (TypeError, ValueError):
        return {
            'statusCode': 400,
            'body': json.dumps('Error: temperature must be a valid number')
        }
    
    fahrenheit = round(celsius * 9/5 + 32, 2)
    
    return {
        'statusCode': 200,
        'body': fahrenheit
    }
