#! /bin/python3
# -*- coding: utf-8 -*-
 
import sys
import os

usage = "Usage: python emotivEDFFixer.py <FILES and DIRS>"

if len(sys.argv) <2:
    print("Error: No argumets given")
    print(usage)
    sys.exit(-1)

#nsField = slice(252,256)
#reservedField = slice(192,236)
headerSizeField = slice(184,192)

def fixEDF(path):
    with open(path,"rb") as file:
        data = file.read()
    
    headerSize = int(data[headerSizeField])
    
    newData = data[:headerSize].replace(bytes(1), b" ") +\
              data[headerSize:]
    
    if newData == data:
        print(path, "doesn't need to be fixed.")
    else:
        basePath, ext = os.path.splitext(path)
        newPath = basePath + "Fixed" + ext
        with open(newPath, "wb") as output:
            output.write(newData)
        
        print(path, "has been fixed. Look for", newPath)
    

for path in sys.argv[1:]:
    if os.path.isfile(path):
        fixEDF(path)
    
    elif os.path.isdir(path):
        for file in os.listdir(path):
            _, ext = os.path.splitext(file)
            newPath = os.path.join(path, file)
            if os.path.isfile(newPath) and ext == ".edf":
                fixEDF(newPath)