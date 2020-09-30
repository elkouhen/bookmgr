import json


def list_books(event, context):
    body = [{
        "title": "Go Serverless v1.0 !",
        "author": "serverless.com"
    },
    {
        "title": "Go Serverless v2.0 !",
        "author": "serverless.com"
    }]

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
