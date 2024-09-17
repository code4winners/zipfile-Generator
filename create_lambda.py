import boto3
import zipfile
import os

# Define constants
FUNCTION_NAME = 'my_lambda_function'
ROLE_ARN = 'arn:aws:iam::????????:role/lambda_execution_role'  # Replace with your role ARN
REGION = 'us-east-2'  # Replace with your desired AWS region

# Create a ZIP file containing the Lambda function code
def create_zip(zip_name, files):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)

# Create a Lambda client
client = boto3.client('lambda', region_name=REGION)

# Create ZIP file
create_zip('lambda_function.zip', ['lambda_function.py'])

# Read ZIP file
with open('lambda_function.zip', 'rb') as f:
    zipped_code = f.read()

# Create Lambda function
response = client.create_function(
    FunctionName=FUNCTION_NAME,
    Runtime='python3.8',  # Specify your Python version
    Role=ROLE_ARN,
    Handler='lambda_function.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300,  # Timeout in seconds
    MemorySize=128  # Memory in MB
)

print("Lambda function created:", response)
