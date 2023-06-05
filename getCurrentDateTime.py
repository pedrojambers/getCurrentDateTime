import datetime

def lambda_handler(event, context):
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {
        'statusCode': 200,
        'body': current_datetime
    }
    return response
