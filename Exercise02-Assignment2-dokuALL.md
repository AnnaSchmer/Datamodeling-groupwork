Assignment 2
============

Exercise 2
----------

### Task 1 - Laura Simunovic

**Dokumentation zu `Exercise02.1-csv2json.py`:**

Programm `Exercise02.1-csv2json.py`- Umwandlung der CSV Datei in JSON Datei
Start: Übung mit der Datei `Exercise01-lotr_scripts_Bereinigt_Tabtrennung.csv`; 
Fragen:
* Where do the JSON key names come from? <br>
  - Regeln für key names (Schlüssel): Strings, ..?
  - aus der Spaltenübersichten schreibt man für JSON Datei den Schlüssel am besten mit der ersten Spaltenname (wenn es geht). Das sollte in einem Programm auch indexiert sein z.B. [0] und nicht das man immer wieder die Spaltennamen hinzufügen muss. 
  
* What about different types of separators?
  - Hier muss man aufpassen und in der Datei schauen, um welches Trennzeichen es sich handelt, wenn ein "," ist, dann muss man nichts dazu machen, aber wenn das Trennzeichen ein ";" oder ein "\t" ist, soll ein *delimiter* bei **csvReader** oder *sep* vorher hinzugefügt werden. Man muss auch berücksichtigen, dass es auch andere gibt wie Doppelnkt ":" oder andere Trennzeichen. In dieser Aufgabe werden aber nur drei wichtigste betrachtet


### Simple program <br>
Import der packeges:
- import csv, json

Mithilfe von input kann man die beliebte csv Datei öffnen
- print("Simple solution\nWhich csv file do you want to convert?") 
- csvFile_open = input("Filename: ") 

So wird der Name neuer JSON Datei sein: 

jsonFile_open = "csvTojsonFile.json"

"Platz" für Leeres Dictioanry erstellen:
- emptyData = {}<br>

Die lotr_clean.csv Datei wird geöffnet:
- with open(csvFile_open) as csvFile_new:<br>

Die csv wird eingelesen und so der Dictionary. Es ist wichtig *delimiter*(Trennzeichen wie ";" oder "\t"), hängt von der csv Datei ab, hinzufügen. Wenn die csv Datei nicht "," als Trennzeichen hat.
- csv_readFile = csv.DictReader(csvFile_new, delimiter=';')<br>
Hier wird der Spaltenname gefragt. Hier wird die *char* genommen, da die erste Spalte keinen Namen hatte. Aber auch mit dem hinzugefügten Name wie Number oder ähnliches kam die Fehlermeldung.

    for csvRow in csvFile_read:<br>
        char = csvRow["char"]<br>
        emptyData[char] = csvRow<br>

Mit dem Befehl `print` wird der Inhalt der csv Datei ausgegeben. Die Spalte **char** ist als `key` und die andere Spalten sind als `values` da inklusive die Spalte **char**. 
print(emptyData)

Hier wird die json Datei mit dem Dateiname csvTojsonFile.json erstellt. Das ist eher ein allgemeiner Name. Im komplexeren Programm wird das berücksichtigt.  
with open(jsonFile_read, "w") as jsonFile_new:
     jsonFile_new.write(json.dumps(emptyData, indent=4, ensure_ascii=False))
     
Um den Unicode beim Output zu vermeiden ist `ensure_ascii=False` hinzugefügt. An der Stelle von Unicode kommt dann einer roter Punkt in Editoren wie Brackets. Wenn man die Datei im Repository öffnet sieht man zuerst keinen Punkt sondern "", das wird dann erst im Editor sichtbar.   
    
Alles in einer Zeile wird als Output ausgegeben.

Um die Aufgabe auf einem simpleren Weg um die Aufgabe zu lösen ist gelungen, aber es ist nicht generisch genug und man müsste sich vor jeder Umwandlung die csv Datei anschauen, um einige Veränderungen im Code durchzuführen, wie z.B. delimiter oder key. 
**Output ist in der Datei `newjsonFile.json` zu finden**
    
