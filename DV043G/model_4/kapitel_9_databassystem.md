# Kapitel 9 - Databassystem

---

## 9.1.Grundläggande databasbegrepp

- Platta filer och databaser, skillnaden mellan traditionella fristående filer och en integrerad databas
- Scheman och underscheman, beskriver databasens hela struktur respektive den del som en enskild användare/applikation har tillgång till
- Databashanterare, programvarulagret som döljer den fysiska lagringen och hanterar all sökning, ändring och tillgångskontroll
- Dataoberoende, möjligheten att ändra den fysiska databasstrukturen utan att applikationsprogrammen behöver skrivas om

---

### 9.1.1. Databas vs. platta filer

Platta filer (flat files) är traditionella filorienterade system som lagrar information i endimensionella strukturer som enbart visar datat ur ett enda perspektiv. Varje del (till exempel avdelning såsom lönekontor, personalavdelning) har sina egna filer, vilket leder till att samma information dubbleras och blir svår att samordna.

Databas är en flerdimensionell samling data där interna länkar gör informationen tillgänglig från många olika perspektiv samtidigt. Alla avdelningar delar samma integrerade databas under central administration, vilket minskar redundans, förenklar backup och ökar säkerheten.

Exempel på platta filer (liknar egentligen vyer med liknande uppgifter):

| Id | Namn | Adress | Befattning |
| --- | --- | --- | --- |
| 1001 | Santi T. | Tornstigen 4 | Data Scientist |
| 1002 | Siriwan T. | Tornstigen 4 | Project Engineer |

| Id | Namn | Adress | Månadslön | Kontonummer |
| --- | --- | --- | --- | --- |
| 1001 | Santi T. | Tornstigen 4 | 51000 | 1234-5678 |
| 1002 | Siriwan T. | Tornstigen 4 | 35000 | ABCD-EFGH |

Problemen med platta filer är:

- Redundans (dubbellagring), namn och adress lagras på flera ställen/delar
- Inkonsekvens (datafelets riskanalys), vid ändring ändras endast en del, vilket gör att informationen stämmer dåligt överens
- Endimensionell sökning, en del kanske är uppbyggd som en sekvens av fasta teckenblock sorterade på Id. Vill man hitta alla som bor på samma adress tvingas datorn läsa igenom hela filen rad för rad från början till slut, eftersom delen bara visar informationen ur ett enda givet perspektiv

Så, istället för fristående platta filer samlas all information i en gemensam databas som styrs av en databashanterare. Databasen dela upp i tre strukturerade tabeller (relationer):

- Tabell 1, Id, Namn, Adress
- Tabell 2, Id, Månadslön, Kontonummer
- Tabell 3, Id, Befattning, Avdelning

Varför är detta bättre?

- Ingen onödig redundans, till exempel lagras adress på ett enda ställe. Ändras adressen där slår ändringen igenom överallt direkt
- Olika perspektiv via underscheman, där ett underschema visar en tabell
- Mångsidig åtkomst, tack vare databsens interna länkar kan man enkelt söka fram vilka som har en viss lön, bor på en viss adress eller jobbar på en viss avdelning

---

### 9.1.2. Scheman och underscheman

När all data samlas på ett ställe är det avgörande att styra vem som får se vad för att skydda känslig information.

- Schema, den kompletta beskrivningen av hela databasens struktur. Det täcker alla entiteter, attribut och de interna länkarna mellan de
- Underschema, en avgränsad beskrivning av enbart den del av databasen som en specifik användare eller avdelning behöver

---

### 9.1.3. Databashanterare

Mjukvaran i ett databassystem är uppdelad i två tydliga lager:

- Applikationslager, hanterarar gränssnittet mot användaren. Applikationen manipulerar inte databasen direkt
- Databashanterare, programvarulagret som faktiskt utför alla sökningar, läsningar, uppdateringar och säkerhetskontroller i minnet / på disken. Applikationen skickar begäranden till DBMS, som fungerar som ett abstrakt verktyg

