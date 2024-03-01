import json
import cv2
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: " + json.dumps(event))
    request_body = event.get('body')  # Note the lowercase 'b'
    if request_body is not None:
        data = json.loads(request_body)
        # Process the data
        return {"statusCode": 200, "body": json.dumps({"message": "Success"})}
    else:
        return {"statusCode": 400, "body": json.dumps({"message": "Request body is missing"})}

    return "Success"

