import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')


table = dynamodb.Table('Movie_listv4')

response = table.query(
    KeyConditionExpression=Key("Title").eq("Wakanda") #query the table for any tile with "Wakanda"
)

for i in response['Items']: # looping through my table and printing the all the result with that match my key conditions
   #print the screen, using  all the all the fields based on the response from the key condition 
    print(i['Title'], ":", i['releaseYear'], ":",i['ratings'], ":", i['budget']) 
