
import json

def lambda_handler(event, context):
    # TODO implement
    message = 'Ya were in Lambda'
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
