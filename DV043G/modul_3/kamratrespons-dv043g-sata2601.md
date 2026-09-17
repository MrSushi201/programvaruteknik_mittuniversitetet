# Kamratrespons - DV043G

---

## Frågor

---

### 1. Algoritmer (5 poäng)

Gör en strikt och en "allmän" beskrivning av algoritmbegreppet.
Exemplifiera med tre algoritmer.
Beskriv stegen i de algoritmer du exemplifierar med.

Det finns två definitioner av begreppet algoritm i kurslitteraturen, en informell och en formell.
Den informella definitionen beskriver en algoritm som en samling av steg som definierar hur en uppgift utförs [1], [2].
Den formella definitionen beskriver en algoritm som en väldefinierad terminerande process som består av en samling av ordnad mängd, entydiga och exekverbara steg [1], [2].

Det som skiljer sig mellan den informella och den formella är de fyra kriterierna som nämnts ovan:

- En ordnad mängd av steg - Det finns en tydlig exekveringsordning i algoritmen
- Entydighet - Att alla steg är väldefinierade
- Exekverbara steg - Att alla steg är genomförbara
- Terminerande process - Att algoritmen har ett tydligt slut (inte nödvändigtvis att datorn har exekverat alla definierade steg som finns i algoritmen!)

Exempel på algoritmer är:

1. Euklides algoritm för att hitta den största gemensamma delaren mellan två positiva heltal X och Y
2. Sekventiell sökning i en kontinuerlig lista
3. Binär sökning i en kontinuerlig lista

Beskrivning för Euklides algoritm (hur den fungerar):

Euklides algoritm används för att hitta den största gemensamma delaren mellan två positiva heltal X och Y.
Rent praktiskt så kan man då dela både nämnaren och täljaren med den största gemensamma delaren för att föenkla bråk.
Exempel om X = 100 och Y = 22 så blir det bråket 100/22 (eller så kan man använda den största gemensamma delaren och dela 100 och 22 med den, och då blir det motsvarande bråket istället 50/11).

Hur Euklides algoritm fungerar:

1. Identifiera X och Y, där X är det större positiva heltalet och Y är det mindre positiva heltalet
2. Definiera några regler (villkor):
    1. Att både X och Y får inte börja med ett värde som är mindre eller lika med 0
    2. Att X är alltid större än Y
    3. Divisionen sker mellan X med Y, och inte Y med X
    4. En ny tilldelning sker vid division mellan X och Y som ger rest, där X antar värdet av Y, och Y antar värdet av resten
    5. Upprepa ovan stegen tills Y antar värdet noll
    6. Den största gemensamma delaren är då det värdet X antar vid Y är lika med 0

Beskrivning för sekventiell sökning i en kontinuerlig lista

Sekventiell sökning används för att hitta ett sökvärde i en kontinuerlig lista genom stegvis indexering från det första värdet tills antingen att sökvärdet matchar ett värde i listan eller inte alls matchar något värde.

Hur sekventiell sökning fungerar:

1. Definiera några regler (villkor):
    1. Listan får inte vara tom. Om listan är tom så kan man inte indexera över listan och det finns inget värde att söka på
2. Definiera ett sökvärde
3. Första värdet i listan blir "testvärdet" som sökvärdet ska testas mot
4. Sökvärdet testas mot testvärdet
5. Så länge sökvärdet inte matchar testvärdet så flyttar man vidare till nästa värde i listan och ny tilldelning och upprepning sker
6. Om sökvärdet matchar testvärdet så är sökningen framgångsrik. Om sökningen når listans slut och en matchning mellan sökvärdet och alla testvärdena inte hittats så är sökningen misslyckad, det vill säg att sökvärdet inte finns i listan

Beskrivning för binär säkning i en kontinuerlig lista

Binär sökning används också för att hitta ett sökvärde i en kontinuerlig lista med hjälp av halveringsprincipen.
Binär sökning kräver också att listan är sorterad eller ordnad i storleksordning.
Principiellt så fungerar binär sökning genom halvering av listan, det vill säga algoritmen undersöker först värdet som finns mitt i listan.
Sökvärdet jämförs mot det valda "mittvärdet" eller "testvärdet".
Om sökvärdet är mindre än det valda mittvärdet, flyttas sökningen till den vänstra delen av listan.
Om sökvärdet är större än det valda mittvärdet, flyttas sökningen till den högra delen av listan.
Så länge sökvärdet inte matchar mittvärdet så upprepas de ovantående stegen.
Om sökvärdet till slut matchar mittvärdet är sökningen framgånsrik.
Om söksegmentet efter halveringen blir tomt utan att värdet hittats är sökningen misslyckad.

Vi översätter ovanstående beskrivning till en instruktion som liknar den som beskriver sekventiell sökning:

