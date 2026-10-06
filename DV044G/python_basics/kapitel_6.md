# 6. Funktioner och loopar

Kapitel 6 täcker två av de viktigaste byggstenarna inom programmering: hur du skapar egna återanvändbara funktioner och hur de upprepar kod med hjälp av loopar.

## 6.1 Vad är en funktion egentligen?

Funktioner är värden. I Python är funktioner värden som kan tilldelas variabler. Om du råkar skriva över ett inbyggt funktionsnamn (till exempel len = "text"), förlorar du åtkomsten till funktionen tills du använder nyckelordet "del" för att ta bort din egen variabelkoppling (del len).

```python
len # <built-in function len>
type(len) # <class 'builtin_function_or_method'>
len = "I´m not the len you´re looking for."
len # "I´m not the len you´re looking for."
type(len) # <class 'str'>
del len # Delete the len = "I´m not the len you´re looking for."
len # <built-in function len>
```

Exekvering i tre steg. När en funktion körs anropas den med argument, funktionskroppen utför sin uppgift, och slutligen returneras ett värde som ersätter själva anropet.

```python
# Typing just the name does not execute the function
len # <built in function len>

# Use parentheses to call the function
len()
"""
Traceback (most recent call last):
    File "<pyshell#3>", line 1, in <module>
        len()
TypeError: len() takes exactly one argument (0 given)
"""
num_letters = len("Four") # Först, len() anropas med argument "Four". Lägnden av "Four" kalkyleras och returneras ett värde som tilldelas ett variabelnamn "num_letters"
```

Sidoeffekter vs. returvärden. När en funktion förändrar något utanför sig själv har den en sidoeffekt. Funktionen print() visar exempelvis text i skalet som en sidoeffekt, men dessa faktiska returvärde är None (av typen NoneType).

## 6.2 Skriva egna funktioner

- Anatomi
- Parametrar vs Argument
- Indentering och PEP 8
- Returvärden
- Docstrings

En funktion består av en funktionssignatur (till exempel def funktion_namn(parameter):) och en funktionskropp.

```python
def multiply(x, y):
    product = x * y
    return product
```

En parameter är platshållaren i signaturen, medan ett argument är det faktiska värdet som skickas med vid anropet.

Alla rader i funktionskroppen måste indenteras exakt lika mycket; PEP 8 rekommenderar fyra mellanslag.

Nyckelordet "return" avslutar funktionen och skickar tillbaka ett resultat. Om inget "return"-uttalande finns returnerar funktionen automatiskt "None".

Docstrings utgör av tre-citerad sträng (""" ... """) längst upp i funktionskroppen används för att dokumentera funktionen och kan läas med hjälpfunktionen "help()".

## 6.4 Loopar - upprepa kod

- while-loopar
- for-loopar
- range()
- Nästlade loopar

while-loopar upprepar en kodlänk så länge ett testvillkor utvärderas till True. Om villkoret aldrig blir falskt uppstår en oändlig loop (som kan avbrytas i IDLE med Ctrl + C).

```python
n = 1
while n < 5:
    print(n)
    n = n + 1

while n < 5:
    print(n)

num = float(input("Enter a positive number: "))
while num <= 0:
    print("That is not a positive number!")
    num = float(input("Enter a positive number: "))
```

for-loopar exekverar koden en gång för varje element i en samling eller sekvens. Att använda for-loopar för att gå igenom samlingar är mer koncist, lättläst och anses mer "Pythonic" än while-loopar.

```python
for letter in "Python":
    print(letter)

word = "Python"
index = 0

while index < len(word):
    print(word[index])
    index = index + 1
```

range()-funktionen genererar talsekvenser, till exempel range(3) för 0, 1, 2 eller range (10, 20) för 10 till 19.

```python
for n in range(3):
    print("Python")

for n in range(10, 20):
    print(n * n)
```

Nästlade loopar är loopar inuti andra loopar kallas nästlade och ökar antal exekveringssteg och kodens komplexitet.

```python
amount = float(input("Enter an amount: "))
for num_people in range(2, 6):
    print(f"{num_people} people: ${amount / num_people:,.2} each")

for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")
```

## 6.5 Förstå räckvidd (Scope) och LEGB-regeln

- Scope avgör var variabler och namn är tillgängliga i koden
- LEGB-regeln, beskriver ordningen som Python söker efter ett variabelnamn:
  - L (Local) - Den lokala räckvidden inuti den aktuella funktionen
  - E (Enclosing) - Omslutande räckvidd i nästlade funktioner
  - G (Global) - Den översta räckvidden i skiptet
  - B (Built-in) - Pythons inbyggda funktioner och nyckelord (som "len" och "abs")
- Nyckelordet "global" kan tvinga Python att ändra en variabel i den globala räckvidden, men detta rekommenderas generellt inte

---

## 6.6 Introduktion till pseudokod

Pseudokod är ett sätt att beskriva vad ett program eller en algoritm ska göra utan att använda syntaxen i ett riktigt programmeringsspråk. I stället används enkla instruktioner som beskriver programmets logik på ett övergripande sätt.

Pseudokod hjälper dig att fokusera på vad som ska hända än hur det ska implementeras i exempelvis Python. Genom att beskriva lösningen steg för steg blir det lättare att planera, förstå, och diskutera ett programs uppbyggnad inann själva kodskrivandet påbörjas.

Pseudokod är ett bra sätt att:

- Planera programmets logik innan du börjar koda
- Förstå algoritmer och arbetet strukturerat med problemlösning
- Undvika att fastna i detaljre som syntax och formatering
- Strukturera idéer och tankar på ett sätt som är lätt att förstå för både dig själv och andra

I den här kursen används pseudokod som ett komplement till kravspecifikationer och kodskelett i laborationerna. Pseudokoden beskriver vanligtvis programmets övergripande struktur och flöde, medan detaljerna framgår av laborationsbeskrivningen. Du behöver inte skriva egen pseudokod i kursen, men du sk som sagt kunna läsa, förstå, och tillsammans med laborationsbeskrivningen, omsätta den till fungerade Python-kod.

---
