# Laboration 3 - Ett smakprov på programmering

---

## Syfte

Programmering är en viktig del av datavetenskap. I den här laborationen får du ett första smakprov på programmering och algoritmiskt tänkande.

Tanken är att studenten ska använda Python för att prova några grundläggande idéer och för att se hur en algoritm kan få en dator att utföra en uppgift.

---

## Efter laborationen ska studenten ha fått en första inblick i

- Vad ett program och en algoritm är
- Hur instruktioner utförs i en bestämd ordning (sekvens)
- Hur ett program kan välja mellan olika alternativ (selektion)
- Hur instruktioner kan upprepas (iteration)
- Hur en enkel algoritm kan beskrivas med pseudokod och sedan uttryckas i Python

---

## Deluppgift 1 - Prova ett program (sekvens)

´´´python
namn = input('Vad heter du? ')
print('Hej', namn)
print('Välkommen till programmering!')
´´´

### Gör följande

1. Skriv in programmet och kör det
2. Ändra välkomstmeddelandet till något annat
3. Lägg till ytterligare en print() som skriver ut en egen text.
4. Kör programmet igen

´´´python
namn = input('Vad heter du? ')
print('Hej', namn)
print('Hur är det med dig idag?')
print('Jag mår jättebra!')
´´´

### Fundera och besvara

Instruktionerna utförs uppifrån och ned. Vad händer om du flyttar den sista print()-raden så att den ligger först i programmet?

Standardprogram utförs uppifrån och ned (sekventiellt). Det ursprungliga programmet ser ut så här (presentationsmässigt):

Vad heter du?                   # Tilldelningen av ett värde med ett variabelnamn "namn" sker här.
Hej, Santi                      # Antag att det tilldelade värdet är 'Santi'
Hur är det med dig idag?        # Den omskrivna print()-raden
Jag mår jättebra!               # Den nya print()-raden

Om den sista print()-raden flyttats och är nu först i programmet, så kommer den att exekveras först vid körning. Detta är resultatet (representationsmässigt):

Jag mår jättebra!               # Den nya print()-raden
Vad heter du?                   # Tilldelningen av ett värde med ett variabelnamn "namn" sker här.
Hej, Santi                      # Antag att det tilldelade värdet är 'Santi'
Hur är det med dig idag?        # Den nya print()-raden

---

## Deluppgift 2 - Låta programmet välja (selektion)

Ett program kan utföra olika instruktioner beroende på ett villkor. Vi vill skapa ett program som avgör om ett heltal är udda eller jämnt. Algoritmen kan beskrivas med pseudokod:

´´´pseudokod
LÄS tal
OM resten när tal divideras med 2 är 0
    SKRIV 'Talet är jämnt'
ANNARS
    SKRIV 'Talet är udda'
´´´

I Python kan samma idé uttryckas så här:

´´´python
tal = int(input('Skriv ett heltal: '))
if tal % 2 == 0:
    print('Talet är jämnt')
else:
    print('Talet är udda')
´´´

### Gör följande

1. Kör programmet
2. Prova med ett jämnt och ett udda tal
3. Prova även med 0 och ett negativt tal

Operatorn & ger resten vid heltalsdivision

### Fundera och besvara

Vilken del av Pythonprogrammet motsvarar OM och ANNARS i pseudokoden?

if-satsen i Pythonprogrammet motsvarar OM i pseudokoden, och else-satsen motsvarar ANNARS i pseudokoden.

---

## Delupgift 3 - Upprepa instruktioner (iteration)

En av datorns styrkor är att den kan upprepa samma instruktion många gånger. Vi vill skriva ut 'Hello World' fyra gånger.

´´´pseudokod
UPPREPA 4 GÅNGER
    SKRIV 'Hello World'
´´´

I Python:

´´´python
for i in range(4):
    print('Hello World')
´´´

### Gör följande

1. Kör programmet
2. Ändra det så att texten skrivs ut 10 gånger
3. Ändra texten till något annat

Prova därefter:

´´´python
for i in range(10):
    print(i)
´´´

### Fundera och besvara

Vad tror du att range(10) gör?

range(10) i Python används för att skapa ett range-objekt (eller en sekvens/talserie) med 10 element/heltal.
Viktigt att veta är att just range(10) räknar ALLTID från 0 och 10 tal framåt. Det vill säga, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (och inte 10).

---

## Delupgift 4 - Från algoritm till program

Nu ska du själv göra ett litet program utifrån en algoritm. Euklides algoritm är en mycket gammal algoritm för att hitta den största gemensamma delaren för två heltal. Exempelvis är den största gemensamma delaren till 48 och 18 talet 6. Algoritmen kan beskrivas med pseudokod:

´´´pseudokod
LÄS a
LÄS b
SÅ LÄNGE b inte är 0
    rest <- a % b
    a <- b
    b < rest
SKRIV a
´´´

### Gör följande

Översätt pseudokoden till ett Pythonprogram. Du kommer bland annat att behöva:

a = int(input('Skriv första talet: '))
b = int(input('Skriv andra talet: '))

och en upprepning som börjar:

while b != 0:

Resten av programmet skriver du själv med pseudokoden som hjälp.

Testa programmet med:

- 48 och 18
- 20 och 5
- 17 och 7

Kontrollera att resultaten verkar rimliga.

### Fundera och besvara

Jämför pseudokoden med Pythonprogrammet. Vilka delar liknar varandra? Vad behöver uttryckas mer exakt när algoritmen skrivs som Python?

Logikmässigt så liknar pseudokoden och Pythongrammet väldigt mycket. Men programmering kräver noggrannhet/absoluthet/entydighet, det vill säga att det inte får finnas rum för tolkning eller gissning.

Till exempel, pseudokoden specifierar inte vilken datatyp a och b är. Men vi vet att denna algoritm innehåller matematiska beräkningar, och därför måste a och b vara uttryckta som heltal, därav användning av int()-funktioner som översätter/konverterar strängar från input()-funktinoner till heltal.

a = int(input('Skriv första talet: '))
b = int(input('Skriv andra talet: '))

while b != 0:
    rest = a % b
    a = b
    b = rest

print(a)

Vid a lika med 48 och b lika med 18 blir den största gemensamma delaren 6.
Vid a lika med 20 och b lika med 5 blir den största gemensamma delaren 5.
Vid a lika med 17 och b lika med 7 blir den största gemensamma delaren 1.

En algoritm är en beskrivning och en idé om hur en viss uppgift ska utföras, medan ett program är en konkret tolkning av den algoritmen. Ett program kan därför aldrig bli bättre än den algoritm som beskriver det. Om algoritmen är ofullständig och innehåller fel eller luckor, kommer programmet också att ärva dessa brister. Om man däremot gör justeringar direkt i programmet för att fixa algoritmens fel, representerar inte längre programmet den ursprungliga algoritmen utan man har nu förändrat algoritmen under implementeringen.
