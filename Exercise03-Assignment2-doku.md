Assignment 2
============

Exercise 1
----------

**Dokumentation zu "Exercise03-Assignment2.py":**

1. Teil 1: Erstellen der csv-Datei mit den zwei Spalten "Mitgliedsstaaten" und "URL":  
- Erstellen einer csv-Datei im Write-Modus und zugehörigem Reader Objekt  
- Erste Zeile der csv-Datei (also die Überschriften) schreiben  
- Web-Traffic abfangen  
- Öffnen der Ressource und mittels Beautifulsoup die tr-Tags aus der Tabelle filtern, da diese die einzelnen Zeile der Tabelle beinhalten  
- Einzelne Mitgliedsstaaten mit zugehöriger URL in die csv-Datei schreiben  
  - Dazu iteriert man über die gefilterten tr-Tags  
  - Ehemalige Mitgliedsstaaten werden aussortiert, indem die for-Schleife einfach weiterläuft, wenn der tr-Tag eine Klasse mit den jeweiligen Hintergrundfarben besitzt, die die ehemaligen Mitglieder kennzeichnet  
  - Im try-Block werden dann die Namen der Mitgliedsstaaten und die URL's in die csv-Datei geschrieben
  - Die Exception entsteht, da der erste tr-Tag (Spaltenüberschrift) keinen tb-Tag als Child-Tag besitzt. Da wir diese Zeile aber sowieso auslassen wollen, soll die for-Schleife einfach weiterlaufen  
  

2. Teil 2: Für jeden Mitgliedsstaat die Attribute aus der Infobox extrahieren und in einer geeigneten Datenstruktur abspeichern:  
- Funktionen definieren, um die Attribute "Hauptstadt", "Einwohnerzahl", "Fläche" und "Amtssprachen" der jeweiligen Länder zu extrahieren  
  - Hauptstadt finden  
    - Mit Beautifulsoup suchen wir den a-Tag mit dem Text "Hauptstadt", um von dort aus über Eltern, Geschwister sowie Kind Elementen zu der gesuchten Hauptstadt zukommen  
    - Hier müssen wir eine If-Bedingung benutzen, da die Hauptstadt mal in einem a-Tag und mal direkt im td-Tag steht  
    - Da Liechtenstein keine Hauptstadt besitzt und somit BeautifulSoup keinen Text "Hauptstadt" findet, wird dies mit if abgefangen und ein Alternativtext festlegen  
  - Einwohnerzahl finden  
    - Mit Beautifulsoup suchen wir den a-Tag mit dem Text "Einwohnerzahl", um von dort aus über Eltern, Geschwister sowie Kind Elementen zu der gesuchten Einwohnerzahl zu gelangen  
    - Da hier teilweise hochgestellte Zahlen sowie newlines im Text vorhanden sind, welche wir nicht mit abspeichern wollen, werden diese mittels Regulären Ausdrücken ersetzt  
  - Fläche finden  
    -  Mit Beautifulsoup suchen wir den a-Tag mit dem Text "Fläche", um von dort aus über Eltern, Geschwister sowie Kind Elementen zu der gesuchten Fläche zu gelangen  
    - Auch hier werden hochgestellte Zahlen sowie newlines durch Reguläre Ausdrücke ersetzt
  - Amtssprachen finden  
    - Mit Beautifulsoup suchen wir den a-Tag mit dem Text "Amtssprachen", um von dort aus über Eltern, Geschwister sowie Kind Elementen zu den gesuchten Amtssprachen zu gelangen
    - Die gefundenen Tags mit den verschwiedenen Sprachen durchlaufen wir mit einer for-Schleife, um die Sprachen in einer Liste abzuspeichern  
