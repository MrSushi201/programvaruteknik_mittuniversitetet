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
Abstraktion innebär att man aner vad som ska utföras med datastrukturen utan att i detalj behöva bry sig om hur det utförs nere i minnescellerna.
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

### 8.2.1. Frågor

1. På vilket sätt är datastrukturer som arrayer, listor, stackar, köer, och träd abstraktioner? Data i datorns primärminne lagras i grunden i en lång sekvens av individuellt adresserbara minnesceller. Datastrukturer som arrayer, listor, stackar, köer och träd är abstrakta verktyg (simulerade modeller). De skapas för att skärma av användaren/programmeraren från de tekniska detaljerna i det fysiska minnet och låta oss hantera information på ett mer logiskt och bekvämt sätt

2. Beskriv en tillämpning där du förväntar att en statisk datastruktur används. Beskriv sedan en tillämpning där du förväntar dig att en dynamisk datastruktur används. En tillämpning av statisk datastruktur är spelbrädan med fast storlek (kan vara schack, fyra-i-rad, osv) medan en dynamisk struktur länkade listor eller träd uppbyggda av pekare (som exempelvis domino)

3. Beskriv en sammanhang utanför datavetenskapen där begreppet pekare förekommer. En telefonkatalog är i grunden en samling pekare som pekar ut var specifika personer bor eller kan nås. Samma sak gäller för sidhänvisning, innehållsförteckning eller fotnot i en bok som pekar vidare till var man hittar mer information i texten

---

## 8.3. Hur datastrukturer lagras och implementeras i datorns fysiska minne

---

### 8.3.1. Lagring av arrayer

För endimensionella arrayer lagras data i en kontinuerlig följd av minnesceller. Om basadressen för arrayen är "x" och varje element upptar "s" minnesceller, beräknas adressen för elementet på index "i" som "adress = x + (i x s)".

För tvådimensionella arrayer (matriser) är det annorlunda. Eftersom datorns primärminne är endimensionellt (en linjär sekvens av adresser) måste matriser "plattas till" för att kunna lagras. Data lagras på två sätt för tvådimensionella arrayer, nämnlingen radvis lagring och kolumnvis lagring. För radvis lagring lagras hela första raden först, därefter hela andra raden, och så vidare. För kolumnvis lagring lagras hela första kolumnen först, sedan nästa kolumn.

För att hitta elementet i rad "r" och kolumn "c" omvandlar kompilatorn indexparet till en specifik minnesadress via ett adresspolynom.

---

### 8.3.2. Lagring av poster / aggregat

Hur en struct eller record lagras beror på om fältens storlekar är kända i förväg. Antag att det är fasta storlekar (statiska datastrukturer) så lagras alla fält/data direkt efter varandra i ett sammanhängande block i minnet. Exempelvis, "Employee" med tillhörande "Name", "Age", SkillRating" ser ut så här i datorns primärminne [[Employee.Name], [Employee.Age], [Employee.SkillRating]]. Om fälten kan ändra storlek lagras istället ett block med pekare som pekar ut de olika minnesplatserna där fältens data faktiskt ligger. Samma exempel [[Employee.Name.Pekare -> Employee.Name], [Employee.Age.Pekare -> Employee.Age], [Employee.SkillRating.Pekare -> Employee.Skillrating]].

---

### 8.3.3. Lagring av länkade listor

En nod i en länkad lista bestående av dynamiskt allokerat minne innehåller två fält: själva datat samt en pekare till nästa nod i listan. Det finns några viktiga komponenter i en länkad lista:

- Huvudpekare är en variabel/pekare som håller minnesadressen till listans första nod
- Slutnod är den sista nodens pekare som sätts till ett nollvärde (NIL eller None) för att markera att listan är slut

Insättning och borttagning av data:

- För att ta bort en nod (till exempel Employee.Age) så ändrar man pekaren från föregående nod, i detta fall Employee.Name, till Employee.SkillRating, och frigör sedan minnesytan som Employee.Age upptog.
- För att skapa en ny nod, till exempel Employee.Country skapas noden i minnet, och man manipulera pekare enligt den önskade ordningen
- Vid sortering flyttar man enbart om pekarna i minnet istället för att flytta själva datat, vilket gör operationen mycket snabb

