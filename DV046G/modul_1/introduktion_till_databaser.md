# 1. Introduktion till databaser

I den första lektionen får du bekanta dig med några av de mest grundläggande begreppen inom databasteknik.
Du kommer att lära dig:

- Vad en databas är,
- Vad en databashanterare gör, och
- Vad som menas med databasmodell och databasarkitektur

Du får också en första inblick i den mest använda modellen idag, relationsmodellen, som ligger till grund för många av de databassystem du kommer att stötta på framöver.

---

## 1. Grundläggande begrepp

För att förstå databaser definieras fyra centrala begrepp i litteraturen:

- Databas (Database)
- Databashanteringssystem (DBMS - Database Management System)
- Databasapplikation (Database Application)
- Databassystem (Database System)

### Databas (Database)

En delad samling av logiskt relaterade data samt en beskrivning av dessa data, utformad för att möta en organisations informationsbehov.
Databasen fungerar som en integrerad och självbeskrivande resurs. 

### Databashanteringssystem (Database Management System)

Den programvara som tillåter användare att definiera, skapa, underhålla och styra åtkomsten till databasen.

### Databasapplikation (Database Application)

Ett datorprogram som interagerar med databasen genom att skicka förfrågningar (vanligen SQL-satser) till DBMS under sin körning.

### Databassystem (Database System)

En samlingsbeteckning som innefattar applikationsprogrammen, DBMS och själva databasen.

### Vardagliga tillämpningar av databassystem

Databasteknik är idag en integrerad del av vardagen. Exempel på tillämpningar är:

- Stormarknaden
- Bibliotek
- DVD- eller filmuthyrning
- Internet och e-handel
- Universitet

Stormarknaden: Streckkodsläsare söker upp priser i en produktdatabas, uppdaterar lagersaldon och lägger automatisk beställning vid låga lagernivåer.

Bibliotek: Sökning på titlar eller författare, hantering av reservationer och utskick av påminnelser.

DVD- eller filmuthyrning: Registrering av tillgängliga kopior, kunduppgifter och historik över uthyrningar. 

Internet och e-handel: Webbsidor söker i databaser efter böcker, priser, lagerstatus och rekommenderar relaterade produkter.

Universitet: Registrering av studenter, kurser, resultat och personalutbetalningar.

---

## 2. Traditionella filbaserade system och deras begränsningar

Innan databaser slog igenom användes filbaserade system (file-based systems), vilka var tidiga försök att datorisera manuella arkivsystem.
I dessa var varje avdelning i en organisation ansvarig för sina egna data och skrev egna applikationsprogram.

### Fem huvudsakliga begränsningar med filbaserade system

1. Separation och isolering av data (Separation and isolation of data)
2. Dataduplicering / Redundans (Duplication of data)
3. Databeroende (Data dependence)
4. Inkompatibla filformat (Incompatible file formats)
5. Fasta frågor och spridning av applikationsprogram (Fixed queries / proliferation of application programs)

Separation och isolering av data: Data ligger utspridda i separata filer, vilket gör det svårt att ställa frågor som kräver information från fler än en fil samtidigt.

Dataduplicering: Samma information lagras på flera ställen, vilket slösar på lagringsutrymme och tid samt leder till risk för inkonsistens (förlorad dataintegritet) om en ändring bara görs på ett ställe.

Databeroende: Filernas fysiska struktur och lagringsformat är inbäddade direkt i applikationskoden. Om filstrukturen ändras måste koden i alla berörda program skrivas om.

Inkompatibla filformat: Program skrivna i olika språk har ofta olika filstrukturer, vilket försvårar datadelning.

Fasta frågor och spridning av applikationsprogram: System klarade bara fördefinierade rapporter och saknade stöd för oplanerade frågor, vilket ledde till en överflöd av specialskrivna program.

---

## 3. Databasansatsen och vyer

DAtabasansatsen löser filsystemens problem genom att separera datadefinitionen från applikationsprogrammen och centralisera datalagringen.

- Systemkatalog (System Catalog / Data Dictionary / Metadata)
- Språk i DBMS
  - DDL (Data Definition Language)
  - DML (Data Manipulation Language)
- Kontrollfunktioner
- Vy-mekanism (View Mechanism)

Systemkatalog (System Catalog / Data Dictionary / Metadata): Databasen innehåller inte bara operativa data utan även sin egen beskrivning ("data om data"). Det är denna självbeskrivande egenskap som ger program-databeroende (program-data independence).

DDL (Data Definition Language): Tillåter användare att definiera databasens struktur, datatyper och villkor.

DML (Data Manipulation Language): Tillåter användare att infoga, uppdatera, radera och söka data, vanligen via frågespråket SQL.

Kontrollfunktioner: DBMS erbjuder säkerhetssystem (förhindrar obehöriga), integritetssystem (bevarar konsistens), samtidighetsstyrning (concurrency control för delad åtkomst) och återställningssystem (recovery control vid hårdvaru- eller mjukvarufel).

Vy-mekanism (View Mechanism): En vy är en virtuell delmängd av databasen. Vyer förenklar systemet för användaren, ökar säkerheten genom att dölja känsliga data (t.ex. löner) och skyddar applikationer mot förändringar i den underliggande databasstrukturen.

---

## 4. Komponenter i DBMS-miljön

DBMS-miljön består av fem integrerade komponenter:

1. Hårdvara (Hardware)
2. Mjukvara (Software)
3. Data
4. Procedurer (Procedures)
5. Människor (People)

Hårdvara (Hardware): Allt från enskilda datorer till stora nätverk av servrar, ofta uppbyggt enligt en klient-server-arkitektur där en backend-server hanterar databsen och frontend-klienter kör användargränssnittet. 

