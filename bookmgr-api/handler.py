import json

# Load the AWS SDK for Python
import boto3
from dynamodb_json import json_util as json

def create_dynamodb_client(region="us-east-1"):
    return boto3.resource("dynamodb", region_name=region)

def list_books_(client):
    books = client.scan(TableName="books")['Items']

    return json.loads(books)

def list_books_handler(event, context):

    dynamodb = boto3.client("dynamodb")

    return list_books_(dynamodb)


def main():
    # Create the DynamoDB Client with the region you want
    dynamodb = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")

    # Call DynamoDB's query API
    print(list_books_(dynamodb))


if __name__ == "__main__":
    main()