---

### 9.1.4. Dataoberoende

Genom att skilja på applikationsprogramvaran och DBMS uppnås dataoberoende:

- Det innebär att den interna databasstrukturen eller det övergripande schemat kan ändras utan att man behöver skriva om alla befintliga applikationsprogram
- Endast de underscheman som berörs av ändringen behöver uppdateras; övriga applikationer fortsätter fungera precis som vanligt

---

### 9.1.5. Databasmodeller

En databasmodell är den konceptuella syn på databasen som DBMS presenterar för användaren/programmeraren. Den döljer den komplicerade fysiska lagringen på disken och låter användaren arbeta med enkla strukturer. De två vanligaste modellerna är relationsmodellen (tabeller med rader och kolumner) och den objekorienterade modellen.

---

### 9.1.6. Frågor

Identifiera två avdelningar i en fabrik som har olika användingsområden för samma lagerinformation. Beskriv hur underschemat för de två avdelningarna skulle skilja sig åt.

Vad är syftet med en databasmodell?

Syftet med en databasmodell är att dölja den komplexa och fysiska lagringen på disken, och låter användaren arbeta med enkla strukturer. Det är i princip den konceptuella syn/vyn på själva databsen som DBMS presenterar för användaren.

Sammanfatta rollerna för applikationsprogramvaran respektive databashanteraren?

- Applikationslager hanterar gränssnittet mot användaren. Den manipulerar inte databasen direkt
- Databashanteraren är faktiskt det program som utför alla sökningar, läsningar, uppdateringar och säkerhetskontroller i minnet eller på disken. Applikationen skickar begäranden till DBMS, som fungerar som ett abstrakt verktyg

---

## 9.2. Relationsmodellen

- Grundbegrepp, data organiseras i tvådimensionella tabeller som kallas relationer
  - En rad kallas en tupel
  - En kolumn kallas ett attribut
- Relationsdesign
- Relationell operationer
  - SELECT, väljer ut specifika rader utifrån villkor
  - PROJECT, väljer ut specifika kolumner
  - JOIN, slår ihop två relationer baserat på gemensamma attribut
- Structured Query Language (SQL), det deklarativa språket för frågor och databashantering

---

### 9.2.1. Grundläggande begrepp och terminologi

Inom relationsmodellen framställs data i tvådimensionella tabeller som kallas relationer.

- Relation, en tabell bestående av rader och kolumner
- Tupel, en enskild rad i tabellen. Varje tupel representerar en specifik entitet (till exempel en enskild anställd)
- Attribut, en kolumn i tabellen. Varje attribut beskriver en viss egenskap eller karaktäristik hos entiteten (till exempel namn, adress eller personummer)

---

### 9.2.2. Relationsdesign och redundans

En central del i databasdesign är att bestämma hur informationen ska fördelas mellan olika tabeller:

- Problemet med för stora tabeller (redundans), om man försöker samla allt i en enda stor tabell uppstår redundans - samma data upprepas på flera rader
- Risker med redundans
  - Slöseri med utrymme, samma information lagras i onödan flera gånger
  - Raderingsanomalier, om en rad raderas för att en anställd slutar riskerar man att av misstag radera den enda förekomsten av information om själva jobbet eller avdelningen
- Lösning (uppdelning i mindre tabeller), istället delar man upp databasen i flera fokusområden
- Förlustfri uppdelning, vid uppdelning av en relation i mindre delar krävs att uppdelningen görs så att ingen information går förlorad när tabellerna slås ihop igen. Om fel attribut används som koppling kan information gå förlorad

---

### 9.2.3. Relationella operationer

För att hämta ut information ur relationsdatabaser används tre grundläggande operationer:

- SELECT, väljer ut rader (tupler) ur en relation som uppfyller ett visst angivet villkor
- PROJECT, väljer ut kolumner (attribut) ur en relation och skapar en ny relation med enbart dessa kolumner
- JOIN, slår ihop två relationer baserat på gemensamma attribut för att skapa en ny, kombinerad relation

