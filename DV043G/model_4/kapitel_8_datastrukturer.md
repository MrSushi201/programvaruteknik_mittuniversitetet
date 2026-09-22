# 8. Datastrukturer

---

## 8.1. Grundläggande datastrukturer

Kapitlet behandlas de tre mest fundamentala datastrukturerna för att samla och organisera data i program:

- Arrayer / aggregat
- Listor / stackar / köer
- Träd

Arrayer (vektorer och fält) är rektangulära block av data där alla element är av samma datatyp.
Endimensionell array är en enkel rad av element där varje position identifieras med ett enskilt index (oftast med start på 0). En lista i ett Pythonprogram är en endimensionell array.
Tvådimensionell array består av rader och kolumner där positioner identifieras med par av index (rad, kolumn).
Arrayer har en statisk (konstant) storlek som bestäms vid deklarationen och lagras kontinuerligt (i en följd) i datorns minnne. För tvådimensionella arrayer kan elementen lagras antingen radvis (row major order) eller kolumnvis (column major order).
Aggregat (poster / struct / record) är block av data där fälten till skillnad från en array kan vara av olika datatyper och storlekar. Fälten identifieras och nås via fältnamn (t.ex. Employee.Age eller person1.name) istället för numeriska index.

En lista består av en sekventiellt ordnad samling av element. Början av listan kallas huvud och slutet kallas svans.
En stack (Last-In, First-Out) är en begränsad lista där tillägg och borttagningar enbart få göras vid huvudet. Slutet kallas för botten. Att lägga till ett element kallas att pusha och a ta bort kallas att poppa. Användningsområden är backtracking (ångra-funktioner), beräkning av aritmetiska uttryck samt hantering av funktionsanrop och rekursion.
En kö (First-In, First-Out) är en begränsad lista där element läggs till slutet och tas bort i början. Användningsområden är system där element betjänas i ankomstordning (t.ex. en skrivarkö). Problemet med array-lagring är om en kö lagras i en vanlig array flyttar sig datat genom arrayen när element tas bort i framkanten och läggs till i bakkanten. Detta gör att utrymmet utnyttjas dåligt. Lösningen är att använda en cirkulär kö eller en länkad lista.
Datorn kan organisera en struct i minnescellerna på två olika sätt beroende på om fältens storlek är känd i förväg eller dynamisk.

- Kontinuerligt minnesblock (för fält med fast storlek)
- Separata minnesplatser länkade med pekare (för fält med dynamisk storlek)

Om varje fält har en fast och känd storlek lagras hela structen i ett enda sammanhängande block av minnesceller.
Om fältet "Name" tar 25 minnesceller, "Age" tar 1 cell och "SkillRating" tar 1 cell, avsätter datorn ett sammanhängande block på totalt 27 celler i minnet. Om structen start på minesadress "x", hittar kompilatorn ett specifikt fält genom en förskjutning (offset) från startadressen. Fältet "Age" återfinns då direkt på minnesadress "x + 25".
Om fälten har dynamisk storlek (kan ändra storlek under körning) lagras fälten istället på separata platser i minnet.
Ett block reserveras då för pekare (minnesadresser), där varje pekare pekar ut var respektive fält faktiskt ligger i minnet.
Om ett enskilt fält behöver växa flyttas enbart det fältet till en ny, större minnesyta och dess pekare uppdateras, utan att resten av structen behöver flyttas eller arrangeras om.
En struct lagrar data, men saknar funktioner för att manipulera datat.
I C++ vidareutvecklas struct-begreppet till klasser (class). En klass samlar både data (attribut) och operationer/metoder.

Träd är en samling element som är organiserade i en hierarkisk struktur (likt ett organisationsschema). Noden längst upp i trädet kallas rotnod. Noder närmast över kallas föräldrar, noder närmast under kallas barn, och noder med samma föräldrar kallas syskon. En gren med underliggande noder kallas för delträd. Avslutande noder längst ner som saknar barn kallas terminalnoder. Det största antalet noder i en väg från roten ner till ett löv.
Binärträd är en specifik trädstruktur där varje nod har maximalt två barn (ett vänster barn och ett höger barn).

