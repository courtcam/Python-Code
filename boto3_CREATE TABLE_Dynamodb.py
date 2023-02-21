import boto3

dynamodb = boto3.client("dynamodb")

# Creating table

response = dynamodb.create_table(
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
    KeySchema=[
        {"AttributeName": "Title", "KeyType": "HASH",
            
        },
        {"AttributeName": "releaseYear", "KeyType": "RANGE"
            
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10,
    },
    TableName='Movie_listv6',
)
print(response)