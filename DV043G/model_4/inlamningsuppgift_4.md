# Teoretisk del

---

## 1. Relationsdatabas

Beskriv hur en relationsdatabas är uppbyggd och hur man använder den. Ta med begreppen schema och subschema i din beskrivning av relationsdatabasen.

Innan vi djupdyker i relationsdatabasen (som egentligen är en databasmodell av många andra) så kan det vara bra att titta på vad ett databassystem är, och dess byggstenar som till exempel schema och subschema/underschema.

Ett databassystem och databashanterare (Database Management System, eller DBMS) fungerar som ett abstraherande lager mellan applikationen och den fysiska lagringen. Ett schema i ett databassystem fungerar som en mall eller en beskrivning för "hela" databasens struktur [1]. Det täcker entiteter, deras attribut, datatyper, länkarna (relationerna) mellan dem och mycket mer [1]. Ett subschema/underschema är ett ytterligare lager i systemet och fungerar som en avgränsad beskrivning/vy för enbart "en del" av databasen, som är relevant för en specifik målgrupp eller/och ett specifikt syfte [1]. Subscheman tillämpas för att förhindra att obehöriga ska få tillgång till all information (alla ska inte se eller ha tillgång till allting (till och med databasadministratör i vissa fall)), och för att uppnå dataoberoende [1].  

Med det sagt, relationsdatabas använder en specifik modell (också ett abstrakt verktyg i sig själv som dess byggstenar som finns förklarats nedan) som kallas relationsmodellen. I modellen visualiseras och organiseras data i tvådimensionella tabeller som består av rader och kolumner [1], och modellen innehåller specifika begrepp:

- Relation
- Tupel
- Attribut
- Kopplingsattribut

Relation är tabellstrukturen som består av rader och kolumner [1].
Tupel är en enskild rad i relationen som innehåller data för en specifik entitet [1].
Attribut är en kolumn i relationen där varje cell beskriver en viss egenskap hos entiteten [1].
Kopplingsattribut är ett gemensamt attribut som kopplar samman olika relationer med varandra [1].

Ett exempel på två relationer/tabeller/vyer som kan kopplas samman med ett kopplingsattribut (Vehicle Identification Number, eller VIN):

| BilId | VIN | Märke | Model | ModelÅr |
| --- | --- | --- | --- | --- |
| 1 | ABCD1234 | Vovvo | AB60 | 2027 |
| 2 | ABCD1235 | Polester | 99 | 2027 |

| PersonId | VIN | Namn | Mejl | Land |
| --- | --- | --- | --- | --- |
| 1 | ABCD1234 | Santi Taweesamarn | santi@taweesamarn.com | USA |
| 2 | ABCD1235 | Johan Andersson | johan@andersson.com | Kina |

Som ett exempel så skulle man teoretiskt och praktiskt kunna koppla ett fordon till en person med hjälp av kopplingsattributet "VIN" som fungerar som ett unikt identifikationsnummer. Men då denna information innehåller känsliga personuppgifter så ska det med största sannolikhet inte vara tillgängligt till många målgrupper.

Sedan, rent praktiskt, i många fall används Structured Query Language (SQL) av en användare för att kommunicera/interagera med ett databassystem [1]. De tre grundläggande relationella operationerna som SQL bygger på är [1]:

- SELECT, väljer ut specifika rader (tupler)
- PROJECT, väljer ut specifika kolumner (attribut)
- JOIN, slår samman två tabeller (relationer) med hjälp av ett kopplingsattribut

---

## 2. Datastrukturer

Gör en översikt över några vanliga datastrukturer. Beskriv med ord och figurer. Ange lämpligt användning för respektive struktur. Följande strukturer ska vara med i beskrivningen:

- Pekare
- Array
- Länkad lista
- Träd

De ovanstående datastrukturerna nämns i kursmaterialet.

Först, en pekare är en variabel (identifierare) eller minnesplats i datorns minne som innehåller en adress till en annan minnescell där data ligger lagrat [1, s. 445], [2, s. 2]. Eftersom en typ av information finns lagrad i en pekare, skulle man också kunna säga att en pekare i sig är en datastruktur [1, s. 445]. Den implementeras därför i samband med andra (dynamiska) datastrukturer. Pekare används för dynamisk minnesallokering/datastruktur och gör det möjligt att sortera och flytta om data genom att enbart ändra adresser istället för att flytta själva datat i minnet [1, s. 445]. Visuellt kan pekare se ut så här:
[ adress1 ] -> [ "data1" ], där adress1 är minnesadressen till datat "data1".

