import json

# Load the AWS SDK for Python
import boto3
from botocore.exceptions import ClientError

ERROR_HELP_STRINGS = {
    # Common Errors
    'InternalServerError': 'Internal Server Error, generally safe to retry with exponential back-off',
    'ProvisionedThroughputExceededException': 'Request rate is too high. If you\'re using a custom retry strategy make sure to retry with exponential back-off.' +
                                              'Otherwise consider reducing frequency of requests or increasing provisioned capacity for your table or secondary index',
    'ResourceNotFoundException': 'One of the tables was not found, verify table exists before retrying',
    'ServiceUnavailable': 'Had trouble reaching DynamoDB. generally safe to retry with exponential back-off',
    'ThrottlingException': 'Request denied due to throttling, generally safe to retry with exponential back-off',
    'UnrecognizedClientException': 'The request signature is incorrect most likely due to an invalid AWS access key ID or secret key, fix before retrying',
    'ValidationException': 'The input fails to satisfy the constraints specified by DynamoDB, fix input before retrying',
    'RequestLimitExceeded': 'Throughput exceeds the current throughput limit for your account, increase account level throughput before retrying',
}

# Use the following function instead when using DynamoDB Local
#def create_dynamodb_client(region):
#    return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000", aws_access_key_id="access_key_id", aws_secret_access_key="secret_access_key")

def create_dynamodb_client(region="us-east-1"):
    return boto3.client("dynamodb", region_name=region)


def create_query_input():
    return {
        "TableName": "Books",
        "KeyConditionExpression": "#5fda0 = :5fda0",
        "ExpressionAttributeNames": {"#5fda0":"Author"},
        "ExpressionAttributeValues": {":5fda0": {"S":"Author"}}
    }


def execute_query(dynamodb_client, input):
    try:
        response = dynamodb_client.query(**input)
        print("Query successful.")
        # Handle response
    except ClientError as error:
        handle_error(error)
    except BaseException as error:
        print("Unknown error while querying: " + error.response['Error']['Message'])


def handle_error(error):
    error_code = error.response['Error']['Code']
    error_message = error.response['Error']['Message']

    error_help_string = ERROR_HELP_STRINGS[error_code]

    print('[{error_code}] {help_string}. Error message: {error_message}'
          .format(error_code=error_code,
                  help_string=error_help_string,
                  error_message=error_message))


def list_books(event, context):
    body = [
        {
            "key": 0,
            "title": "Go Serverless v1.0 !",
            "author": "serverless.com"
        },
        {
            "key": 1,
            "title": "Go Serverless v2.0 !",
            "author": "serverless.com"
        }]

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response



def main():
    # Create the DynamoDB Client with the region you want
    dynamodb_client = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")

    # Create the dictionary containing arguments for query call
    query_input = create_query_input()

    # Call DynamoDB's query API
    print(execute_query(dynamodb_client, query_input))


if __name__ == "__main__":
    main()