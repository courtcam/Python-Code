#AWS Service Inventory Create a list of services using Python. IE: S3, Lambda, EC2, etc


# intializing the array 
aws_services = []

#making an array of aws services by using the append method  
aws_services.append("ECS")
aws_services.append("VPC")
aws_services.append("Lambda")
aws_services.append("RDS")
aws_services.append("EC2")
aws_services.append("DynamoDB")

#print current array
print(aws_services)

#print the length of the array
print("the Length of my array is ",len(aws_services))

#print the list to dipslay the update list
print(aws_services)

#print the length of the array
print("the Length of my array is ", len(aws_services))


#Removing two item form the array 
aws_services.pop(4)
aws_services.pop(0)

#Print the new list and the new length of the list.
print(aws_services)
print("the Length of my NEW array is ", len(aws_services))
