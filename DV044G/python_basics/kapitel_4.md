# 4. Strängar och strängmetoder

## Vad är en sträng

- En sträng representeras av datatypen "str" och är en av Pythons fundamentala datatyper för att hantera text
- Skapas som en string literal genom att omsluta text med enkla '', eller dubbla "" citationstecken
- Längd, funktion len() returnerar antalet tecken i strängen, inklusive blanksteg
- Flerradssträngar, trippla citationstecken """""" gör att text kan sträcka sig över flera rader och bevara blanksteg

## Konkatenering, indexering och slicing

- Konkatenering, slår ihop två strängar med "+"-operatorn (till exempel "abra"+"cadabra" ger "abracadabra")
- Indexering, åtkomst till enskilda tecken görs med hakparanteser [n]. Python använder nollbaserad indexering ('' är första tecknet). Negativa index räknar från slutet [-1] är sista tecknet
- Slicing, hämtar ett delsegment med syntaxen [start:slut], där slutindexet inte inkluderas (till exempel "apple pie"[0:3] ger "app")
- Oföränderlighet, strängar kan inte ändras efter att de har skapats. Försök att tilldela ett nytt tecken (word[0]="f" när word = "goal") ger ett "TypeError". För att ändra en sträng måste en ny sträng skapas, det vill säga word = "f" + word[1:]

## Strängmetoder

- Ändra skiftläge, .lower() och .upper() konverterar text till gemener eller versaler
- Ta bort blanksteg, .strip() tar bort blanksteg från både början och slutet, medan .lstrip() och .rstrip() tar bort från vänster respektive höger sida
- Kontrollera början/slut, .startwith() och .endwith() returnerar Boolean-värden (True eller False) och är skiftlägeskänsliga
- Metoder ändrar inte originalsträngen utan returnerar alltid en ny modifierad kopia

## Användarinput och konvertering mellan strängar och tal

- Funktionen input() hämtar text från användaren och returnerar alltid resultatet som en sträng
- Aritmetik med strängar, att addera två siffersträngar konkatenerar de ("2" + "2" = "22"), mdan multiplikation med ett heltal upprepar strängen ("12" * 3 blir "121212")
- Konverteringsfunktioner, int() och float() omvandlar siffersträngar till heltal eller flyttal, medan str() omvandlar tal och andra objekt till strängar

## Formatering och sökning i strängar

- f-strings, genm att sätta ett f framför strängen (till exempel f"{namn} är {ålder} år") kan du enkelt bädda in variabler och uttryck direkt i måsvingar
- .find(), söker efter en delsträng och returnerar indexet för den första förekomsten, eller "-1" om delsträngen inte hittas
- .replace(), ersätter alla förekomster av en delsträng med en anna text

---

## Frågor

Vad händer om du försöker ändra det första tecknet i en sträng med s = "A" och varför uppstår det felet?

- Antag s = "BBCD". Om s[0] = "A" så blir det TypeError, eftersom strängar är oföränderliga, vilket innebär att de inte kan ändras

Vad blir resultatet av uttrycket "3" * 3 i Python?

- Det blir "333"

Vilket index returnerar metoden .find() om delsträngen du söker efter inte existerar i strängen?

- Metoden returnerar -1 om delsträngen inte hittats