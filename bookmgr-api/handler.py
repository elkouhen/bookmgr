import json
import os

import boto3
from dynamodb_json import json_util as json


def list_books_(client):
    books = client.scan(TableName="books")['Items']

    return json.loads(books)


def list_books_handler(event, context):
    dynamodb = create_dynamodb_client()

    books = list_books_(dynamodb)

    print(books[0])

    return books[0]


def create_dynamodb_client():
    if os.environ['IS_OFFLINE']:
        return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")
    else:
        return boto3.client("dynamodb")


def main():
    # Create the DynamoDB Client with the region you want
    dynamodb = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")

    # Call DynamoDB's query API
    print(list_books_(dynamodb))


if __name__ == "__main__":
    main()
