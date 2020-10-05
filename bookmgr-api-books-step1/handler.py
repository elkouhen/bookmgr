import json


def get_books(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps([{
            "id": 1,
            "author": "GoF",
            "title": "Design Patterns"
        }])
    }
