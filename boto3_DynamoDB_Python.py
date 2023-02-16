import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',
            'AttributeType': 'S',
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'releaseYear',
            'KeyType': 'HASH',
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='Movies',
)

print(response)



response = dynamodb.put_item(
    Item={
        "Title":{
          "S":"soul"
       },
       "ratings":{
          "N":"8.8"
       },
       "revenue":{
          "N":"2000000000"
       },
       "releaseYear":{
          "S":"2020"
       },
       "budget":{
          "N":"150000000"
       },
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Movies',
)