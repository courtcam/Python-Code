import boto3

dynamodb = boto3.client('dynamodb')

#Creating table 

table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Title',
            'AttributeType': 'S',
        },
        
        {
            'AttributeName': 'releaseYear',
            'AttributeType': 'N'
        },
       
        {
            'AttributeName': 'ratings',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'budget',
            'AttributeType': 'N'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Title',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'releaseYear',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='Movies',
)

print(table)

response = dynamodb.put_item(
   
    Item1={
        
        "Title":
          "soul"
       ,
       "ratings":
          "8.8"
       ,
       "releaseYear":
           "2020"
       ,
       "budget":
          "150000000"
    }  
   
    Item2={
        
        "Title":
            "Avatar"
       ,
       "ratings":
           "8"
       ,
       "releaseYear":
           "2009"
       ,
       "budget":
          "237000000"
       
    }

	Item3={
       
        "Title":
          "Avenger Endgame"
       ,
       "ratings":
          "8.5"
       ,
       "releaseYear":
          "2019"
       ,
       "budget":
          "357000000"     
    }
	
	Item4={
       
        "Title":
          "Black Adam"
       ,
       "ratings":
          "6.5"
       ,
       "releaseYear":
          "2022"
       ,
       "budget":
          "260000000"
      
    }  
       
    Item5={   
       
        "Title":
		"Avenger Endgame"
       ,
       "ratings":
	   "8.5"
       ,
       "releaseYear":
          "2019"
       ,
       "budget":
          "357000000"
       ,
       
    Item6={  
        "Title":
		  "Wakanda"
       ,
       "ratings":
          "8"
       ,
       "releaseYear":
          "2022"
       ,
       "budget":
	   "250000000"
    }
	   
	   
       
    Item7={       
        "Title":
            "Black Panther"
        ,
       "ratings":
           "8"
       ,
       "releaseYear":
           "2018"
       ,
       "budget":
           "250000000"
    }
       
    Item8={
        "Title": 
            "barbershop"
       ,
       "ratings":
           "5"
       ,
       "releaseYear":
           "2002"
       ,
       "budget":
           "12000000"
    }
       
     Item9={  
        "Title":
            "Justice League"
       ,
       "ratings":
           "6.5"
       ,
       "releaseYear":
           "2017"
       ,
       "budget":
           "300000000"
    }
       
     Item10={  
       
        "Title":
            "Spider man 3"
       ,
       "ratings":
           "7.5"
       ,
       "releaseYear":
           "2007"
       ,
       "budget":
           "258000000"
     }
       
       
    },
    ReturnConsumedCapacity='TOTAL',
    TableName='Movies',
)