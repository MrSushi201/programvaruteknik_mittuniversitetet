# 9. Tupler, listor och dictionarier
"""
9.1. Tupler
En sekvens är en ordnad lista av värden där varje element
tilldelas ett heltalsindex som börjar på 0. Både strängar och tupler är sekvenser.

Vad är en tupel?
Namnet härstammar från matematiken där det betecknar en ändlig, ordnad sekvens av värden.
Tupler kan innehålla vilken datatyp som helst och kan blanda olika datatyper i samma tupel.
T.ex. (1, 2.0, "three").

Skapa tupler:
- Tupelliteral: skrivs med kommateckenseparerade värden inom parenteser
tup1 = (1, 2, 3)
  - Tom tupel: tup2 = () eller tup2 = tuple().
  - Enstaka element: kräver ett avslutande kommatecken, t.ex tup3 = (1, ).
  Skriver du (1) utan komma tolkar Python uttrycket som ett heltal.
- Den inbyggda funktionen tuple(): skapar en tupel från en itererbar sekvens.
T.ex. tuple("Python")som blir: tup3 = ("P", "y", "t", "h", "o", "n")
- Tuple Packing: värden separerade med komma packas automatiskt till en tupel även utan parenteser.
T.ex. coordinates = 4.21, 9.29

Egenskaper och operationer:
- Längd: funktionen len(tup1) returnerar antalet element
- Indexering och slicing: element hämtas med tup1[index], och delsekvenser med slice-notering
- Oföränderlighet (immutability): när en tupel väl har skapats kan dess element into ändras eller bytas ut. Att försöka tilldela ett nytt värde kastar TypeError
- Iteration: tupler är itererbara och kan loopas över med en for-loop

Tuple Unpacking och variabeltilldelning:
- Element i en tupel kan packas upp till enskilda variabler, t.ex. x, y = coordinates där coordinates = 1.2, 3.4
- Genom att kombinera packing och unpacking kan du göra flerfaldiga variabeltilldelningar på en rad.
T.ex. name, age, occupation = "Santi", 31, "Data Engineer"
- Undantag vid unpacking: antalet variabler måste stämma exakt överens med antalet element i tupeln:
  - För få värden, t.ex. a, b, c, d = 1, 2, 3 kastar ValueError
  - För många värden, t.ex. a, b, c = 1, 2, 3, 4 kastar ValueError
- Tillhörighetskontroll med "in":
  - Operatorn "in" returnerar True om elementet finns i tupeln och annars False (t.ex. "o" in vowels)
- Returvärden från funktioner:
  - Ett vanligt användningsområde för tupler är att returnerar flera värden från en funktion.
  T.ex. def adder_subtrater(num1, num2):
            return (num1 + num2, num1 - num2)
"""

# Skapa tupler
tup1 = (1, 2, 3)                                                # Skapa en tupel med hjälp av parenteser och kommateckan
print(type(tup1), tup1)
tup2 = ()                                                       # Skapa en tom tupel med paranteser
print(type(tup2), tup2)
tup3 = tuple()                                                  # Skapa en tom tupel med hjälp av tuple()
print(type(tup3), tup3)
coordinates = 4.21, 9.29                                        # Tuple Packing
x, y = coordinates                                              # Tuple Unpacking
print(type(coordinates), coordinates)
print(f"{type(x)}, x: {x}, {type(y)}, y: {y}")

# Egenskaper och operationer
print(len(tup1))                                                # Returnerar antalet element
print(tup1[2])                                                  # Returnerar elementet som ligger på indexet 2
print(tup1[1:3])                                                # Returnerar elementen som ligger mellan index 1 och 3 men inte 3
for _ in tup1:                                                  # Tupler är itererbara och kan loopas över med en for-loop
    print(_)

# Variabeltilldening
vowels = ("a", "e", "i", "u", "o")
print("x" in vowels)                                            # Tillhörighetskontroll med in
print("a" in vowels)                                            # Tillhörighetskontroll med in