1. Listan får inte vara tom. Om listan är tom så kan man inte halvera listan och det finns inget värde att söka på
2. Listan måste vara sorterad eller ordnad i storleksordning
3. Definiera eller tilldela ett sökvärde
4. Välj det värde som ligger mitt i listan, tilldela detta värde som testvärdet som sökvärdet ska testas mot
5. Sökvärdet testas mot testvärdet
6. Om sökvärdet inte matchar testvärdet OCH sökvärdet är mindre än testvärdet, flyttas sökningen till den vänstra delen av listan, och denna del blir då en ny söklista
7. Om sökvärdet inte matchar testvärdet OCH sökvärdet är större än testvärdet, flyttas sökningen till den högra delen av listan, och denna del blir då en ny söklista
8. Upprepa steg 4-6/7
9. Om sökvärdet till slut matchar testvärdet är sökningen framgångsrik
10. Om sökvärdet inte matchar något testvärde ELLER om söklistan efter halvering blir tom så är sökningen misslyckad

---

### 2. Sökning

Jämför binär sökning med sekventiell sökning i kontinuerliga listor.
Ange när det är effektivt att använda den ena respektive den andra metoden.
Är den ena metoden alltid effektivare än den andra?

Som tidigare nämnts i fråga 1 så kräver inte sekventiell sökning att söklistan är sorterad eller ordnad medan söklistan måste vara sorterad eller ordnad vid använding av binär sökning.
Utifrån detta är det definitivt effektivare att använda sekventiell sökning än binär sökning när söklistan är osorterad.
Så, för att jämföra algoritmernas prestanda mot en kontinuerlig (osorterad) lista så måste man först sortera (som är en annan algoritm i sig) listan vid användning av binär sökning.

Däremot, antar att sökelementet inte finns i den osorterad lista så måste algoritmen loopa igenom listan innan den kan rapportera en misslyckad sökning.

Till exempel så kan vi disktuera de två sista frågorna från modulens quiz.
Vi antar en lista med 4000 element i listan.
Med sekventiell sökning, i det värsta fallet (där sista värdet är antingen sökvärdet eller att sökvärdet saknas helt från listan), så måste algoritmen loopas genom alla 4000 elementen.
Med binär sökning, i det värsta fallet (där sista mittvärdet är sökvärdet eller att sökvärdet saknas i listan), halveras algoritmen listan 12 gånger bara.
Det är tydligt att binär sökningen är ett bättre val i detta fall.

För att genalisera eller bevisa prestandan, och när är det lämpligast att använda den ena metoden respektive den andra kan vi hänvisa till kurslitteraturen igen.
Kurslitteraturen beskriver genomsnittlig söksteg för sekventiell sökning som n/2 när n är antalet element i en lista, medan genomsnittlig söksteg för binär sökning är cirka log2(n) [1], [2].

Vi exemplifierar med följande scenarios:

Låt n = 1, både sekventiell och binär sökning behöver göra 1 sökning i värsta fall(så söksteg är samma).
Låt n = 2, sekventiell kräver i värsta fall 2 söksteg, och binär kräver också i värsta 2 söksteg då det sökta värdet kan ligga i den andra halvan.
Däremot, låt n = 3, sekventiell kräver i värsta fall 3 söksteg medan binär nu max 2 söksteg (eftersom algoritmen nu kollar mitten först, och har max 1 element kvar på vardera sida).
Låt n = 4, sekventiell kräver återigen i värsta fall 4 söksteg medan binär återigen max 2 söksteg.
Slusatsen, från och med n = 3, så vinner binär sökning varje gång, och ju större n blir, desto mer skillnad i antalet söksteg.

Så, en till fördel med binär sökning är att den är mycket effektivare ju större söklistan blir.

---

### 3. Variabler och konstanter

Pelle Programmerare menar att möjligheten att deklarera konstanter i ett programspråk inte är nödvändig eftersom man kan använda variabler istället.
Vidare tycker Pelle att man ska använda globala variabler för att det blir mycket enklare då.

Ge argument för att Pelle Programmerare skriver sämre program med denna inställning.
Varför är det i vissa lägen bättre att använda konstanter i stället för variabler?
Vilka problem kan uppstå om man använder globala variabler?
Ange minst två problem.

Först och främst kan det vara bra att definiera följande begrepp, variabel och konstant.
En variabel är en identifierare för en minnesplats som kan anta och ändra olika värden under programmets gång.
En konstant är också en identifierare som däremot binds till ett fast, icke-föränderligt värde vid deklarationen, och som programmeringsspråket inte tillåter att man ändrar på värdet under exekveringen.
Vid första ögonblicket kan definitionen för en variabel vara till mycket fördel i jämförelse med konstant.
Däremot, det finns massvis med fördelar med konstanter som variabler inte kan erbjuda.
Exempelvis kan en konstant inte ändras av misstag under programmets gång medan variabel kan dynamiskt ändras.
Detta ger ökad säkerhet.
Det innebär också att man i princip behöver bara underhålla konstanten på en plats stället för alla ställen i programmet (som man oftast får göra vid användning av variabler).
Detta är i sig inte ett problem utan det sparar så mycket tid och förebygger mot mänskliga fel.

Sedan, problem som kan uppstå vid användning av globala variabler är att det är väldigt riskebelt.
Först, vilken funktion och del i ett program som helst som använder den globala variabeln kan ändra på själva värdet, vilket resulterar i att andra funktioner som från början förlitar sig på det första värdet nu också påverkas av ändringen.
Det i sin tur leder till högre koppling mellan delarna i ett program.