- Öffnen der zuvor erstellten csv-Datei der Mitgliedsstaaten und URL's  
- Erstellen eines leeren Dictionarys als Datenstruktur, um die Mitgliedsstaaten und deren Attribute dort abzuspeichern  
- Über die csv-Datei iterieren, um die Ressource jedes Landes zu öffnen und die jeweiligen Daten im Dictionary "mitgliedsstaaten" abzuspeichern  
  - Die erste Zeile wird übersprungen, da diese die Überschriften enthält  
  - Für jeden aufgerufenen Mitgliedsstaat wird ein Dictionary erzeugt, indem die jeweiligen Attribute aus der Infobox abgespeichert werden  
  - Um das Dictionary des jeweiligen Mitgliedsstaates zu befüllen, werden die zuvor definierten Funktionen, mit dem Inhalt der jeweiligen Ressource als Parameter, aufgerufen  
  - Anschließend wird der Mitgliedsstaat mit zugehörigem Dictionary in dem Dictionary "mitgliedsstaaten" abgespeichert  

3. Teil 3: Das Dictionary in eine JSON-Datei schreiben:
- Die json-Datei wird im Write-Modus geöffnet/erstellt. Hierbei wird encoding utf-8 verwendet  
- Mittels der dump() Methode wird das Dictionary "mitgliedsstaaten" in die json-Datei geschrieben. Hierbei wird indent=4 gewählt, um die json-Datei leserlich zu gestalten und ensure-ascii=False gesetzt, damit in der json-Datei keine unicode Zeichen benutzt werden


4. Ausgesucht haben wir eine Liste der Mitgliedsstaaten der Vereinigten Nationen. Diese Liste listete sowohl die aktuellen als auch die ehemaligen Mitgliedsstaaten auf. Da es für uns nicht sinnvoll erschien die ehemaligen Mitgliedsstaaten mit in unsere Auswahl zu übernehmen, da dies Staaten sind die mitlerweile umbenannt wurden oder sich zusammengeschlossen haben und somit nicht mehr existieren, wurden nur die aktuellen Mitgliedsstaaten von uns ausgewertet.  
Bei der Auswahl der Liste hatten wir einige Mühe uns eine Liste auszusuchen, da so viele verschiedene interessante Listen existieren. Bei unserer ersten Idee die Friedensnobelpreisträger zu nehmen, stießen wir auf das Problem, dass die Wikipediaartikel teilweise sehr kurz waren und die Infoboxen kaum Inhalt beinhalteten. Aus diesem Grund entschieden wir uns dazu eine Liste zu nehmen, die auf verschiedene Länder verlinkt, da diese sehr gleichförmig dargestellt werden und jeweils gleichen Attribute in der Infobox besitzen.  
Ausgewählt haben wir dann die Liste der UN-Mitgliedstaaten, da die UN mit dem Gedanken zur Sicherung des Weltfriedens entstand. Demnach dient die UN gemäß ihrer Charta der Sicherung des Weltfriedens, der Einhaltung des Völkerrechts, dem Schutz der Menschenrechte und der Förderung der internationalen Zusammenarbeit (Quelle: https://de.wikipedia.org/wiki/Vereinte_Nationen).  
Mit dem Beitritt zur UN zeigen Staaten somit, dass sie sich diesen Zielen verpflichtent fühlen und ihre Wichtigkeit anerkennen.  
Wir wollen also mit dieser Liste diese Staaten darstellen und ihre wichtigsten Länderinformationen aufzeigen. Besonders interessant war für uns auch die Mehrsprachigkeit einer solchen weltweiten Organisation, weshalb wir die Amtssprachen der jeweiligen Länder in unsere Liste integriert haben.  
Außerdem hatten wir zuerst die englische Wikipedialiste zur Auswertung gewählt, sind dann aber auf die deutsche Wikipediaseite gewechselt, da hier die Formatierung der Infoboxen gleichmäßiger war. Bei der englischen Version unterschieden sich die html-Tags der Infobox je Land teilweise stark voneinander ab, sodass das Programm komplexer und unübersichtlicher geworden wäre.  
Für die Attribute "Hauptstadt", "Einwohnerzahl" und "Fläche", haben wir uns entschieden, da dies die wichtigsten Länderinformationen eines Landes sind. Desweiteren haben wir das Attribut "Amtssprachen" noch gewählt, da uns dies als wichtig für die Kommunikation zwischen den verschiedenen UN-Staaten erschien. 