---

### 8.3.4. Lagring av stackar och köer

Stackar implementeras ofta i ett kontinuerligt block av minnesceller (en vanlig array). En stackpekare (huvudpekare) håller reda på vilket index nästa element ska läggas på eller tas ifrån. En tom stack indikeras av att stackpekaren står på 0 eller botten.

För köer och cirkulra köer krävs det två pekare, en huvudpekare var element tas bort och en svanspekare var element läggs till. För att förhindra att kön "vandrar" ur arrayens minnesutrymme används en cirkulär kö, där den sista minnescellen i blocket anses ligga direkt intill den första. När en pekare når slutet av arrayen snurrar den runt till index 0 igen.

---

### 8.3.5. Lagring av binärträd

Det finns två helt olika sätt att lagra ett binärträd i minnet:

- Länkad struktur med pekare (dynamiskt)
- Kontinuerligt minnesblock utan pekare (array-baserat / statiskt)

Varje nod i en länkad struktur med pekare består av tre fält (data, vänster barnpekare, höger barnpekare). Roten pekas ut av en rotpekare. Blad och löv har NIL/None i sina barkpekare.

Varje nod i ett träd som består av ett kontinuerligt minnesblock utan pekare så lagras trädet i en vanlig array rad för rad (roten först, sedan dess barn, sedan barnbarn). Roten placeras på index 1. För en nod på position "n":

- Vänster barn ligger på position "2n"
- Höger barn ligger på position "2n + 1"
- Föräldrer hittas på position "n/2", det vill säga positionen dividerad med 2 utan decimaler
- Syskon hittas genom att lägga till 1 (om positionen är jämn) eller dra ifrån 1 (om positionen är udda)

Denna array-metod är extremt effektiv för balanserade och fyllda träd, men om trädet är glest eller obalanserat leder det till enorma mängder tomma/slösade platser i arrayen.

För att skydda användaren från dessa tekniska lagringsmodeller döljs den fysiska hanteringen bakom funktioner. Ett klassiskt exempel är rekursiv utskrift av ett sorterat binärträd:

def PrintTree(Tree):
    if Tree is not None:
        PrintTree(Tree.Left)    1. Besök bänster subträd rekursivt
        Print(Tree.Value)       2. Skrivut nodens värde
        PrintTree(Tree.Right)   3. Besök höger subträd rekursivt

Detta algoritmiska mönster skriver ut alla element i trädet i perfekt alfabetisk/sorterad ordning.

---

### 8.3.6. Frågor

1. Vad är villkoret för att en länkad lista ska anses vara tom? För att en länkad lista ska anses vara tom så räcker det att sluthuvudets/svanshunvudets pekare mot ett nollvärde (NIL eller None) för att markera att listan är slut. För att listan ska anses vara helt tom finns det inga noder alls i minnet. Villkoret är därför att huvudpekaren själv innehåller värdet NIL eller None.

2. Hur hittar du positionen för föräldern och syskonet till en nod på position 7 i ett träd som lagras i ett kontinuerligt minnesblock utan pekare? Om position är 7 så blir vänsterbarnet 14, och högerbarnet 15, plus att förändern blir 7/2 och syskonet blir det 6 då positionen är udda.

3. När en kö implementeras cirkulärt i en array - vad kännetecknar förhållandet mellan huvud- och svanspekare när kön är tom respektive full? När kön är tom så pekar både huvudpekare och svanspekare på samma minnescell. När kön är full pekar huvudpekare och svanspekare faktiskt också på samma minnescell. Eftersom förhållandet huvud är lika med svans uppstår i båda fallen måste man ha extra information (till exempel en räknare för antal element eller lämna en tom minnescell) för att systemet ska kunna skilja på om kön är helt tom eller helt full.

---

## 8.4. En kort fallstudie

Målet i fallstudien är att lagra en alfabetiskt sorterad lista med namn och stödja tre grundläggande operationer:

- Söka efter ett element (Search) rekursivt
- Skriva ut hela listan i alfabetisk ordning (PrintTree) rekursivt
- Sätta in ett nytt element (Insert) rekurivt

