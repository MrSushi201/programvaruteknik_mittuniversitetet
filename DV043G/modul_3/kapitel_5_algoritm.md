# 5. Algoritm

---

## 5.1. Algoritmkonceptet

---

### 5.1.1. Den formella definitionen av en algoritm

Informellt beskrivs en algoritm som en samling steg som definierar hur en uppgift utförs.
Formellt beskrivs en algoritm som en **ordnad mängd** av **entydiga**, **exekverbara** steg som definierar en **terminerande** process.
För att ett förfarande ska räknas som en algoritm i strikt datavetenskaplig mening krävs fyra kriterier:

- Ordnad mängd
- Exekverbara steg
- Entydighet
- Terminerande process

Stegen har en väldefinierad exekveringsordning.
Detta innebär inte alltid en enkel linjär sekvens; parellella algoritmer kan ha flera trådar som förgrenar sig, och i digitala kretsar styrs stegen av orsak och verkan.

Varje enskilt steg måste vara praktiskt genomförbart.
Det får inte finnas något utrymme för tolkning eller mänsklig gissning.

Tillståndet i processen måste ge tillräcklig information för att unikt och fullständigt bestämma vad som ska göras i varje steg.
Varje enskilt steg måste faktiskt vara praktiskt genomförbart.
Exekveringen kräver ingen mänsklig kreativitet, utan enbart förmågan att följa instruktioner.

Algoritmen måste nåt ett slut efter ett ändligt antal steg.
Inom teoretisk datavetenskap dras en tydlig gräns mellan processer som slutligen levererar ett svar och processer som pågår i oändlighet utan resultat.

---

### 5.1.2. ALgoritmers abstrakta natur och representation

Det är avgörande att skilja mellan en algoritm och dess representation.

- En algoritm är ett abstrakt koncept, proces som en historia är abstrakt
- En representation är den konkreta beskrivningen av algoritmen, på samma sätt som en tryckt bok är den fysiska representationen av en historia

Samma algoritm kan representeras på många olika sätt utan att själva algoritmen förändras.
Om en person upplever en instruktion som tvetydig beror det oftast inte på att den underliggande algoritmen är felaktig, utan på att representationen inte har tillräcklig detaljnivå för den personen.

---

### 5.1.3. Algoritm, program och process

Tre centrala begrepp som ofta sammanblandas skiljs åt enligt följande:

- Algoritm är den abstrakta metoden eller problemlösningslogiken
- Program är en formell representation av en algoritm som är utformad för att en dator ska kunna exekvera den
- Process är aktiviteten att faktiskt exekvera ett program eller en algoritm i minnet

---

### 5.1.4. Frågor

1. Varför misslyckas dessa instruktioner med att utgöra en algoritm enlig den formella definitionen?
Svaret är att den är inte tillräcklig väldefinierad.
Vad händer när det inte finns något mynt kvar i fickan?
Eller om det finns oändligt många mynt i fickan?

2. Hur förklarar du skillnaden mellan ett program och en process?
Svaret är att ett program är en representation av en algoritm, och en process är aktiviteten där den faktiska programmet/algoritmen exekveras.

3. Vad som är vagt i den inofficiella/informella definitionen?
Svaret är att den informella defintionen saknar de fyra grundpelarna som skiljer en slumpmässig beskrivning från en riktig algoritm. De fyra grundpelarna som formar en algoritm är:

- En ordnad mängd
- Entydiga steg
- Exekverbara steg
- Terminerande process

---

## 5.2. Representera algoritmer

---

### 5.2.1. Behovet av ett formellt representationssystem

För att en dator - eller en människa - ska kunna exekvera en algoritm exakt och utan fel, måste algoritmen uttryckas i en form som inte lämnar utrymme för tolkningar eller gissningar.
Vanligt mänskliga språk (som svenska eller engelska) lämpar sig ofta dåligt för algoritmisk representation av två orsaker:

1. Tvetydighet
2. Brist på rätt detaljnivå

---

### 5.2.2. Primitiver, syntax och semantik

Datavetenskapen löser kommunikationsproblemet genom att etablera en väldefinierad samling byggstenar som kallas primitiver.
Primitiv är en grundläggande, odelbar instruktion eller byggsten i ett språk som har en helt entydig och fastställd betydelse.
När man kräver att en algoritm beskrivs i primitiver elimieras tvetydigheter och en enhetlig detaljnivå etableras.
Syntax är den symboliska representationen eller grammatiken (hur primitiven skrivs och ser ut).
Semantik är den faktiska innebörden eller handlingsregeln bakom primitiven (vad den utför).
Programmeringsspråk är en samling primitiver tillsammans med formaliserade regler för hur de får kombineras för att uttrycka komplexa idéer.

