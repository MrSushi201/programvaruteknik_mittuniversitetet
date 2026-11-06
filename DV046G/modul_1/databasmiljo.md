# 2. Databasmiljö

## 1. ANSI-SPARC Tre-nivåarkitektur

År 1971 föreslog DBTG (CODASYL) en två-nivåarkitektur med schema och subscheman.
År 1975 presenterade ANSI / X3 / SPARC en tre-nivåarkitektur med en systemkatalog, vilket bygger på principer om att isolera applikationsprogram från fysiska lagringsdetaljer.
Syftet med tre-nivåarkitekturen är att separera varje användares vy av databasen från hur databasen fysiskt representeras på datorn.

### De tre abstraktionsnivåerna

1. Extern nivå (External level)
2. Begreppsmässig / konceptuell nivå (Conceptual level)
3. Intern nivå (Internal level)

Extern nivå (Extern level): Användarens vy av databasen. Beskriver endast den del av databasen som är relevant för en viss användare eller applikation och döljer resten av systemet.

Begreppmässig / konceptuell nivå (Conceptual level): Gemenskapsvyn ("community view") av databasen som beskriver vad för data som lagras samt relationerna mellan dessa. Den innehåller alla entiteter, attribut, relationer, integritetsvillkor och säkerhetsinformation, helt oberoende av fysiska lagringsdetaljer.

Intern nivå (Internal level): Den fysiska representationen av databasen på datorn som beskriver hur data lagras. Den täcker datastrukturer, filorganisationer, indexering, datakomprimering och kryptering för att uppnå optimal prestanda och utrymmesanvändning. Under den interna nivån finns den rent fysiska nivån som hanteras av operativsystemet under DBMS-styrning.

---

## 2. Scheman, mappningar och instanser

För att administrera de tre nivåerna skiljer man på beskrivningen av data och själva data.

- Databasschema (Database schema / Intension)
  - Externa scheman (Subscheman)
  - Konceptuellt schema
  - Internt schema
- Databasinstans (Database instance / Extension / State)

Databasschema (Database schema / Intension): Den övergripande beskrivningen av databasstrukturen som definieras under designfasen och ändras sällan.

Externa scheman (Subscheman): Flera olika vyer för olika användaren.

Konceptuellt schema: En komplett beskrivning av hela databasens logiska struktur.

Internt schema: En fullständig beskrivning av den interna modellen med lagrade poster, datafält och index. 

---

### Mappningar

DBMS ansvarar för att översätta (mappa) förfrågningar och resultat mellan nivåerna.

- Extern / Konceptuell mappning
- Konceptuell / Intern mappning

Extern / Konceptuell mappning: Kopplar namn i användarens vy till den relevanta delen av det konceptuella schemat.

Konceptuell / Intern mappning: Gör det möjligt för DBMS att hitta de faktiska fysiska posterna på lagringsmediet som motsvarar en logisk post i det konceptuella schemat.

---

## 3. Dataoberoende

Huvudsyftet med tre-nivåarkitekturen är att erbjuda dataoberoende, vilket innebär att högre nivåer inte påverkas när ändringar görs på lägre nivåer.

- Logiskt dataoberoende (Logical data independence)
- Fysiskt dataoberoende (Physical data independence)

Logiskt dataoberoende (Logical data independence): Innebär att externa scheman (och applikationsprogram) inte påverkas av ändringar i det konceptuella schemat (t.ex. när nya entiteter, attribut eller relationer läggs till eller tas bort).

Fysiskt dataoberoende (Physical data independence): Innebär att det konceptuella schemat inte påverkas av ändringar i det interna schemat (t.ex. byte av av filorganisation, lagringsstrukturer, indexering eller lagringsenheter).

---

## 4. Dataspråk

Ett dataunderspråk (data sublanguage) består av två delar och är inbäddat i ett värdspråk (host language, t.ex. C, Java, Visual Basic) eller används interaktivt.

- Data Definition Language (DDL)
  - Tillåter databasdesigners och DBA att beskriva och namnge entiteter, attribut, relationer samt säkerhets- och integritetsvillkor.
  - Kompilering av DDL-satser skapar tabeller i systemkatalogen (System Catalog / Data Dictionary / Metadata), vilken innehåller "data om data".
- Data Manipulation Language (DML)
  - Tillhandahåller operationer för datamanipulering: infogning (insert), uppdatering (update), borttagning (delete) och sökning (retrieval).
  - Den del av DML som hanterar datasökning kallas frågespråk (Query Language).
  - DML delas in i två typer
    - Proceduriell DML (Procedural DML)
    - Icke-proceduriell DML / Deklarativ DML (Nonprocedural DML)
