# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:30:11 2020

@author: Caroline
"""


import os

#Charaktere aus der Charakterspalte zählen:

tsvFile = open('Exercise01-lotr_scripts_Bereinigt_Tabtrennung.csv')

lines = tsvFile.readlines()

tsvFile.close()

characters = []
for line in lines:
    cols = line.split('\t')
    characters.append(cols[1])
    
characterCounts = {}

for i in range(1,len(characters)):
    characterCounts[characters[i]] = characterCounts.get(characters[i], 0) + 1
    


characterCountFile = open('Exercise01-charactersCount.csv', 'a')

for name in characterCounts:
    characterCountFile.write(name + ';' + str(characterCounts[name]) + '\n')
    
characterCountFile.close()    



#Charaktere aus der Dialogspalte zählen:

dialogs = []
for zeile in lines:
    column = zeile.split('\t')
    dialogs.append(column[2])
    

woerterDialog = []   
for dialog in dialogs:
    woerter = dialog.split(' ')
    for wort in woerter:
        wort = wort.replace('.','')
        wort = wort.replace(',','')
        wort = wort.replace('?','')
        wort = wort.replace('!','')
        wort = wort.replace(':','')
        woerterDialog.append(wort)
    
        
characterDialog = []  
for a in woerterDialog:
    for person in characters:
        if a.upper() == person:
            characterDialog.append(a.upper())
            break
             
characterCountsDialog = {}     
for x in characterDialog:
    characterCountsDialog[x] = characterCountsDialog.get(x, 0) + 1 
    

characterCountDialogFile = open('Exercise01-characterCountDialog.csv', 'a')
for nameDialog in characterCountsDialog:
    characterCountDialogFile.write(nameDialog + ';' + str(characterCountsDialog[nameDialog]) + '\n')

characterCountDialogFile.close()           