---

### 5.2.3. Pseudokod och flödesscheman

För att planera och utforma algoritmer innan man skriver färdig kod i ett specifikt programmeringsspråk använder man pseudokod.
Pseudokod är ett inofficiellt, intuitivt notationssystem där algoritmer uttrycks informellt.
Det är mer exakt och strukturerat än naturligt språk, men betydligt enklare för människor att läsa och skriva än strikta programmeringsspråk.

Under 1950- och 1960-talen var flödesscheman - där algoritmer ritas med geometriska figurer och pilar - det primära verktyget.
När algoritmer blir komplexa förvandlas dock flödesscheman lätt till ett rörigt nystan av korsande pilar som gör koden svåröverskådlig.
Pseudokod används som det huvudsakliga designverktyget för logik, medan flödesscheman främst används vid grafiska presentationer.

---

### 5.2.4. De tre fundamentala byggstenarna i pseudokod

All algoritmisk logik kan konstrueras med hjälp av tre grundläggande strukturer:

- Sekvens
- Selektion
- Iteration

Tilldelning används för att beräkna ett värde och spara det under ett variabelnamn för framtida bruk.
Syntaxen är:
namn = uttryck (eller namn <- uttryck)
Semantiken är uttrycket till höger utvärderas och resultatet lagras i variabeln till vänster.

Sekvens är kontrollstrukturen som styr flödet - att datorn utför instruktionerna linjärt, rad för rad i den ordning de är skrivna.

Selektion innebär att man väljer en av två alternativa vägar i algoritmen beroende på om ett booleskt villkor är sant eller falskt.
Syntaxen är:
if (villkor):
    handling A
else:
    handling B
Semantiken är om villkoret utvärderas till sant utförs handling A; annars utförs handling B.

Iterationen upprepar en eller flera instruktioner så längde ett givet villkor förblir sant.
Syntaxen är:
while (villkor):
    handling
Semantiken är att villkoren testas först.
Om det är sant utförs handlingsblocket och villkoret testas igen.
När villkoret blir falskt avbryts loopen och exekveringen fortsätter efter while-strukturen.

---

### 5.2.5. Indenteringens roll

I många traditionella programmeringsspråk används måsvingar eller nyckelord som BEGIN och END för att angränsa kodblock.
I Python och vår pseudokod används i stället strikt indentering för att definiera strukturen.
Indraget anger exakt vilka satser hör till en viss if- eller while-sats, och visar hur satser är nästlade.

Exempel:
if (not raining):
    if (temperature == hot):
        go swimming
    else:
        play golf
else:
    watch television

---

### 5.2.6. Moduläritet, funktioner och parametrar

För att dela upp komplexa algoritmer i mindre, återanvändbara delar använder vi funktioner (som i andra sammanhang även kallas procedurer, subrutiner eller metoder).

En funktion definieras i pseudokod med nyckelordet "def" följt av funktionens namn.

Exempel:
def Greetings():
    Count = 3
    while (Count > 0):
        print the message "Hello"
        Count = Count - 1

När uppgiften behövs i koden anropas den enkelt med sitt namn Greetings().

För att göra en funktion generell använder vi parametrar.

- Formell parameter
- Reell parameter

Formell parameter är det generella platshållarnamnet som står i funktiones huvud.
Reell parameter är det faktiska datavärdet eller variabeln som skickas med vid anropet.

---

### 5.2.7. Namngivningskoventioner

När vi skapar variabler eller funktioner av flera ord underviker vi mellanslag genom tre vanliga tekniker.

1. Underlinjer eller snake_case
2. PascalCasing
3. camelCasing

---

### 5.2.8. Frågor

Skriv Euklides algoritm i pseudokod.
Euklides algoritm är en algoritm för att hitta den största gemensamma divisorn eller delaren för två positiva heltal X och Y.

Initiera variablerna med indatavärdena.
X = det större av de två indatavärdena.
Y = det mindre av de två indatavärdena.

Iteration och villkor - upprepa så länge Y inte är 0.
while (Y != 0):
    Remainder = resten av divisionen mellan X och Y
    X = Y
    Y = Remainder

Resultat när loopen avbrutits.
StörstaGemensammaDelaren = X.

Hur byggstenarna samverkar i algoritmen:

- Instruktionerna inuti loppen utförs i en linjär följd. Det är helt avgörande att beräkna Remainder innan vi rensar eller förändrar X oh Y
- I varje varv testas villkoret Y != 0. Testet avgör om algoritmen ska fortsätta eller avslutas
- While-slingan repeterar blocket med satser ända tills Y = 0 och algoritmen terminerar

