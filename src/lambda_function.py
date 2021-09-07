from main import main
import json

def lambda_handler(event, context):
    msg = main()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "Success!",
            "message": msg
        })
    }
