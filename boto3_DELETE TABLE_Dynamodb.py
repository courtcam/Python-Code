import boto3

dynamodb= boto3.client('dynamodb')
response = dynamodb.delete_table(TableName = "Movie_listv4")

print(response)




