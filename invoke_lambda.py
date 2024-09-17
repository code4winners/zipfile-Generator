import boto3
import json

# Define constants
FUNCTION_NAME = 'my_lambda_function'
REGION = 'us-east-2'  # Replace with your desired AWS region

# Create a Lambda client
client = boto3.client('lambda', region_name=REGION)

# Define payload
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# Invoke Lambda function
response = client.invoke(
    FunctionName=FUNCTION_NAME,
    InvocationType='RequestResponse',  # 'Event' for asynchronous invocation
    Payload=json.dumps(payload)
)

# Read response
response_payload = response['Payload'].read().decode('utf-8')
print("Response:", response_payload)
