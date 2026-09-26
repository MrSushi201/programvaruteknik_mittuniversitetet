# Teoretisk del

---

## 1. Relationsdatabas

Beskriv hur en relationsdatabas är uppbyggd och hur man använder den. Ta med begreppen schema och subschema i din beskrivning av relationsdatabasen.

Relationsdatabas använder sig av en specifik modell (ett abstrakt verktyg i sig själv, som dess byggstenarna som finns förklarats nedan) som kallas relationsmodellen. I modellen visualiseras och organiseras data i tvådimensionella tabeller (arrayer) som består av rader och kolumner, och modellen använder specifika terminologi:

- Relation
- Tupel
- Attribut
- Kopplingsattribut

Relation är tabellstrukturen som består av rader och kolumner [1].
Tupel är en enskild rad i relationen som innehåller data för en specifik entitet [1].
Attribut är en kolumn i relationen där varje cell beskriver en viss egenskap hos entiteten [1].
Kopplingsattribut är en gemensam attribut som kopplar samman olika relationer med varandra [1].

Exempelvis på två relationer som kan kopplas samman med en kopplingsattribut:

| BilId | VIN | Märke | Model | ModelÅr |
| --- | --- | --- | --- | --- |
| 1 | ABCD1234 | Vovvo | AB60 | 2027 |
| 2 | ABCD1235 | Polester | 99 | 2027 |

| PersonId | VIN | Namn | Mejl |
| --- | --- | --- | --- |
| 1 | ABCD1234 | Santi Taweesamarn | santi@taweesamarn.com |
| 2 | ABCD1235 | Johan Andersson | johan@andersson.com |

Ovan kan man se två relationer/tabeller/subscheman.

---

## 2. Datastrukturer

Gör en översikt över några vanliga datastrukturer. Beskriv med ord och figurer. Ange lämpligt användning för respektive struktur. Följande strukturer ska vara med i beskrivningen:

- Pekare
- Array
- Länkad lista
- Träd

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
