#!/usr/bin/python

import os

path = os.getcwd()

file_info = []


for file in os.listdir():
    
    file_size = os.stat(file).st_size
    
    file_info.append({
        
        'name': file,
        'size': file_size
        
        })
        
print(*file_info, sep="\n")