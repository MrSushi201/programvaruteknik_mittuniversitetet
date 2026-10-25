# 9.6. Dictionaries - Store relationships in dictionaries
"""
En dictionary är en datastruktur som lagrar data i form av nyckel-värdepar.
Varje nyckel är en unik identifiering som pekar på ett värde.
Datastrukturen fungerar som en matematisk avbildning (map).

---

Skapa dictionaries:

1. Dictionaryliteral
Använder måsvingar {} och kolon : mellan nyckel och värde
Exampelvis
    capitals = {"California": "Saramento", "Texas": "Austin"}
2. Anrop till dict()
Kan skapas utifrån en sekvens av tvåelementstupler
Exampelvis
    dict([("California", "Sacremento"), ("Texas", "Austin")])
3. Tom dictionary
Skrivs som {} eller dict()
Exampelvis
    dict1 = {}
    dict2 = dict()
4. Ordning
Från och med Python 3.6/3.7 garanteras att nyckel-värdeparen bevarar den ordning som de sattes in i

---

Hämta och ändra värden:

- Hämta värde
Hakparentes med nyckeln returnerar värdet
Exampelvis
    capitals["Texas"] returnerar "Austin"
- Lägga till nytt par
Exampelvis
    dict["nyckel"] = värde
- Uppdatera befintligt värde
Tilldelning till en befintlig nyckel överskriver det gamla värdet
Exampelvis
    Om dict[nyckel1] = värde1 existerar
    dict[nyckel1] = värde2 ersätter då värde1
- Ta bort par
Nyckelordet del raderar ett par
Exampelvis
    del dict[nyckel] 

---

Felhantering och tillhörighetskontroll med in:

- Om du försöker hämta en nyckel som inte finns kastar Python KeyError
Exampelvis
    capitals["Arizona"]
- key in dictionary returnerar True om nyckeln finns
Exampelvis
    print("Texas" in capitals)
- Viktigt: operatorn in kontrollerar endast nycklar, inte värden. Utvärderingen "Sacremento" in capitals returnerar False
Exampelvis
    print("Austin" in capitals) ger False men
    print("Texas" in capitals) ger True

---

Iterera över dictionaries:

- En standard for-loop över en dictionary itererar över dess nycklar
Exampelvis
    for key in dict:
- Metoden .items() returnerar ett vy-objekt (dict_items) bestående av tupler med (key, value)
Exampelvis
    print(capitals.items())
- Tillåter direkt unpacking i loopen
Exampelvis
    for state, capital in capitals.items():

---

Krav på nycklar och värden (immutability)

- Nycklar: måste vara av en oföränderlig datatyp. Giltiga typer är heltal, flyttal, strängar, booleans och tupler
Försök att använda en föränderlig typ (som en lista) som nyckel kastar Python TypeError
- Värden: kan vara av vilken typ som helst, inklusive listor, tupler eller andra dictionries

---

Nästlade dictionaries

- Dictionaries kan innehålla andra dictionaries som värden (inte nycklar!)
- Åtkomst sker via kedjad hakparentes (dubbel "indexering")

---
"""

# Övning

# 1. Skapa en tom dictionary captains
captains = {}

# 2. Lägg till data i captains
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3. Skriv 2 if-satser som kontrollerar om "Enterprise" och "Discover" existerar som nycklar i dictionaryn
# Tilldela "unknown" om en nyckel existerar ej
if "Enterprise" in captains:
    pass
else:
    captains["Enterprise"] = "unknown"

print(captains["Enterprise"])

if "Discovery" not in captains:
    captains["Discovery"] = "unknown"
else:
    pass

print(captains["Discovery"])

# 4. Skriv en for-loop som visar fartyg och kapten i dictionaryn
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

# 5. Ta bort "Discovery" från dictionaryn
del captains["Discovery"]