---

## 8.2. Relatereade begrepp

Avsnitt behandlar de tre teoretiska grundpelarna för alla datastrukturer:

1. Abstraktion
2. Statiska kontra dynamiska datastrukturer
3. Pekare

Datorns primärminne (RAM) är i grunden enbart organiserat som en lång sekvens av numrerade adresserbara minnesceller (bytes). Minnet förstår inte i sig självt vad en matris, en lista eller ett träd är.
För att programmerare och användare ska slippa tänka i fysiska minnesadresser och byte-mönster skapas datastrukturer som abstrakta verktyg.
Abstration innebär att man aner vad som ska utföras med datastrukturen utan att i detalj behöva bry sig om hur det utförs nere i minnescellerna.
Användaren som drar nytta av abstraktionen kan vara en människa (via ett användargränssnitt), en klient över ett nätverk, eller en annan kodmodul i programmet.
Lektionsmaterialet framhåller att datastrukturer hanteras som abstrakta verktyg genom att man definierar en uppsättning funktioner för dem.

En avgörande skillnad vid konstruktion av datastrukturer är om deras storlek och form är fast eller om den förändras över tid.

| Egenskap | Statisk datastruktur | Dynamisk datastruktur |
| --- | --- | --- |
| Storlek | Konstant/fast storlek som bestäms vid deklarationen | Kan växa och krympa automatiskt under körning |
| Exempel | En standard-aray med 100 platser eller ett schackbräde | Länkade listor, binära träd, eller ett dominomönster |
| Minneshantering | Enkel. Data lagras oftast i ett sammanhängande minnesblock | Komplex. Kräver dynamisk minnesallokering och hantering av pekare |
| Utmaningar | Kan bli full (begränsat utrymme) eller slösa minne om den inte fylls | Kräver hantering av tillägg, borttagning och frigörande av minne |

Eftersom varje minnescell har en unik numerisk adress, kan själva adressen kodas och lagras som data i en annan minnescell. En pekare är en variabel eller minnesyta som lagrar en sådan minnesadress.
Pekaren pekar ut var ett specifikt dataelement faktiskt befinner sig i primärminnet.
Ett klassiskt exempel på en pekare på maskinnivå är CPUns program counter eller instruktionspekare, som innehåller adressen till nästa instruktion som ska exekveras.
I programmeringsspråk används pekare för att bygga ihop nätverk av data (till exempel länkade listor eller träd) där relaterade element pekar på varandra.
För att ta bort noden "Olle" i en länkad lista ändras pekaren från "Eva" så att den pekar direkt på "Per". Därefter frigörs den minnesplats som "Olle" upptop.
För att sätta in "Stefan" mellan "Eva" och "Olle" skapas först ett nytt listelement för "Stefan", varefter "Eva"s pakare sätts till "Stefan" och "Stefan"s pekare till "Olle".
För att sortera en länkad list behöver man inte flytta själva datat i minnet - man flyttar enbart om pekarna, vilket gör operationen mycket snabb och effektiv.

Lektionsmaterialet knyter ihop abstraktionskonceptet med utvecklingen av egentillverkade datatyper.

- Struct (C) / Record (Pascal) / Post som samlar relaterade fält av olika datatyper i en och samma variabel (till exempel person1.name, person1.shoeNr)
- En struct lagrar enbart data men saknar inbyggda metoder för att manipulera datat

- Klasser (Class) och Objekt (OOP)
- I C++ och moderna språk byggs struct-begreppet ut till klasser
- En klass samlar både data (attribut) och operationer (metoder)
- Genom enkapsulering döljs interna lagrinsdetaljer så att datastrukturen kan användas som ett rent abstrakt verktyg

---