---

### 9.2.4. Structured Query Language (SQL)

SQL är det standardiserade deklarativa språket för att kommunicera med relationsdatabaser.
Det kallas deklarativt för att man beskriver vilken information man vill ha, snarare än hur algoritmen ska gå tillväga för att hämta den.

Sökningar med SELECT:

´´´SQL
SELECT EmplId, Dept
FROM Assignment, Job
WHERE Assignment.JobId = Job.JobId
AND Assignment.TermDate = '*'
´´´

- SELECT i SQL anger vilka kolumner som ska tas fram
- FROM anger vilka tabeller som ska slås ihop
- WHERE anger filteringsvillkoren för raderna

Ändring av data i SQL:

- INSERT INTO, lägger till nya rader
- DELETE FROM, tar bort rader utfriån villkor
- UPDATE, ändrar befintliga attributvärden

´´´SQL
INSERT INTO Employee
VALUES
    ('43212', 'Sue A. Burt', '33 Fair St.', '444661111')
´´´

´´´SQL
DELETE FROM Employee
WHERE Name = 'G. Jerry Smith'
´´´

´´´SQL
UPDATE Employee
SET Address = '1812 Napoleon Ave.'
WHERE Name = 'Joe E. Baker'
´´´

---

## 9.3. Objektorienterade databaser

- Lagrar objekt istälelt för platta rader, vilket gör att objekten kan innehålla både data och egna metoder/beteenden
- Introducerar begreppet persistenta objekt (objekt som lagras permanent och lever kvar efter att programmet avslutats)

---

### 9.3.1. Lagra objekt istället för tabeller

I relationsmodellen lagras data i tvådimensionella tabeller med rader (tupler) och kolumner (attribut). I en objektorienterad databas lagras data istället direkt som objekt skapade från klasser (till exempel av klasser Employee, Job, och Assignment).

- Direkta länkar, istället för att slå ihop tabeller med JOIN-operationer kopplas objekten ihop med interna länkar och pekare som hanteras automatiskt av datbashanteraren

---

### 9.3.2. Persisenta objekt

När ett vanligt objektorienterat program körs i primärminnet försvinner alla skapade objekt så fort programmet avslutas - objekten kallas då transienta. I en objektorienterad databas ser databashanteraren till att objekten lagras permanent i masslagringen även efter att programmet har stängts av. Det kallas att objekten görs persistenta.

---

### 9.3.3. Fördelar jämfört med relationsdatabaser

1. Ingen krock mellan programmeringsparadigmer, när man skriver ett objektorienterat program och använder en relationsdatabas uppstår en krock när objektmallen ska översättas till platta tabeller. Med en objektorienterad databs jobbar både applikationskoden och databasen med samma modell
2. Inkapsling av komplex information och multimedia, ett objekt kan kapsla in komplicerade datastrukturer (som namn i olika format) eller multimediadata (som ljud och video) utan att databsens övergripande strukturer påverkas
3. Intelligenta objekt (metoder inuti databasen), objekten i databasen innehåller inte bara data, utan även egna metoder (funktioner). Istället för att skriva en komplex databasfråga kan man helt enkelt skicka ett meddelande till ett Employee-objekt och be det rapportera sin egen jobbhistoria

---

## 9.4. Databasintegritet och transaktioner

- Transaktioner och commit/rollback, loggning och commit-punkter för att garantera att databasen återställs vid systemfel
- Samtidighetsproblem, belyser "lost update" och "incorrect summary" när flera transaktioner körs samtidigt
- Låsning och dödlägen, delade och exklusiva lås samt protokoll som "wound-wait" för att förhindra dödlägen

I avsnittet behandlas hur en databashanterare säkerställaer att data förblir korrekt, konsekvent och skyddad mot systemfel och krockar när flera användare arbetar samtidigt.

---

### 9.4.1. Transaktioner och commit/rollback-protokollet