Om listan lagras som en vanlig enkellänkad lista måste man söka igenom den sekventiellt från början, vilket blir mycket slött när listan växer. En array tillåter snabb binärsökning, men är statisk och svår att utöka dynamiskt när nya namn tillkommer.

Listan lagras som ett binärt sökträd, mitten-elementet i den sorterade sekvensen placeras som trädets rot. Vänster subträd innehåller alla element som är mindre än roten, och höger subträd innehåller alla element som är större än roten.

Sökningen använder binärsökningsprincipen och utnyttjar trädets struktur:

- Jämför det sökta värdet med den aktuella nodens värde
- Om noden är tom (None), har sökningen misslyckats
- Om värdena är lika har sökningen lyckats
- Om det sökta värdet är mindre än den aktuella nodens värde, anropas "Search" rekursivt på det vänstra subträdet
- Om det sökta värdet är större än den aktuella nodens värde, anropas "Search" rekursivt på det högra subträdet

För att skriva ut innehållet i perfekt alfabetisk ordning används in-order traversal. Eftersom allt till vänster om en nod är mindre och allt till höger är större, garanterar denna enkla trestegsalgoritm att namnen skrivs ut i exakt sorterad ordning.

När ett nytt namn ska läggas till behöver man inte snuva om i hela trädet:

- Man söker sig ner längs trädet med det nya värdet precis som vid en vanlig sökning
- När man når en tom plats (en None) skapas en ny lövnod med det nya värdet på den platsen
- Om värdet redan finns i trädet görs ingen ändring

När paketet är färdigbyggt kan en programmerare använda funktionerna Search, PrintTree och Insert utan att bry sig om att namnen i själva verket ligger spridda i minnet sammankopplade med pekare. För användaren fungerar det som en vanlig sorterad lista.

---

### 8.4.1. Frågor

1. Rita det binära sökträdet du skulle använda för att lagra listan med bokstäver R, S, T, U, V, W, X, Y, Z för framtida sökning.
R, S, T, U
W, X, Y, Z
                    V
            S               X
        R       U       W       Z
            T               Y

2. Ange vägen som följs av binäralgoritmen när den söker efter element J i trädet A - M. Vad händer när man söker efter elementet P?
                            G
            D                               K
    B               F               I               M
A       C       E               H       J       L

Den sökta vägen G -> K -> I -> J

Den sökta vägen blir G -> K -> M -> None (misslyckad sökning).

1. Rita ett diagram/beskriv statusen för aktiveringen i den rekursiva utskriftalgoritmen (PrintTree) vid den tidpunkt då noden K skrivs ut i trädet A - M.

2. Beskriv hur en trädstruktur där varje nod kan ha upp till 26 barn skulle kunna användas för att koda och kontrollera korrekt stavning av engelska ord.

---

## 8.5. Skräddarsydda datatyper

---

### 8.5.1. Användardefinierade datatyper

Programmeringsspråk erbjuder inbyggda primitiva datatyper som int, float, char och boolean. När man vill samla relaterade information av olika typer skapar man en egen sammansatt datatyp.

- Typ (Type) och Instans (Instance)

Typen/mallen är en ritning som beskriver datastrukturens uppbyggnad men som i sig inte reserverar något minnesutrymme (fungerar som en kakform). Instansen är det faktiska objektet som skapas i minnet utifrån mallen när programmet körs. Traditionella användardefinierade datatyper (som struct) beskriver enbart hur data lagras, men tillhandahåller inga funktioner eller operationer för att manipulera datat.

En abstrakt datatyp tar steget vidare genom att samla både data (representation) ich funktioner/operationer (beteende) i en och samma enhet.

Språk som stödjer abstrakta datatyper bygger på två viktiga principer:

- Gemensam enhet som är syntax för att samla datastrukturen och dess tillhörande funktioner på ett ställe
- Informationsdöljande är en mekanism som döljer den interna minnesstrukturen. Användaren tillåts enbart interagera med datastrukturen via funktioner (såsom push(), pop(), isEmpty()), vilket förhindrar att utomstående kod ändrar datat på felaktigt sätt.