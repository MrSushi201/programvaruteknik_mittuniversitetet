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

Träd är en samling element som är organiserade i en hierarkisk struktur (likt ett organisationsschema). Noden längst upp i trädet kallas rotnod. Noder närmast över kallas föräldrar, noder närmast under kallas barn, och noder med samma föräldrar kallas syskon. En gren med underliggande noder kallas för delträd. Avslutande noder längst ner som saknar barn kallas terminalnoder. Det största antalet noder i en väg från roten ner till ett löv.

Binärträd är en specifik trädstruktur där varje nod har maximalt två barn (ett vänster barn och ett höger barn).

---

### 8.1.1. Frågor

1. Vad är den huvudsakliga skillnaden mellan en array och en struct/record när det gäller elementens datatyper och hur de nås? Svar:

- Data lagras i en följd i arrayer medan i struct/record lagras data