En transaktion är en sekvens av databasoperationer som utgör en logisk enhet (till exempel att överföra pengar mellan två konton). Under körningen av en transaktion kan databasen tillfälligt befinna sig i ett inkonsekvent tillstånd.

- Loggning, innan några ändringar görs i själva databasen skrivs varje steg ner i en logg i ett icke-flyktigt minne
- Commit-punkt, det ögonblick då alla steg i transaktionen har loggats. Här garanterar databashanteraren att transaktionen kommer att genomföras helt och hållet, även om strömavbrott eller systemfel skulle inträffa
- Rollback, om ett fel inträffar innan commit-punkten nås, använder databashanteraren loggen för att ångra och rulla tillbaka alla delvis utföra ändringar så att databasen återgår till sitt ursprungliga konsekventa tillstånd
- Kaskadåterställning, om en transaktion rullas tillbaka kan det påverka andra transaktioner som hunnit läsa eller bygga vidare på dess tillfälliga data, vilket tvingar även dessa att rullas tillbaka

---

### 9.4.2. Samtidighetsproblem vid parallell körning

När flera transaktioner körs samtidigt för att effektivisera tiden i masslagringen kan krockar uppstå.

- Det förlorade uppdateringsproblemet, uppstår när två transaktioner läser samma konto samtidigt innan någon av de hunnit skriva tillbaka sin ändring. Den ena transaktionens ändring skrivs då över och förloras
- Felaktigt summeringsproblem, uppstår när en transaktion beräknar en totasumma samtidigt som en annan transaktion flyttar värden mellan poster, vilket ger ett felaktigt resultat

---

### 9.4.3. Låsningsprotokoll

För att förhindra krockar använder databashanteraren lås på de datalement som används.

- Delat lås (shared lock), används när en transaktion enbart ska läsa data. Flera transaktioner kan ha delade lås på samma element samtidigt
- Exklusivt lås (exclusive lock), krävs när en transaktion ska ändra (skriva) data. Ingen annan transaktion vår varken läsa eller ändra elementet så länge låset hålls

---

### 9.4.4. Dödlägen och wound-wait-protokollet

När två transaktioner håller var sin resurs och väntar på att den andra ska släppa sin uppstår ett dödläge (deadlock).

- Wound-wait-protokollet, en metod för att lösa dödlägen genom att ge prioritet åt äldre transaktioner
  - Om en äldre transaktion behöver data som låsts av en yntre, avbryts/rullas den yngre transaktionen tillbaka (wound) så att den äldre kan slutföras
  - Om en yngre transaktion behöver data från en äldre, tvingas den yngre att vänta (wait)
  - Detta garanterar att varje transaktion förr eller senare blir äldst och släpps igenom utan att fastna

---

## 9.5. Traditionella filstruktur

- Sekventiella filer, poster lagras i en rak sekvens
- Indexerade filer, använder en separat indextabell för snabb direktuppslagning
- Hash-filer, beräknar adressen till en hink direkt från nyckeln via en hash-funktion, vilket eliminerar behovet av indexfiler

I avsnittet görs en avstickare från databassystem för att undersöka de historiska filstrukturer som ligger till grund för hur data lagras, söks och organiseras på sekundärminne. Tre huvudsakliga typer av filstrukturer behandlas:

1. Sekventiella filer
2. Indexerade filer
3. Hash-filer

Sekventiella filer:

- Uppbyggnad, data läses och skrivs i en rak sekvens från början till slut, vilket är den vanligaste filtypen för till exempel textdokument, programkod, ljud och video
- Filslut, filens slut markeras av en särskild indikator kallad End-Of-File (EOF) eller genom en specialpost kallad sentinel
- Fysisk lagring, på sekventiella media (som band eller CD-skivor) lagras filen i en sammanhängande rad. På en hårddisk kan operativsystemet däremot sprida ut filens sektorer på olika ställen på disken
- Uppdatering och merging

---

## 9.6. Datamining

- Att hitta dolda mönster i stora statiska datalager

---