# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:31:51 2020

@author: Caroline
"""


import requests
import requests_cache
import bs4
import csv
import json
import re


#Teil 1: Erstellen der csv-Datei mit den zwei Spalten "Mitgliedsstaaten" und "URL"


#Erstellen einer csv-Datei im Write-Modus
unMemberStates = open('Exercise03-UN-MemberStates.csv' , 'w', newline ='')
unMemberStatesWriter = csv.writer(unMemberStates, delimiter =';')

#Schreiben der 1. Zeile der csv-Datei (Die Überschriften)
unMemberStatesWriter.writerow(['Mietgliedsstaat', 'URL'])

#Abfangen von Web-traffic
requests_cache.install_cache('demo_cache')

#Öffnen der Ressource und Selektion der gesuchten Elemente
resource = requests.get('https://de.wikipedia.org/wiki/Mitgliedstaaten_der_Vereinten_Nationen')
wikiSoup = bs4.BeautifulSoup(resource.content)
elements = wikiSoup.select('table.wikitable tr')

#Mitgliedsstaaten sowie die dazugehörige URL wird in die csv-Datei geschrieben
for x in elements:
    if x.attrs.get('class') != None:        #ehemalige Mitgliedsstaaten, welche in der Tabelle farblich markiert sind, werden aussortiert
        if x.attrs.get('class')[0] == 'hintergrundfarbe5':       
            continue
        elif x.attrs.get('class')[0] == 'hintergrundfarbe6':
            continue
    try:
        land = x.findChild('td').find_next_sibling('td').find('a').text
        url = 'https://de.wikipedia.org' + str(x.findChild('td').find_next_sibling('td').find('a').attrs.get('href'))
        unMemberStatesWriter.writerow([land, url])
    except:
        continue        #bei der 1. Zeile (Überschriften) soll die Schleife einfach weiter gehen

unMemberStates.close()     
   


#Teil 2: Für jeden Mitgliedsstaat die Attribute aus der Infobox extrahieren und in einer geeigneten Datenstruktur abspeichern


#Funktionen definieren, um die Attribute "Hauptstadt", "Einwohnerzahl", "Fläche" und "Amtssprachen" der jeweiligen Länder zu extrahieren    

#Hauptstadt finden
def hauptstadtFinden(laenderSoup):
    hauptstadtString = laenderSoup.find('a', text='Hauptstadt')
    if hauptstadtString == None:                    #Da Liechtenstein keine Hauptstadt besitzt 
        hauptstadt = 'Es existiert keine Hauptstadt'
    else:    
        grandparentHauptstadtString = hauptstadtString.parent.parent
        siblingHauptstadt = grandparentHauptstadtString.find_next_sibling('td')
        hauptstadtTag = siblingHauptstadt.findChild('a', recursive=False)
        if hauptstadtTag == None:                   #Teilweise steht die Hauptstadt nicht in einem a-Tag, sondern direkt im td-Tag
            hauptstadt = siblingHauptstadt.text.strip()
        else:    
            hauptstadt = hauptstadtTag.text
    return hauptstadt



#Einwohnerzahl finden
def einwohnerzahlFinden (laenderSoup):
    einwohnerString = laenderSoup.find('a', text='Einwohnerzahl')
    grandparentEinwohnerString = einwohnerString.parent.parent
    siblingEinwohner = grandparentEinwohnerString.find_next_sibling('td')
    einwohnerZahl = siblingEinwohner.text.strip()
    regexEinwohner = re.compile(r'\[[A-Z 0-9]\]')
    regexEinwohner2 = re.compile(r'\n')
    einwohnerZahl = re.sub(regexEinwohner, '', einwohnerZahl)
    einwohnerZahl = re.sub(regexEinwohner2, ' ', einwohnerZahl)
    return einwohnerZahl


#Fläche finden
def flaecheFinden(laenderSoup):
    flaecheString = laenderSoup.find('a', text='Fläche' )
    grandparentFlaecheString = flaecheString.parent.parent
    siblingFlaeche = grandparentFlaecheString.find_next_sibling('td')
    flaeche = siblingFlaeche.text.strip()           
    regexFlaeche = re.compile(r'\[[A-Z 0-9]*\]')
    regexFlaeche2 = re.compile(r'\n')
    flaeche = re.sub(regexFlaeche, '', flaeche)
    flaeche = re.sub(regexFlaeche2, ' ', flaeche)
    return flaeche



#Amtssprachen finden
def amtssprachenFinden(laenderSoup):
    spracheString = laenderSoup.find('a', text='Amtssprache')
    grandparentSpracheString = spracheString.parent.parent
    siblingSprache = grandparentSpracheString.find_next_sibling('td')

    spracheTags = siblingSprache.find_all('a', recursive=False)

    sprachen = []

    for i in spracheTags:
        sprachen.append(i.text)
    return sprachen




#csv-Datei der Mitgliedsstaaten öffnen
csvFileObject = open('Exercise03-UN-MemberStates.csv')      
readerObject = csv.reader(csvFileObject, delimiter = ';')


#Erstellen eines leeren Dictionaries als Datenstruktur für die Mitgliedsstaaten und deren Attribute
mitgliedsstaaten = {}


#Über die csv-Datei iterieren und die jeweiligen Daten im Dictionary "mitgliedsstaaten" abspeichern
for row in readerObject:
    if readerObject.line_num == 1:
        continue               #Erste Zeile überspringen
    dictionaryland = {}        #Erstellen eines Dictionaries für das jeweilige Land
    resourceLand = requests.get(row[1])
    laenderSoup = bs4.BeautifulSoup(resourceLand.content, from_encoding='utf-8')
    dictionaryland['Hauptstadt']= hauptstadtFinden(laenderSoup)
    dictionaryland['Einwohnerzahl']= einwohnerzahlFinden(laenderSoup)
    dictionaryland['Flaeche']= flaecheFinden(laenderSoup)
    dictionaryland['Amtssprachen']= amtssprachenFinden(laenderSoup)
    mitgliedsstaaten[row[0]] = dictionaryland
    


csvFileObject.close()


 
#Teil 3: Das Dictionary in eine json-Datei schreiben

jsonFile = open('Exercise03-UN-MemberStates-Attributes.json', 'w', encoding='utf-8')
json.dump(mitgliedsstaaten, jsonFile, indent=4, ensure_ascii=False)
jsonFile.close()


   