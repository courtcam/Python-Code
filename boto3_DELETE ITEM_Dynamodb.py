import boto3
dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('Movie_listv4')
from boto3.dynamodb.conditions import Key, Attr
response = table.delete_item(
    Key={
        'Title': 'Wakanda'
    }
)
print(response)