I sin enklaste form så är en array en datastruktur där elementen lagras i en kontinuerlig följd i minnet (och antingen radvis eller kolumnvis vid två- eller flerdimensionella arrayer), vilket betyder att elementen ligger precis bredvid varandra i datorns minne [2, s. 2]. Det är också viktigt att nämna att varje element kan identifieras och nås med index [1, s. 438], [2, s. 2] från 0 till (N - 1) där N är arrayens storlek. Arrayer kan användas om datatypen för alla element är av samma typ och att det är konstant storlek per element [1, s. 438]. Varje element/minnescell i en array tar upp exakt lika mycket minnesutrymme eftersom alla element är av samma datatyp. Exempel på arrayer är [0, 1, 2, 3, ..., N] där N är ett heltal eller ["a", "b", "c", ..., "ä"] där alla element är små bokstäver av datatypen sträng.

En länkad lista är en dynamisk datastruktur vars storlek och datatyper kan variera - med andra ord, listan kan växa eller krympa över tid då element läggs till eller tas bort []. Viktig egenskap hos en länkad lista (men även för andra dynamiska datastrukturer) är att den tar inte mer minnesutrymme än vad den exakt behöver för de tänkta elementen []. En länkad lista byggs upp av följande komponenter:

- Huvudpekare, en pekare som lagrar minnesadressen till listans första nod
- Nod, där varje element i listan kallas en nod och består ytterligare av:
  - Data, det faktiska datat som finns lagrat i noden
  - Pekare, en minnesplats som innehåller adressen till nästa nod i sekvensen
- Slutindikator (NIL eller None), den sista nodens pekare sätts till ett nollvärde för att markera att listan är slut

Visuellt kan en länkad lista se ut så här:

[ huvudpekare ] -> [ data1 / pekare1 ] -> [ data2 / pekare2 ] -> ... [ dataN / NIL ].

Om en länkad lista är tom från början, det vill säga att den inte innehåller något element alls, så sätts/pekar huvudpekaren till nollvärdet NIL / None [].

En länkad lista används när antalet element inte kan förutbestämmas och ändras ofta, samt som en grundläggande dynamisk struktur för att implementera stackar och köer [].

Ett träd är en datastruktur som organiserar/lagrar data på ett sätt som liknar, ett träd... Konkreta exempel på trädstrukturen är ett organisationsschema eller ett familjträd. För att förklara hur ett träd som datastruktur fungerar samt definiera viktiga begrepp som används i samband med träd så kan vi använda oss av följande figur som illustrerar ett binärträd:

                                            [ Nod1 | pekare2 | pekare3 ]  (Rotnod) <--- Rotpekare
                                            /                           \
                [Nod2 | pekare3 | pekare 4 ]                             [ Nod5 | pekare5 | pekare6 ]
                /                           \                            /                          \
   [ Nod3 | NIL ]                           [ Nod4 | NIL ]  [ Nod6 | NIL ]                          [ Nod7 | NIL ]   (Lövnod)  

Varje position i ett träd kallas för nod, och varje nod består egentligen av återigen:

- Data, det faktiska datat som finns lagrat i noden, och
- Pekare, en eller flera minnesplatser som innehåller adresser till andra noder längst trädet

---

## 3. Filer

Hur fungerar indexerade filer respektive hash-filer? Vilka fördelar och nackdelar finns det med respektive sätt att hantera data i filer?

---

## 4. Kö

En kö har implementerats i cirkulär form, se figuren nedan. Rita figurer som visar köns läge steg-för-steg efter följande operationer:

1. Bokstäver G och R har ställts i kön
2. De tre boktäverna har tagits bort ur kön
3. D och P har ställts i kön

Glöm inte att sätta ut huvudpekare och svanspekare i varje figur!

|     |  U  |  F  |  K  |  L  |  A  |     |     |
         H                             T

---
