import boto3

dynamodb = boto3.client("DynamoDB")
# dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY')
table = dynamodb.Table("Movies")
with table.batch_writer() as batch:

    batch.put_item(Item={"Title": "soul","ratings": "8.8","releaseYear": "2020","budget": "150000000",})
    batch.put_item(Item={"Title": "Avatar","ratings": "8","releaseYear": "2009","budget": "237000000",})
    batch.put_item(Item={"Title": "Avenger Endgame","ratings": "8.5","releaseYear": "2019","budget": "357000000",})
    batch.put_item(Item={"Title": "Black Adam","ratings": "6.5","releaseYear": "2022","budget": "260000000",})
    batch.put_item(Item={"Title": "Avenger Endgame","ratings": "8.5","releaseYear": "2019","budget": "357000000",})
    batch.put_item(Item={"Title": "Wakanda","ratings": "8","releaseYear": "2022","budget": "250000000",})
    batch.put_item(Item={"Title": "Black Panther","ratings": "8","releaseYear": "2018","budget": "250000000",})
    batch.put_item(Item={"Title": "barbershop","ratings": "5","releaseYear": "2002","budget": "12000000",})
    batch.put_item(Item={"Title": "Justice League","ratings": "6.5","releaseYear": "2017","budget": "300000000",})
    batch.put_item(Item={"Title": "Spider man 3","ratings": "7.5","releaseYear": "2007","budget": "258000000",})
#print(batch)
