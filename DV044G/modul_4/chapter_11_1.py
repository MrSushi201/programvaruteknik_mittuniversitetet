# 11.1. Arbeta med moduler
"""
En modul är en Python-fil (med filändelsen .py)
som innehåller kod avsedd att importeras och återanvändas i andra filer.
Tekniskt sett är varje Python-skipt du skapar en modul.

---

Skapa och importera en modul:

Om du skapar filen adder.py i en projektmapp myproject/ med följande innehåll:
'''python
def add(x, y):
    return x + y
'''
Och sedan försöker anropa add(2, 2) direkt i filen main.py i samma mapp utan import
kastar Python ett NameError: name "add" is not defined.
För att komma åt funktionen måste modulen importeras med import adder.
I detta sammanhang kallas adder.py för den importerade modulen och main.py för den anropande modulen.

---

Namnområden (Namespaces):

Ett namnområde är en samling av (variabler, funktioner, och klasser).
Varje modul har sitt eget namnområde. Även när du har skrivit import adder i main.py, kastar ett direkt anrop av add(2, 2) fortfarande ett NameError.
Detta beror på att add ligger i modulen adder:s namnområde.
För att komma åt ett namn i en importerad modul måste du använda punknotering:
<module>.<name>

'''python
# main.py
import adder

value = adder.add(2, 2) # korrekt åtkomst via punknotering
print(value)
'''

- Regel för filnman
Modulens filnamn utgör dss namnområde vid import.
Därför måste filnamnet vara en giltig Python-identifierare (får endast innehålla bokstäver, siffror och understreck, och får inte börja med en siffra).
- Hela namnområdet importeras
När du använder import adder importeras hela modulens namnområde.
Om du senare lägger till funktionen double(x) i adder.py blir adder.double() direkt tillgänglig i main.py utan att importsatsen behöver ändras.

---

Varianter av import-satser:

Det finns tre huvudsakliga sätt att importera moduler på.

1. import <module> (standardsätt):
  - Funktion: importerar hela modulens namnområde under modulens eget namn
  - Användning: adder.add(2, 2)
  - Fördel: bevarar fullständig kontext och håller namnområden helt åtskilda
2. import <module> as <other_name> (alias / omdöpning):
  - Funktion: importerar modulens namnområde men döper om det i den anropande modulen
  - Exempel: import adder as a kräver att du anropar a.add(2, 2). Om du försöker anropa adder.add() kastas NameError eftersom det ursprungliga namnet inte längre finns i namnområdet
  - När det används: används när modulnamnet är väldigt långt eller om det krockar med ett befintligt namn i den anropande filen
3. from <module> import <name1>, <name2> (direktimport av specifika namn):
  - Funktion: importerar endast de angivna namnen direkt in i den anropande modulens lokala namnområde
  - Exempel: from adder import add gör att du kan anropa add(2, 2) direkt utan prefix
  - Fallgrop / Felmeddelande: om du försöker anropa adder.add() kastas NameError eftersom själva modulen adder inte importerats
  - Nackdel: du förlorar kontexten kring var koden kommer ifrån, och det finns en risk för namnkrockar i din fil

---

Analogi för namnområden och undantagsfall

Boken förklarar namnområden med en analogi om ID-nummer och landskoder.
Om alla människor på jorden krävde ett unikt ID-nummer blir det komplext.
Delar man istället upp ID-numren per land (t.ex. US-357 och GB-246), räcker det att ID-numret är unikt inom sitt eget land.
Landskoden fungerar som ett namnområde som grupperar namn, förhindrar krockar och ger kontext.

- Ett rimligt undantag för from ... import ...: modulen datetime i Pythons standardbibliotek innehåller en klass som också heter datetime.
Att skriva datetime.datetime(2020, 2, 2) blir lätte tjatigt.
Därför brukar man antingen skriva import datetime as dt (dt.datetime()) eller from datetime import datetime.
Eftersom klassen och modulen har exakt samma namn förloras ingen kontext

---

Inläsningskontroll med if __name__ == '__main__':

När Python kör en skriptfil sätts ett antal inbyggda specialvariabler innan koden exekveras.
En av dessa är __name__:

- När en fil körs direkt av användaren sätter Python __name__ == '__main__'
- När en fil importeras som en modul sätter Python __name__ till modulen filnamn (t.ex. 'adder')

Eftersom kod som ligger på toppnivå i en modul alltid exekveras när modulen importeras, 
använder man ett villkor för att förhindra att testkod eller huvudlogik körs vid import:

'''python
def main():
    print("Detta körs när skriptet startas direkt!")

if __name__ == '__main__':
    main()
'''

Detta gör att filen både kan köras som ett självständig skript och importeras säkert som en modul utan att oönskad kod körs automatiskt.
"""