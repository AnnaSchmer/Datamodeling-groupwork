# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:30:22 2020

@author: laura
"""

print("In this python program csv2json there are two different ways to convert a csv file in a JSON file.")
# SIMPLE PROGRAM
import csv, json
print("Try it first with a simple program solution\nWhich file do you want to convert?") 
csvFile_open = input("Filename: ") 

jsonFile_open = "newjsonFile.json"

emptyData = {}
with open(csvFile_open) as csvFile_new:
    csvFile_read = csv.DictReader(csvFile_new, delimiter=';') # change delimter if not ";"
    for csvRow in csvFile_read:
        char = csvRow["char"] # change the name char if not char, in every csv File probably different
        emptyData[char] = csvRow
        
print(emptyData)


with open(jsonFile_open, "w") as jsonFile_open:
    jsonFile_open.write(json.dumps(emptyData, indent=4, ensure_ascii=False)) 
print("csv File is converted to JSON file\t")

# A BIT MORE COMPLEX PROGRAM
import os 
import csv 
import json 
from collections import OrderedDict

# Introduction to the program
print("\nYou can do it also with a bit more complex program solution\nWhich file do you want to convert?") 
filename = input("Filename: ") 
print("Which delimiter (seperator) was used? (for a tabulator write tab, for a new line write new)")
d = input("Delimiter: ")
extension = filename.split(".")[-1].lower()
f = open(filename) 
# for converting different csv Files (with different delimiter)
if extension == "csv": 
    if d == "tab":
        data = list(csv.reader(f, delimiter='\t')) #load csv file, set delimiter as tab 
    elif d == "new":
        data = list(csv.reader(f, delimiter='\n')) #load csv file, set delimiter as newline
    else: 
        data = list(csv.reader(f, delimiter=d)) #load csv file, set delimiter as input 
    print("CSV file loaded") 
else: 
      print("unsupported file type ... exiting") 
      exit()
# convert csv File to json File 
if extension == "csv":
   keys = data[0]  # Header der CSV-Datei
   converted = []
   for i in range(1, len(data)):
      obj = OrderedDict()  # tracks insertion order
      for j in range(0,len(keys)):
         if len(data[i][j]) > 0:
            obj[keys[j]] = data[i][j]
         else:
            obj[keys[j]] = None
      converted.append(obj) 
# creating converted File in json Format      
converted_file_basename = os.path.basename(filename).split(".")[0]
converted_file_extension = ".json" 

if(os.path.isfile(converted_file_basename + converted_file_extension)):
   counter = 1   # if filename already exist counter=1
   
   while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension):
      counter += 1  # if filename already exist counter+=1
   
   converted_file_basename = converted_file_basename + "(" + str(counter) + ")"


try:

    with open(converted_file_basename + converted_file_extension, 'w') as outfile:
        json.dump(converted, outfile, indent=4, ensure_ascii=False)
    
except:
   print("Error creating file ... exiting")
else:
   print("File created:",converted_file_basename + converted_file_extension)

# Quelle: Hsu, J. (2020) How to Build a Command Line JSON/CSV Converter in Python, In: https://medium.com/better-programming/how-to-build-a-command-line-json-csv-converter-in-python-204d74563456, zuletzt aufgerufen am 30.07.2020)