"""
9.2. Listor
En lista är en ordnad sekvens av objekt indexerad från 0.
Den största skillnaden gentemot tupler är att listor är föränderliga (mutable).

Skapa listor:
- Listliteral: skrivs med hakparanteser [], t.ex. colors = ["red", "yellow", "green", "blue"]. En tom lista skapas med [].
- Den inbyggda funktionen list(): skapar en lista från en itererbar sekvens eller en tom lista list().
- Strängmetoden .split(): delar upp en sträng till en lista utifrån en avgränsare.
T.ex. "egg, milk, cheese".split(", ") ger ["egg", "milk", "chesse"]
Kan även dela på semikolon .split(";"), mellanslag .split(" ") eller flerteckenssträngar.

Ändra element i listor:
- Direkt indexering: värdet i en position ("slot") kan bytas ut direkt.
T.ex. colors[0] = "burgundy"
- Slice-tilldelning: flera element kan bytas ut samtidigt via slicing.
T.ex. colors[1:3] = ["orange", "magenta"]
  - Den tilldelade listans längd behöver inte matcha slicens längd: att tilldela 3 element till en slice med längd 2 förlänger listan.

Listmetoder (modifierar listan in-place):
- .insert(i, x): sätter in elementet x på index i och skjuter efterföljande element åt höger.
  - Om i är större än listans längd sätts elementet in i slutet.
  - Negativa index fungerar (t.ex. .insert(-1, "indigo") sätter in elementet före det sista).
  - Varning: metoden modifierar listan in-place och returnerar None. Skriver du colors = colors.insert() raderas variabelns innehåll till None
- .append(x): lägger till elementet x i slutet av listan (motsvarar .insert(len(colors), x))
- .extend(iterable): lägger till alla element från en itererbar sekvens i slutet av listan
- .pop(i): tar bort och returnerar elementet på index i (om inget index anges tas sista elementet bort).
Om indexet ligger utanför listans gränser/längds kastas IndexError.

Inbyggda funktioner för talkollektioner:
- sum(nums): beräknar summan av alla tal. Innehåller listan icke-numeriska element (som strängar) kastas TypeError.
- min(nums) och max(nums): returnerar minsta respektive största värdet. Fungerar även på tupler.

List Comprehensions:
- Ett kompakt sätt att skapa n ny lista utifrån en befintlig sekvens:
T.ex. squares = [num ** 2 for num in nums]
- Ersätter mönstret med att skapa en tom lista [], köra en for-loop och anropa .append()
. Kan även använas för typkonvertering: float_numers = [float(value) for value in str_numbers]
"""

colors = ["red", "yellow", "green", "blue"]
print(type(colors), colors)
empty_list1 = []                                                # Tilldela en tom lista med hakparenteser []
empty_list2 = list()                                            # Tilldela en tom lista med metoden list()

colors[0] = "burgundy"                                          # Byt ut värdet på index 0 mot "burgundy"
print(colors)
colors[1:3] = ["orange", "magenta"]                             # Byt ut värden från index 1 till 3 men inte 3 mot "orange" och "magenta"
print(colors)

colors.insert(-1, "indigo")                                     # Sätt in "indigo" i nästsista position
print(colors)
colors.append("something random")                               # Lägg till "something random" i slutet av listan
print(colors)
colors.extend([1, 2, 3])                                        # Lägger till alla element från en itererbar sekvens i slutet av listan
print(colors)
colors.pop()                                                    # Tar bort det sista elementet från listan
print(colors)

nums = [1, 2, 3, 4,]
print(sum(nums), min(nums), max(nums))                          # Summan av alla tal i listan, minsta värdet i listan, och största värdet i listan
squares = [num ** 2 for num in nums]                            # List Comprehension ersätter mönstret med att skapa en tom lista [], köra en for-loop och anropa .append()
print(type(squares), squares)
float_numbers = [float(value) for value in ["1.5", "2.3", "5.25"]]
print(type(float_numbers[1]), float_numbers)

