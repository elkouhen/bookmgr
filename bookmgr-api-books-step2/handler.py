import json

import boto3


def create_dynamodb_client():
    return boto3.client("dynamodb")


def get_books(event, context):
    dynamodb = create_dynamodb_client()

    books = dynamodb.scan(TableName="books")['Items']

    return {
        "statusCode": 200,
        "body": json.dumps(books)
    }
