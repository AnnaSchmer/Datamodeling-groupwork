Assignment 2
============

Exercise 1
----------

**Dokumentation zu "Exercise01-programm.py":**

1. Erstellen einer Liste aller Charaktere aus der Spalte "character":  
- Öffnen der bereinigten Datei und auslesen aller Zeilen, welche in einer Liste "lines" gespeichert werden.  
- Erstellen einer leeren Liste "characters".  
- Anschließend über die Liste "lines" iterieren und dabei jeweils das Listen Element (also eine Zeile) am Tabulator aufsplitten (da die csv-Datei Tabulatorgetrennt war). Es entsteht somit von jeder Zeile eine Liste aus den Spaltenelementen. Hiervon wird nun jeweils der Eintrag mit Index 1 (da Charaktere in der zweiten Spalte stehen)in die zuvor neu erstellte Liste "characters" hinzugefügt.  

2. Erstellung eines Dictionaries mit Namen als Schlüssel und der zugehörigen Anzahl als Value:  
- Erstellen eines leeren Dictionaries.  
- Anschließend über die Liste "characters" mittels Index von 1 bis Länge der Liste iterieren. Man beginnt hier bei 1, da der Index 0 die Spaltenüberschrift ist. Ist der jeweilige Schlüssel characters[i] schon im Dictionary vorhanden, wird auf den bisherigen Value eins drauf addiert. Ist dieser Schlüssel noch nicht vorhanden wird er neu hinzugefügt und der zugehörige Value auf 1 gesetzt, da 0+1=1.  

3. Erstellen einer csv-Datei mit den Namen und der zugehörigen Anzahl:  
- Öffnen einer neuen csv-Datei im Append-Modus  
- Nun wird über das Dictionary iteriert und somit in jede Zeile jeweils der Name (Schlüssel des Dictionaries) und die Anzahl (Value des Dictionaries) geschrieben.  

4. Namen der Charaktere aus der Dialog-Spalte zählen und in einer csv-Datei abspeichern:    
- Erstellen einer leeren Liste "dialogs" in der die einzelnen Elemente die Zeilen der Dialog-Spalte sein sollen.  
- Dazu analog wie in 1. über die Liste "lines" iterieren mit der Änderung, dass wir nun jeweils den Eintrag mit Index 2 (da Dialog in Spalte 3) in die zuvor neu erstellte Liste "dialogs" hinzufügen.  
- Erstellen einer leeren Liste "woerterDialog" in der die einzelnen Elemente alle Wörter der gesamten Dialog-Spalte sein sollen.  
- Dazu wird über die Liste "dialogs" iteriert und die einzelnen Elemente (einzelne Zeilen) an einem Leerzeichen gesplittet. Es entsteht somit von jeder Zeile eine Liste aus den Wörtern. Über diese einzelnen Listen wird jeweils zusätzlich iteriert, um von den einzelnen Wörtern die Satzzeichen zu entfernen und diese anschleißend in die neue Liste "woerterDialog" hinzuzufügen.  
- Erstellen einer leeren Liste "charactersDialog" in der die Charakternamen aus den Dialogen abgespeichert werden. 
- Dazu benutzen wir eine verschachtelte for-Schleife, indem wir über die Wörter der Liste "woerterDialog" und die Namen der Liste "characters" aus 1. iterieren um diese Vergleichen zu können. Wenn das Wort aus "woerterDialog" umgewandelt in Großbuchstaben gleich einem Namen aus "characters" ist, wird dieses in Großbuchstaben zur Liste "charactersDialog" hinzugefügt.
- Erstellen eines leeren Dictionaries "characterCountsDialog", welches als Schlüssel die Namen und als Value die zugehörige Anzahl enthalten soll.  
- Dazu wird über die Liste "charactersDialog" iteriert. Ist der jeweilige Schlüssel characterCountsDialog[i] schon im Dictionary vorhanden, wird auf den bisherigen Value eins drauf addiert. Ist dieser Schlüssel noch nicht vorhanden wird er neu hinzugefügt und der zugehörige Value auf 1 gesetzt, da 0+1=1.  
- Die zugehörige csv-Datei wird analog wie in 3. erstellt.