- Fjärde generationens språk (4GLs)
  - Icke-proceduriella verktyg som ökar utvecklares produktivitet, inklusive rapportgeneratorer, formulärgeneratorer och grafikgenerator.

---

## 5. Datamodeller och konceptuell modellering

En datamodell är en samling koncept för att beskriva data och består av tre delar.

- En strukturell del (regler för hur databaser konstrueras)
- En manipulativ del (vilka operationer som är tillåtna på data)
- En uppsättning integritetsvillkor (säkerställer att data är korrekta)

### Kategorier av datamodeller

1. Objektbaserade datamodeller (Object-based data models)
2. Postbaserade datamodeller (Record-based data models)
  - Relationsmodellen (Relational model)
  - Nätverksmodellen (Network model)
  - Hierarkisk modell (Hierarchical model)
3. Fysiska datamodeller (Physical data models)
4. Konceptuell modellering (Conceptual modelling)

Objektbaserade datamodeller (Object-based data models): Innefattar entity-relationship (ER), semantiska, funktionella och objektorienterade modeller.

Postbaserade datamodeller (Record-based data models): Databasen består av poster med fasta format. 

Relationsmodellen (Relational model): Data representeras som tabeller och raltioner (deklarativ ansats).

Nätverksmodellen (Network model): Data representeras som poster (noder) och relationer representeras som mängder / pekare i en grafstruktur (navigationsansats).

Hierarkisk modell (Hiarchical model): En begränsad nätverksmodell där strukturen utgörs av ett träd där varje nod har maximalt en förälder (navigationsansats).

Fysiska datamodeller (Physical data models): Beskriver hur data lagras i datorn på den lägsta nivån (t.ex. unifying model och frame memory).

Konceptuell modellering (Conceptual modelling): Processen att skapa en detaljerad och komplett arkitektur för databasen som är helt oberoende av alla fysiska och tekniska implementationsdetaljer.

---

## 6. Funktioner i ett DBMS

Codd (1982) definierade 8 grundläggande tjänster som ett fullskaligt DBMS måste erbjuda, till vilka författarna lagt till ytterligare 2. 

1. Datalagring, hämtning och uppdatering
2. Användartillgänglig systemkatalog
3. Transaktionsstöd
4. Samtidighetsstyrning (Concurrency control services)
5. Återanställningstjänster (Recovery control services)
6. Auktoriseringstjänster (Authorization services)
7. Stöd för datakommunikation
8. Integritetstjänster
9. Tjänster för att främja dataoberoende
10. Verktygstjänster (Utility services)

Datalagring, hämtning och uppdatering: Grundläggande förmåga att hantera data utan att användaren behöver känna till fysiska lagringsdetaljer.

Användartillgänglig systemkatalog: En central lagringsplats (systemkatalog / datadiaktet / metadata) som beskriver scheman, användare, behörigheter och integritetsvillkor.

Transaktionsstöd: Mekanismer som garanterar att alla uppdateringar i en transaktion antingen genomförs helt eller inte alls.

Samtidighetsstyrning (Concurrency control services): Säkerställer att databasen uppdateras korrekt när flera användare läser och skriver samtidigt.

Återanställningstjänster (Recovery control services): Återställer databasen till ett konsistent tillstånd vid hårdvaru- eller mjukvarufel.

Auktoriseringstjänster (Authorization services): Säkerställer att endast behöriga användare har tillgång till data. 

Stöd för datakommunikation: Integration med datakommunikationshanterare (Data Communication Manger - DCM) för att ta emot förfrågningar över nätverk. 

Integritetstjänster: Säkerställer att data i databsen följer angivna regler och restriktioner.

Tjänster för att främja dataoberoende: Tillhandahåller vyer och subscheman för att isolera program från databasens struktur.

Verktygstjänster (Utility services): Hjälpprogram för import / export, prestandaövervakning, indexreorganisation och skräpinsamling (garbage collection).

---

## 7. Komplettering från "En webbkurs om databaser"

- Separation mellan SQL och lagring
- Prestandaoptimering (Indexering)

Separation mellan SQL och lagring: När du skriver SQL-frågor (DML) arbetar du mot den konceptuella / externa nivån utan att bry dig om filorganisationen på hårddisken.

Prestandaoptimering (Indexering): Genom att skapa index (på den interna nivån) kan man drastiskt förbättra sökhastigheten utan att behöva ändra några SQL-frågor eller applikationskod, vilket visar nyttan med fysisk dataoberoende.