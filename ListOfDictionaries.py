#!/usr/bin/env python3.7

# generates a list of dictionaries about files in the working directory
import os

# Get working directory and assign it to the varible "Path" 
path = os.getcwd()

#list all the DIR in the current working DIR by passing in the path parameter
ListOfDir  = os.listdir(path)

for i in ListOfDir:
 
   pathOfFile = path + "/"+ i 
   size = os.path.getsize(path + "/"+ i)
   ListOfDict = {'NAME' : i, 'PATH' : pathOfFile, 'SIZE' : size}
   print(ListOfDict)
 