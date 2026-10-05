# 5. Siffror och matematik

## 5.1 Heltal och flyttal

Python har tre inbyggda taltyper:

- Heltal, int
- Flyttal, float
- Komplexa tal, complex

Heltal (int) är hela tal utan decimaler. Det finns ingen övre gräns för hur stora heltal Python kan hantera i minnet. För att göra stora tal lättare att läsa kan understreck ( _ ) användas som tusentalsavgränsare.

```python
type(1)
int("25") # Typecast "25" to 25
a = 1000
b = 1_000
```

Flyttal (float) är tal med decimalpunkter. Flyttal kan skrivas direkt, konverteras med float(), eller skrivas med understreck (till exempel, 1_000_000.0).

```python
type(1.0)
float("1.11") # Typecast "1.11" to 1.11
a = 1000.01
b = 1_000.01
c = 1e6 # 1000000.0
d = 1e-4 # 0.0001
```


E-notation (vetenskaplig notation) används vid skrivning av stora eller mycket små flyttal, till exempel 1e6 (1 x 10^6 = 1000000.0) eller 1e-4 (0.0001). Tal som överstiger Pythons maximala flyttalgräns returnerar (inf) eller (-inf).

## 5.2 Aritmetiska operationre och uttryck

De grundläggande aritmetiska operatorerna är:

- Addition och Subtraktion
- Multiplikation
- Division
- Heltalsdivision
- Upphöjt till
- Modulus eller Rest-operatorn
- Prioritetsregler och PEP 8

Addition ( + ) och Subtraktion ( - ) av två heltal ger ett heltal, men om en operand är ett flyttal blir resultatet ett flyttal. Paranteser rekommenderas för tydlighet vid negativa tal.

Multiplikation ( * ) följer samma typregler som addition och subtraktion.

Division ( / ) returnerar alltid ett flyttal, även om divisionen går jämnt ut. Division med noll kastar ett "ZeroDivisionError".

Heltalsdivision ( // ) dividerar och avrundar nedåt till närmaste heltal. Observera att negativa tal avrundas nedåt bort från noll.

Upphöjt till ( ** ) används för potenser. Kan även användas med flyttal för till exempel kvadratrot eller negativa exponenter.

Modulus / Rest-operatorn ( % ) returnerar resten vid division. Den används ofta för att kontrollera om ett tal är jämnt delbart med ett annat (till exempel n % 2 == 0).

## 5.5 Matematiska funktioner och metoder för siffror

Tre inbyggda funktioner och en flyttalsmetod är:

- round(number, ndigits)
- abs(number)
- pow(x, y)
- .is_integer()

round(number. ndigits) avrundar till närmaste heltal eller angivet antal decimaler (till exempel round(3.14159, 3) ger 3.142). Python tillämpar banker´s rounding (avrundning mot jämna tal vid exakta halvtal).

```python
round(2.3) # 2
round(2.7) # 3
round(2.5) # 2
round(3.5) # 4
round(3.14159, 3) # 3.142
round(2.71828, 2) # 2.72
```

abs(number) returnerar absolutbeloppet (avståndet från noll) som ett positivt tal av samma typ (till exempel, abs(-5.0) blir 5.0).

pow(x, y) beräknar (x ** y). Om ett tredje argument z skickas med beräknas (x ** y) % z mer effektivt.

```python
pow(2, 3) # 8
pow(2, -2) # 1/4
pow(2, 3, 2) # 0 because 2 ** 3 % 2 is 0
```

.is_integer() är en metod på flyttalsobjekt som returnerar "True" om flyttalet inte har någon decimaldel (till exempel 2.0.is_integer() ger True, medan 2.5.is_integer() ger False). Denna metod är användbart för validering av indata.

## 5.6 Skriva siffror med i stil

Formatering av tal i f-sträng med Pythons formateringsspråk:

- Avrundade decimaler {n:.2f} visar talet som fixpunkt med 2 decimaler
- Tusentalsavgränsare {n:,} lägger till kommatecken
- Valutaformatering kombinerar båda som {n:,.2f} (till exempel, $1,743.65)
- Procent {ratio:.1%} multiplicerar talet med 100 och lägger till ett procenttecken med 1 decimal (0.9 visas som 90.0%)

```python
n = 7.125
print(f"The value of n is {n}") # The value of n is 7.125
print(f"The value of n is {n:.2f}") # The value of n is 7.12
n = 7.126
print(f"The value of n is {n:.2f}") # The value of n is 7.13
print(f"The value of n is {n:.1f}") # The value of n is 7.1
n = 123456788
print(f"The value of n is {n:,}") # 123,456,788
n = 1234.56
print(f"The value of n is {n:,.2f}") # 1,234.56
n = 0.9
print(f"Over {n.1%} of Pythonists say 'Real Python rocks!'") # Over 90% of Pythonists say 'Real Python rocks!'
```

## 5.7 Komplexa tal

Python har inbyggt stöd för komplexa tal:

- Imaginärdelen skrivs med "j" eller "J" (till exempel, n = 1 + 2j)
- Egenskaperna .real och .imag hämtar reell respektive imaginär del som flyttal
- Metoden .conjugate() returnerar det komplexa konjugat
- De flesta aritmetiska operatorer fungerar med komplexa tal, men heltalsdivision ( // ) kastar ett "TypeError"

---
