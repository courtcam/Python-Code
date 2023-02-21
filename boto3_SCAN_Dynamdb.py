import boto3
dynamodb = boto3.resource('dynamodb')
table=dynamodb.Table('Movie_listv4')
response = table.scan(
    ExpressionAttributeNames={
        '#T': 'Title',
        '#RY': 'releaseYear',
    },
    ExpressionAttributeValues={
        ':t': {
            'R': '2022',
        },
    },
    #FilterExpression='budget = :b',
    #ProjectionExpression='#T, #RY',
    #TableName='Movie_list v4',
)

print(response)