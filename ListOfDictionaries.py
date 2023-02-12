# generates a list of dictionaries about files in the working directory


import os

# Get working directory and assign it to the varible "Path" 
path = os.getcwd()

#list all the DIR in the current working DIR by passing in the path parameter
ListOfDir  = os.listdir(path)

#szieOfpath = path +
#print(ListOfDir)

for i in ListOfDir:
   print(os.getcwd() + "/"+ i )
   size = os.path.getsize(os.getcwd() + "/"+ i)
   #print(size)