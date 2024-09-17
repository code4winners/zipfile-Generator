def lambda_handler(event, context):
    # Process the event
    print("Event received:", event)
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
