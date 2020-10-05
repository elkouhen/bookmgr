import json
import os

import boto3
from dynamodb_json import json_util as dynamodb_json


def create_dynamodb_client():
    return boto3.client("dynamodb")


def get_books_(client):
    books = client.scan(TableName="books")['Items']

    return books


def get_books(event, context):
    dynamodb = create_dynamodb_client()

    books = get_books_(dynamodb)

    return {
        "statusCode": 200,
        "body": json.dumps(books)
    }
