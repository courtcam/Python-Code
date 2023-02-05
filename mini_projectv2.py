# intializing the array 
aws_services = []

#making an array of aws services 
aws_services = ["S3", "lambda", "RDS","EC2","VPC", "dynamoDB"]

#print current array
print(aws_services)

#print the length of the array
print(len(aws_services))

#add another service to the exiing list
aws_services.append("ECS")

#print the list to dipslay the update list
print(aws_services)

#print the length of the array
print(len(aws_services))


#Remove an item form the array 
aws_services = aws_services.remove("VPC")

print(aws_services)