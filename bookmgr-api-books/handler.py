import json
import os

import boto3
from dynamodb_json import json_util as dynamodb_json


def create_dynamodb_client():
    if 'IS_OFFLINE' in os.environ:
        return boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")
    else:
        return boto3.client("dynamodb")


def get_books_(client):
    books = client.scan(TableName="books")['Items']

    return dynamodb_json.loads(books)


def get_books(event, context):
    dynamodb = create_dynamodb_client()

    books = get_books_(dynamodb)

    return {
        "statusCode": 200,
        "body": json.dumps(books)
    }


def main():
    # Create the DynamoDB Client with the region you want
    dynamodb = boto3.client("dynamodb", region_name="localhost", endpoint_url="http://localhost:8000")

    # Call DynamoDB's query API
    print(list_books_(dynamodb))


if __name__ == "__main__":
    main()