Slut på fråga 1.

Beskriv en samling primitiver som används inom något annat område än datorprogrammering.
Matlagning. Grundläggande mått och enkla handlingar.
Noter, förtecken (kors/fönster) och taktangivelser utgör primitiverna för att representera ett musikstycke.

Slut på fråga 2.

---

## 5.3. Att konstruera en algoritm

Detta avsnitt handlar om hur man faktiskt kommer fram till en algoritm - det vill säga själva problemlösningsprocessen som ligger till grund för all programvaruutveckling.

---

### 5.3.1. Problemlösningens natur - en konst snarare än ett recept

Att täcka algoritmernas representation handlar om hur vi skriver ned algoritmer.
Men att upptäcka en ny algoritm kräver kreativitet.
Det finns ingen mekanisk algoritm för att upptäcka algoritmer.
Det är en mänsklig och konstnärlig problemlösningsprocess.

---

### 5.3.2. G. Polyas problemlösningsmodell

Matematikern George Polya ställde 1945 upp fyra generella faser för problemlösning i sin klassiska bok How to Solve it.
Polyas 4 generella problemlösningsfaser är:

1. Förstå problemet
2. Skapa en plan
3. Genomföra planen
4. Utvärdera lösningen

I datavetenskapen och kursmterialet översätts Polyas faser till:

1. Förstå problemet
2. Hitta på en algoritm som kan tänkas lösa problemet
3. Formulera algoritmen och anpassa den till ett körbart program
4. Utvärdera programmets noggrannhet och dess möjlighet att lösa andra problem

Viktiga insikter om Polyas faser:

- Faserna är inte ett sekventiellt recept
- Icke-linjärt flöde

Du kan inte lösa ett svårt problem genom att strikt kryssa av "Fas 1 klar, nu tar vi Fas 2".
Problemlösare börjar ofta skapa strategier innan problemet är helt förstått.
Om strategin misslyckas i Fas 3 eller Fas 4 får man en djupare förståelse för problemets intrikata detaljer och kan återvända till Fas 1 eller Fas 2 med nya insikter.

---

### 5.3.3. Strategier för att få "fotfästet"

När man står inför ett helt nytt och svårt problem handlar om största steget om att "få in et fot i dörren".
Boken lyfter fram tre huvudsakliga tekniker för detta:

- Arbeta baklänges
- Leta efter relaterade problemen
- Stegvis förfining

Gällande arbeta baklängs.
Om du vet vilket utdata som krävs av ett visst indata, kan du vörja från det färdiga resultatet och försöka backa steg för steg till startläget.

Gällande leta efter relaterade problemen.
Om du känner igen ett liknande problem som du eller andra redan har löst, kan du använda den lösningen som mall eller inspiration för det nya problemet.

Gällande stegvis förfining.
Att inte försöka lösa hela det komplexa problemet på en gång i alla dess detaljer.
Istället bryter man ner problemet i flera mindre delproblem.

- Top-down
- Bottom-up
- Samverkan

Top-down är att gå från det generella/stora problemet ner till de specifika delarna.
Bottom-up är att gå i motsatt riktning.
Man börjar med att bygga små, specifika delprogram/komponenter och sätter sedan ihop de till ett störe system.
I praktiken kompletterar Top-Down och Bottom-Up ofta varandra.

---

## 5.4. Iterativa strukturer

Detta avsnitt fördjupar sig i hur upprepande processer utformas i algoritmer med hjälp av loopar (iteration).
För att illustrera hur iterativa strukturer fungerar i praktiken används två klassiska algoritmproblem:

- Sekventiell sökning
- Insättningssortering

Sekventiell sökning eller linjär sökning är en av de enklaste sökalgoritmerna.
Den används för att ta reda på om ett visst sökvärde finns i en lista eller inte.
Algoritmens princip:

1. Man börjar från listans första element
2. Man jämför sökvärdet med det nuvarande testelementet
3. Så länge man inte har hittat värdet och det finns fler element kvar att undersöka, flyttar man vidare till nästa element
4. Om listan är sorterad och man når ett element som är större än sökvärdet, kan sökningen avbrytas i förtid eftersom värdet inte kan finnas längre fram

Pseudokod för sekventiell sökning:

def SortedSequentialSearch(List, TargetValue):
    if (List is empty):
        Declare search a failure
    else:
        Select the first entry in List to be TestEntry
        while (TargetValue > TestEntry and there remain entries to be considered):
            Select the next entry in List as TestEntry
        if (TargetValue == TestEntry):
            Declare search a success
        else:
            Declare search a failure

---