#!/usr/bin/env python3.7
# generates a list of dictionaries about files in the working directory

import os
# Get working directory and assign it to the varible "Path" 
path = os.getcwd()

#list all the DIR in the current working DIR by passing in the path parameter
ListOfFiles  = os.listdir(path)

# A for loop that iterate over the list of files 
for i in ListOfFiles:
 
 #concatenating the current working directory and each file to get the path and assign it to a variable
   pathOfFile = path + "/"+ i
# get the size of the path and assign it to a variable
   size = os.path.getsize(path + "/"+ i)
   ListOfDict = {'NAME' : i, 'PATH' : pathOfFile, 'SIZE' : size}
   print(ListOfDict)
 