# Övning

# 1. Skapa en lista food med two element "rice" och "beans"
food = ["rice", "beans"]

# 2. Lägg till "broccoli" till food med .append()
food.append("broccoli")
print(food)

# 3. Lägg till "bread" och "pizza" till food med .extend()
food.extend(["bread", "pizza"])
print(food)

# 4. Skriv ut två första element från food
print(food[0:2])

# 5. Skriv ut sista element från food
print(food[-1])

# 6. Skapa en lista breakfast från sträng "eggs, fruit, orange juice" using .split()
breakfast = "eggs, fruit, orange juice".split(", ")
print(breakfast)

# 7. Verifera att breakfast har längd 3
print(len(breakfast))

# 8. Skapa en ny lista lengths med list comprehension som innehåller längd för varje element från breakfast
lengths = [len(_) for _ in breakfast]
print(lengths)

"""
9.3. Nästling, kopiering och sortering

Nästlade listor och tupler:
- Listor och tupler kan innehålla andra listor och tupler som element
- Åtkomst sker med dubbel indexering
- Kan betraktas som en matris/tabell med rader och kolumner

Kopiering av listor:
- Direkt tilldelning (list1 = list2): skapar endast en ny referens till samma objekt i minnet. Ändringar i list2 påverkar även list1.
- Ytlig kopia (shallow copy) med [:]: large_cats = animals[:] skapar en ny lista med samma elementreferenser
- Beteende vid nästlade strukturer:
  - Om du gör en ytlig kopia av en nästlagd lista (matrix2 = matrix1[:]), kommer byte av en hel underlista i matrix2 inte påverka matrix1.
  Men ändrar du ett element inuti en nästlad underlista, ändras även matrix1, eftersom underlistans referens delas.
  För fullständigt oberoende krävs en djup kopia (Deep Copy).

Sortering av listor:
- .sort(): sorterar listan in-place i stigande alfabetisk eller numerisk ordning
- Parametern key: tillåter anpassad sortering via en funktion, t.ex. colors.sort(key=len) sorterar efter stränglängd.
- Egendefinierad sorteringsfunktion: man kan skicka in en funktion som tar exakt ett argument.
T.ex. def get_second_element(item):
        return item[1] och anropa items.sort(key=get_second_element) för att sortera en lista av tupler utifrån deras andra element
"""

# Nästlade listor och tupler
two_by_two = [[1, 2], [3, 4]]
print(len(two_by_two))
print(two_by_two[0])
print(two_by_two[1])
print(two_by_two[0][0])                                         # Dubbel indexering

# Kopiering av listor
animals = ["lion", "tiger", "frumious Bandersnatch"]
large_cats1 = animals                                            # Bara en alias eller ny referens till samma objekt
large_cats1.append("Tigger")
print(animals)                                                  # Därför finns Tigger med i den ursprungliga listan
print(large_cats1 == animals)
print(large_cats1 is animals)
large_cats2 = animals[:]
large_cats2.append("leopard")
print(large_cats2)
print(animals)

# Sortering av listor
def get_second_element(item):
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]
items.sort(key=get_second_element)
print(items)

# Övning

# 1. Skapa en tupel data med två värden (1, 2) och (3, 4)
data = ((1, 2), (3, 4))

# 2. Skriv en for-loop som loopar genom data och skriver ut summan för varje nästlad tupel
for i in range(len(data)):
    row = data[i]
    print(f"Row {i + 1} sum: {row[0] + row[1]}")

# 3. Skapa en lista numbers = [4, 3, 2, 1]
numbers = [4, 3, 2, 1]

# 4. Skapa en kopia av numbers
numbers_copy = numbers[:]

# 5. Sortera numbers i numerisk ordning med .sort()
numbers.sort()
print(numbers)
print(numbers_copy)