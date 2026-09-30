# 3. Ditt första Python-program

## Skriv och köra skript (REPL vs. Skriptfönster)

- Det interaktiva fönstret (REPL), när du öppnar IDLE möts du av en interaktiv Python-shell. Processen att läsa in koden, utvärdera den och skriva ut resultatet kallas Read-Evaluate-Print Loop (eller REPL). Det är perfekt för att testa enstaka kodrader, som "print("Hello, world")"
- Skriptfönstret, för att spara program som ska köras flera gånger öppnar du ett nytt fönster (File -> New File) Filer sparas med ändelsen ".py". Skriptet körs i IDLE via menyn "Run -> Run Module" eller genom att trycka på F5

## Hantera fel i koden

- Syntaxfel (Syntax errors), uppstår när koden bryter mot Pythons grammatikregler (till exempel om ett citationstecken saknas i slutet av en sträng). IDLE upptäcker detta innan programmet börjar köra
- Körfelsfel (Run-time errors / Exceptions), upptäcks först när koden körs. Om du till exempel försöker använda en variabel som inte definiterats uppstår ett "NameError"

## Skapa och namnge variabler

- Variabler används för att spara värden och ge de en tydlig kontext i koden
- Värden tilldelas med tilldelningsoperator "=", där värdet till höger tilldelas variabelnamnet till vänster
- Variabelnamn är skiftlägeskänsliga (case-sensitive, till exempel "phrase" och "Phrase" är två helt olika variabler)
- Reglre för namn, får innehålla bokstäver, siffror och understreck "_", men får aldrig börja med en siffra

## Inspektera värden i skaltolken

- I det interaktiva fönstret kan du skriva ett variabelnamn direkt och trycka "Enter" för att inspektera dess exakta värde och datatyp (till exempel visas strängar med citationstecken som "2", medan siffror visas som 2). I ett skript krävs dock alltid "print()" för att visa något på skärmen

## Kommentarer och PEP 8

- Kommentarer inleds med tecknet "#" och ignoreras helt av Python när koden körs
- De kan skrivas som blockkommentarer på egna rader eller som inlinjekommentarer i slutet av en kodrad
- Enligt stilspråket PEP 8 ska kommentarer skrivas i hela meningar med ett mellanslag efter "#"

---

## Frågor

Vad står förkortningen REPL för och hur fungerar den tre-stegs-loopen?

Förkortningen REPL står för Read-Evaluate-Print Loop, och innebär står för processen som läser koden, utvärderar den och skriver ut resultatet.

Vad är skillnaden mellan ett syntaxfel och ett körfelsfel (run-time error)?

Skillnaden mellan ett syntaxfel och ett körfelsfel är att syntaxfel är ett fel som uppstår när programmet bryter mot grammatikregler och som uppstår innan programmet körs medan körfelsfel uppstår under eller efter programmets har körts.

Vilka tecken får användas i ett giltigt variabelnamn i Python, och vilken regel gäller angående siffror?

Variabelnamn får innehålla bokstäver, siffror och understreck, men det får aldrig börja med en siffra.

---
