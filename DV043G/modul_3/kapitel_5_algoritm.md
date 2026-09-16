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

Tillståndet i processen måste ge tillräcklig information för att unikt och fullständigt bestämma vad som ska göras i varje steg.
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