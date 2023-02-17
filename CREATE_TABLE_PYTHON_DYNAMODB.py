import boto3

dynamodb = boto3.client("dynamodb")

# Creating table

table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            "AttributeName": "Title",
            "AttributeType": "S",
        },
        {
            "AttributeName": "releaseYear",
            "AttributeType": "N",
        },

    ],
    TableName='Movies',
    KeySchema=[
        {"AttributeName": "Title", "KeyType": "HASH",
            
        },
        {"AttributeName": "releaseYear", "KeyType": "RANGE"
            
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
)