Mjukvara (Software): Innefattar själva DBMS-programvaran, operativsystemet och applikationsprogrammen.

Data: Utgör bron mellan maskinvaran och människorna och består av operationella data samt metadata (schemat).

Procedurer (Procedures): Regler och instruktioner för inloggning, användning av applikationer, säkerhetskopiering (backup), felhantering och omstrukturering. 

Människor (People): De olika roller som arbetar i eller använder miljön.

---

## 5. Roller i databasmiljön

Litteraturen delar in personerna i databasmiljön i fyra huvudkategorier:

1. Data- och databasadministratörer
  - Data Administrator (DA)
  - Database Administrator (DBA)
2. Databasdesigners
  - Logisk databasdesigner
  - Fysisk databasdesigner
3. Applikationsutvecklare (Application Developers)
4. Slutanvändare (End-Users)
  - Naiva användare (Naïve users)
  - Sofistikerade användare (Sophisticated users)

Data Administrator (DA): Ansvarar för hanteringen av dataresursen på en strategisk nivå, inklusive databasplanering, policyer, standarder samt begreppsmässig och logisk databasdesign.

Database Administrator (DBA): Ansvarar för den tekniska och fysiska realiseringen av databasen, inklusive fysiska design, prestandaoptimering, säkerhet, integritetskontroll och löpande underhåll.

Logisk databasdesigner: Fokuserar på vad data representerar; identifierar entiteter, attribut, relationer och affärsregler oberoende av fysiska detaljer. 

Fysiska databasdesigner: Fokuserar på hur den logiska modellen realiseras i mål-DBMS:et; väljer tabeller, lagringsstrukturer, index och säkerhetsmekanismer.

Applikationsutvecklare (Application Developer): Utecklar de program som utför den funktionalitet slutanvändarna behöver utifrån kravspecifikationer.

Naiva användare (Naïve users): Behöver ingen databaskunskap utan använder färdiga applikationer via enkla kommandon eller menyer (t.ex. kassapersonal eller biblioteksbesökare).

Sofistikerade användare (Sophisticated users): Känner till databasens struktur och använder högnivåspråk som SQL för att ställa komplexa frågor eller skriva egna skript.

---

## 6. Databassystemens historiska utveckling (tre generationer)

Utvecklingen av databassystem indelas i tre generationer:

- Första generationen (1960-talet)
- Andra generationen (1970- och 1980-talet)
- Tredje generationen (1990-talet och framåt)

Första generationen (1960-talet): Bestod av hierarkiska modeller (t.ex. IBM IMS) och nätverksmodeller (t.ex. IDS utvecklat av Charles Bachmann samt CODASYL / DBTG-standarden). Nackdelarna var att de krävde komplex navigationsprogrammering, saknade teoretisk grund och hade minimalt databeroende.

Andra generationen (1970- och 1980-talet): Relationsmodellen (RDBMS), som presenterades i E. F. Codds banbrytande artikel 1970. Detta ledde till IBM System R, utvecklingen av frågespråket SQL och kommersiella RDBMS som Oracle, DB2, Ingres, MySQL, Microsoft SQL Server och Access.

Tredje generationen (1990-talet och framåt): Utvecklades för att hantera mer komplexa applikationskrav och ledde till Objekt-orienterade DBMS (OODBMS) och Objekt-relationella DBMS (ORDBMS). Under denna period växte även XML-integration, Data Warehousing (datavaruhus) och ERP-system (Enterprise Resource Planning) fram.

---

## 7. Fördelar och nackdelar med DBMS

Fördelar:

- Kontroll av dataredundans
- Datakonsistens
- Mer information från samma datamängd
- Delning av data
- Förbättrad dataintegritet och säkerhet
- Enforcement of standards
- Stordriftsfördelar (Economy of scale)
- Ökad tillgänglighet och produktivitet
- Program-databeroende
- Förbättrad samtidsstyrning och återanställning

Kontroll av dataredundans: Eliminerar onödig duplicering genom integration av filer.

Datakonsistens: Minskar risken för motstridiga data.

Mer information från samma datamängd: Integration möjliggör nya insikter tvärs över avdelningar.

Delning av data: Databasen tillhör hela organisationen och kan delas av behöriga användare.

Förbättrad dataintegritet och säkerhet: Centraliserade regler och behörigheter.

Enforcement of standards: Standardiserade format, namngivning och dokumentation.

Stordriftsfördelar (Economy of scale): Sammanlagda resurser ger mer kraftfulla system.

Ökad tillgänglighet och produktivitet: Snabb tillgång till data via SQL minskar utvecklingstiden.

Program-databeroende: Förenklar underhåll då datastrukturer kan ändras utan att applikationer bryts. 

Förbättrad samtidsstyrning och återanställning: Hanterar samtidiga användare och har automatiserade backup / recovery-rutiner.

Nackdelar:

- Komplexitet och storlek
- Kostnader för DBMS
- Extra hårdvarukostnader
- Konverteringskostnader
- Prestanda
- Större konsekvenser vid fel (Impact of a failure)

Komplexitet och storlek: Stor och komplex programvara som kräver betydande disk- och minnesutrymme.

Kostnader för DBMS: Licenser för stora fleranvändarsystem kan vara mycket dyra.

Extra hårdvarukostnader: Krav på mer lagringsutrymme och kraftfullare servrar.

Konverteringskostnader: Omfattande kostnader för att migrera från äldre system (legacy systems) och utbilda personal.

Prestanda: Ett generellt DBMS kan köra vissa specifika applikationer långsammare än ett skräddarsytt filsystem.

Större konsekvenser vid fel (Impact of a failure): Centraliseringen innebär att om systemet går ner påverkas hela organisationen.

---
