# 1. Datalagring

---

## 1.1. Bitar och deras lagring

---

### 1.1.1. Bitar

Inuti dagens datorer kodas all information som mönster av 0:or och 1:or, vilka kallas för bitar.
Även om vi ofta förknippar bitar med tal, är de i själva verket bara symboler vars betydelse beror på sammanhanget - de kan representera allt från siffror och text till färger, bilder och ljud.

---

### 1.1.2. Booleska operationer

För att förstå hur bitar manipuleras används ofta logik där 0:or representerar falskt och 1:or representerar sant.
Operationer som hanterar dessa värden kallas för booleska operationer.
De viktigaste är:

- AND - Ger resultatet 1 (sant) endast om båda ingångarna är 1 (sanna)
- OR - Ger resultatet 1 (sant) om minst en av ingångarna är 1 (sant)
- XOR - Ger resultatet 1 (sant) om ingångarna är olika (sant och falskt)
- NOT - Har bara en ingång och vänder på värdet (0 (falskt) blir 1 (sant), och 1 (sant) blir 0 (falskt))

---

### 1.1.3. Grindar och Flip-flops

En enhet som utför en boolesk operation kallas för en grind.
I moderna datorer är dessa byggda av små elektroniska switchar som kallas transistorer.
Inom dessa kretsar representeras bitarna 0 och 1 som olika spänningsnivåer.
Varje grindtyp har en unik symbol och ett specifikt beteende:

- AND - Ger utdata 1 endast om båda ingångarna är 1
- OR - Ger utdata 1 om minst en av ingångarna är 1
- XOR - Ger utdata 1 endast om ingångarna är olika
- NOT - Ger motsatsen till sitt invärde som utdata

Genom att kombinera grindar kan man skapa en krets som kallas för en flip-flop.
Detta är en grundläggande enhet för datorminne som kan "komma ihåg" en nolla eller en etta så länge den får ström.
Värdet förblir konstant fram till att en puls (en tillfällig ändring från 0 till 1 och tillbaka till 0) från ennan krets tvingar den att byta tillstånd.
Genom att skicka pulser till olika ingångar kan man alltså styra om en flip-flop ska lagra en nolla eller en etta.

---

### 1.1.4. Hexadecimal notation

Eftersom långa rader av bitar (t.ex. 101101010011) är svåra för människor att läsa, använder man ofta hexadeicmal notation som en förkortning.

Systemet delar upp bitmönster i grupper om (fyra) bitar.
Varje grupp om (fyra) bitar representeras an en enda symbol.
Till exempel blir bitmönstret 1011 0101 till 0xB5 i hexadecimal form.

| Bitmönster | Hexadecimal representation |
| --- | --- |
| 0000 | 0x0 |
| 0001 | 0x1 |
| 0010 | 0x2 |
| 0011 | 0x3 |
| 0100 | 0x4 |
| 0101 | 0x5 |
| 0110 | 0x6 |
| 0111 | 0x7 |
| 1000 | 0x8 |
| 1001 | 0x9 |
| 1010 | 0xA |
| 1011 | 0xB |
| 1100 | 0xC |
| 1101 | 0xD |
| 1110 | 0xE |
| 1111 | 0xF |

---

### 1.1.5. Frågor

1. Kretsanalys - Vilka mönster av indata (bitmönster) får en krets bestående av en XOR-grind (där två övre ingångarna går in) följt av en AND-grind (där XOR-grindens utdata och en tredje, nedre ingång går in) att ge utdata 1?
Svar: XOR måste antingen ha 1 och 0 eller 0 och 1, och den tredje måste ha 1 så att AND-grinden kan få 1.
2. Flip-flop - I texten påstås det att om man placerar en 1 på den nedre ingången (medan den övre hålls på 0) tvingas flip-flop-kretsens utdata att bli 0. Beskriv händelseförloppet inuti kretsen i detta fall.
Svar: Så, först, flip-flop kretsens utdata är 0, vilket innebär att OR-grinden har 0 i båda ingångarna. Vi vet att den övre är 0, och den nedre är 1 till NOT-grinden vilket tvingas den att bli 0, det vill säga, båda ingångar till OR-grinden är noll.
3. Flip-flop - Anta att båda ingångarna till flip-flop-kretsen börjar som 0. Beskriv vad som händer steg för steg när den övre ingången tillfälligt sätts till 1.
Svar: Här har vi två OR-grindar och två NOT-grindar efter varje OR-grind. Vi antar att både ingångarna i kretsen är 0. Vi kan också se att utdata går tillbaka till den övre OR-grinden.
När den övre ingång sätts till 1 så kommer det ut en 1 från den övre OR-grinden och sedan blir det 0 på grund av en NOT-grind framför sig. 0:an går vidare till den andra OR-grinden som nu har både ingångarna som 0 vilket ger utdata 0. Då 0 går vidare till en NOT-grind innan utdata för kretsen så blir det 1 och den 1 går både som utdata från kretsen men också tillbaka till den övre OR-grinden.
4.a. Om utdata från en AND-grind skickas genom en NOT-grind kallas kombinationen för en NAND-grind (utdata blir 0 endast om båda ingångarna är 1).
Svar: Kretsen består av två ingångar av NOT-grindar, och dessa ingångarna leder till NAND-grind. Så, Om både 2 ingångarna är 1 (blir 0), så blir det 1 i slutet. Om både 2 ingångarna är 0 (blir 1), så blir det 0 i slutet. Sedan, om de är olika, så blir det 1 efter NAND-grinden.
5.a. 0110 1010 1111 0010 = 0x6AF2
5.b. 1110 1000 0101 0101 0001 0111 = 0xE85517
5.c. 0100 1000 = 0x48
6.a. 0x5FD9 = 0101 1111 1101 1001
6.b. 0x610A = 0110 0001 0000 1010
6.c. 0xABCD = 1010 1011 1100 1101
6.d. 0x0100 = 0000 0001 0000 0000

---

## 1.2. Primärminne

---