Durch die Umwandlung in JSON ist die csv Datei übersichtlicher und lesbarer geworden.

### A bit more complex program:
Dieser komplexer Code habe ich teilweise mithilfe des Codes auf dieser Internetquelle (https://medium.com/better-programming/how-to-build-a-command-line-json-csv-converter-in-python-204d74563456) gelöst und angepasst.
- Es werden zwei neue zusätliche Packages hinzugefügt. Erstmal wird gefragt welche Datei geöffnet sein soll als auch Trennzeichen, der in der csv Datei benutzt wird. 
- Sodass die verschiedene Trennzeichen bei csv Dateien berücksichtigt werden.
- In der Quelle wird die IF-Schleife für die Abfrage der Datei bzw. deren Laden eher als Kommentar geschrieben. Man könnte sagen, dass die Dateiabfrage nicht ausgeführt werden kann, bzw. nicht aktiviert ist. 
- In der Quelle ist ein Fehler in dem Teil des Codes bei der Namensgebung für die JSON Datei.<br>
Unter der while-Schleife: "while os.path.isfile(converted_file_basename + " (" + str(counter) + ")" + converted_file_extension): counter += 1 <br> converted_file_basename = converted_file_basename + " (" + str(counter) + ")" (siehe im Code in der o.g. Datei) ist kamm es zur falscher Einrückung. Es sollte unter direkt *while* steht und nicht nach links eingerückt. 
- Durch die Kommentare im Code kann man die Aufteilung des komplexen Pythonprogramms sehen. Diese Aufteilung ist wichtig wenn man die generische Teile eines Codes nachvollziehen wil.
- Überlegungen zu generischen Teilen: Dateiabfrage, Trennzeichen einer csv Datei sollten berücksichtgt werden (aber immerhin ist es wichtig vorher die csv Datei anzusehen, Größe der Datei, bzw. Länge der Zeilen und Anzahl der Spalten (mit anderen csv habe ich es auch versucht und das spielte keine Rolle, nur delimiter und ggf. Spaltenname bei dem simplen Programm). 

Zusammenfassung:
Der Weg von einem simplen in das komplexe Programm ist nicht so leicht zu machen. Manchmal muss man auch andere Quellen im Internet rechechieren um das Problem zu lösen und ggf. Idee oder Inspiration zu bekommen und das Code anpassen, sodass es für Codeleser verständlich ist. Wichtig in dieser Aufgabe ist ein Programm so zu gestallten, dass verschiedene csv Dateien in json Datei umgewandelt werden könne. Da kommen die generische Teile ins Spiel, die bedeutsam sind, sodass man das Programm immer benutzen kann und nicht jedes Mal etwas in Code zu verändern ist. 


Quellen die mir bei der Aufgabe geholfen haben:
* [Notebook VO7](https://github.com/dis-data-modeling-2020/slides/blob/master/DIS08-07-python-formats.ipynb)
* [Vorlesungsvideo VO7](https://www.youtube.com/watch?v=dCPWvPaXlVg&feature=youtu.be)
* Sweigart, A.: *Automate the boring Stuff with Python : Praktische Programmierung für Einsteiger".* 2., aktualisierte erweiterte Auflage 2020. Heidelberg : dpunkt.verlag,2020. ISBN: 978-3-86490-753-1.
* https://medium.com/better-programming/how-to-build-a-command-line-json-csv-converter-in-python-204d74563456
* https://www.youtube.com/watch?v=La6ZO8vu-1w - Video für simple solution

<hr>

### Task 2 - Anna Schmer

**Dokumentation zu `Exercise02.2-programm.ipynb`:**

Datenset herunterladen und Filme nach Jahr und Genre aufbereiten.
* Task 1: read in the data from the JSON file
  - Alle Abhängigkeiten in den Import statements importieren und die Datei herunterladen und als Variable abspeichern: 
        `response = requests.get("https://raw.githubusercontent.com/dis-data-modeling-2020/slides/master/movies.json")`
  - Die heruntergeladene Datei als Python Objekt encoden und in einer Variable abspeichern:
        `datastore = response.json()`
  - Dies ist wichtig um in Schritt 2 die Daten zu modifizieren.
* Task 2: count for each year, how many movies per genre have appeared:
  - In einer For-Schleife durch den Datensatz iterieren. Dadurch kann jedes Jahr einzeln bearbeitet werden.
  - Für jedes Jahr wird der Counter für die einzelnen Genres auf 0 gesetzt und in zwei jeweils weiteren For-Schleifen tiefer durch den Datensatz iteriert. 
  - Hierbei kommen wir in der dritten Ebene bei den Genres an. Durch if else statements werden die zum Filmtitel zugehörigen Genres überprüft und der jeweilige Counter hochgesetzt. 
  - Der so erzeugte Counter mit dem dazugehörenden Jahr wird nun als Json String in eine Variable zwischengespeichert: 
        `genresJson = json.dumps(genres)` 
* Task 3: create a CSV file where for each year, the counts for each genre are listed.
  - Mit dem Pandas Befehl df = pd.read_json(genresJson) den Json String zu einem Pandas Objekt umwandeln und letztlich mit dem Befehl:
        `df.to_csv(r'Filmgenres.csv')`
  - in eine CSV-Datei umwandeln. Das r vor dem Dateinamen wird als Absicherung eingesetzt, damit ein eventuell angegebener Dateipfad auch unter Windows korrekt eingelesen wird und Backslashes nicht als Sonderzeichen gewertet werden.
Um das Resultat zu sehen wird die erzeugte CSV-Datei eingelesen und ausgegeben. 

* Quellen:
   
   - Modulunterlagen
   - https://datatofish.com/json-string-to-csv-python/
   - https://thispointer.com/python-pandas-access-and-change-column-names-row-indexes-in-dataframe/

<hr>

### Bonus - Sheila Waldispühl

**Dokumentation zu `Exercise02.Bonus.figure1.points.lines-programm.R`, `Exercise02.Bonus.figure2.area-programm.R`, `Exercise02.Bonus.figure3.areaPercentage-programm.R`, `Exercise02.Bonus.figure4.stackedBarplot-programm.R` und `Exercise02.Bonus.figure5.scatterplott-programm.R`:**

Erstellung von Grafiken zu den Filmgenres in R
1. Drehen der Csv Datei (Zeilen-Spalten-tausch) aus der `Exercise02.2-Filmgenres.csv`
    1. Vor der Drehung machte es mir einige Probleme in R und Python die Grafiken zu erstellen (weil ich bis jetzt nur mit csv Dateien in dieser Form gearbeitet habe).
1. Erstellen von vers Grafiken
    1. Grafik 1: Liniendiagramm der Filme pro Genre über die Zeit
       1. PNG: `Exercise02.Bonus.figure1.points.lines-graph`
       1. Code: `Exercise02.Bonus.figure1.points.lines-programm.R`
    1. Grafik 2: Flächendiagramm der Menge aller Filme pro Genres über die Zeit
       1. PNG: `Exercise02.Bonus.figure2.area-programm-graph.png`
       1. Code: `Exercise02.Bonus.figure2.area-programm.R`
    1. Grafik 3: Flächendiagramm der prozentualen Menge der Filme pro Genre über die Zeit
       1. PNG: `Exercise02.Bonus.figure3.areaPercentage-graph.png`
       1. Code: `Exercise02.Bonus.figure3.areaPercentage-programm.R`
    1. Grafik 4: Gestapeltes Säulendiagramm der Menge aller Filme pro Genres über die Zeit
       1. PNG: `Exercise02.Bonus.figure4.stackedBarplo-graph.png`
       1. Code: `Exercise02.Bonus.figure4.stackedBarplot-programm.R`
    1. Grafik 5: Punkte Diagramm-Matrix mit Trendlinie der Anzahl Filme pro Genre über die Zeit
       1. PNG: `Exercise02.Bonus.figure5.scatterplott-graph.png`
       1. Code: `Exercise02.Bonus.figure5.scatterplott-programm.R`

* Bei der Erstellung der Grafiken gibt es verschiedene Probleme
  - Das Hauptproblem ist die Datenfülle. Bei 27 Merkmalen wird die Grafik schnell überfüllt. 
     - Überlegung, ob ich die Werte aufspalten soll.
     - Liniendiagramme & Punktediagramme wirken nicht so überfüllt.
  - Hindernisse bei der Erstellung der Grafiken
     1. Farbdarstellung: Es besteht kein ColorBrewer der 27 verschiedene Farben darstellen kann. Darum muss mit einem Trick das Set auf 27 Werte erweitert werden.`getPalette = colorRampPalette(brewer.pal(9, "Set1"))` `scale_fill_manual(values = getPalette(27))+`
     1. Bei dem Liniendiagramm habe ich die Werte einzeln aufgelistet, was eigentlich dafür sorgt, dass ich 27 verschiedene Liniendiagramme in einer Grafik darstelle. Dies ist bei dem Flächendiagramm jedoch nicht möglich, weil dort die Flächen aufeinander addiert werden müssen. Darum musste ich die Daten gruppieren um den Plot zu erstellen. `genres %>%` `mutate(Year = as.Date(paste0(Year, "-01-01"))) %>%` `gather(Genre, value, Comedy:OhneGenre) %>%` Bei der Gruppierung mit as.date können nur Daten mit Monats und Tagesangaben verwertet werden. Darum muss ich die Angaben erweitern `mutate(Year = as.Date(paste0(Year, "-01-01"))) %>%`
     1. Um die Farbunterscheidung beim Barplot zu erleichtern habe ich eine weisse umrandung eingefügt. ` geom_bar(stat="identity",alpha=1.2 , size=0.1, colour="white")+`
     1. Bei der Matrix der Punktediagramme habe ich mit `geom_smooth(method = "lm", se=FALSE, color="black", formula = y ~ x)+` eine Trendlinie eingefügt. Mit `facet_wrap(~Genre, ncol=9, nrow=3)+` habe ich die Punktewolken in einer Matrix angeordnet und deren Reihung definiert, damit alle Grafiken auf der selben Achse liegen.
Die dazugehörigen Grafiken habe ich im .png Format hinzugefügt.

* Quellen:
  - https://felixfan.github.io/ggplot2-remove-grid-background-margin/
  - https://stackoverflow.com/questions/10349206/add-legend-to-ggplot2-line-plot/10355844 
  - http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/
  - https://www.r-bloggers.com/how-to-expand-color-palette-with-ggplot-and-rcolorbrewer/
  - https://stackoverflow.com/questions/15282580/how-to-generate-a-number-of-most-distinctive-colors-in-r 
  - http://md.psych.bio.uni-goettingen.de/x/mv/unit/dataframe/dataframe.html
  - https://stackoverflow.com/questions/11610377/how-do-i-change-the-formatting-of-numbers-on-an-axis-with-ggplot
  - https://ggplot2.tidyverse.org/reference/position_stack.html
  - https://www.r-graph-gallery.com/136-stacked-area-chart
  - https://stackoverflow.com/questions/8750871/ggplot2-reverse-order-of-scale-brewer 
  - https://www.r-graph-gallery.com/274-map-a-variable-to-ggplot2-scatterplot.html
  - https://www.sharpsightlabs.com/blog/small-multiples-ggplot/
  - https://stackoverflow.com/questions/38412817/draw-a-trend-line-using-ggplot
  - http://www.cookbook-r.com/Graphs/Scatterplots_(ggplot2)/
  - https://www.r-graph-gallery.com/241-custom-layout-strip-ggplot2.html
  - Vorlesungsunterlagen Dis04 - Informationsvisualisierung
