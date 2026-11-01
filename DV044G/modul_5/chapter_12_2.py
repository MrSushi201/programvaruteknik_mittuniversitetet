# 12.2. Sökvägar i Python med pathlib
"""
Standardbibliotekets modul pathlib används för att hantera sökvägar plattformsoberoende:
'''python
import pathlib
'''
Modulen innehåller klassen Path som representerar en sökväg.

---

Skapa Path-objekt:

Det finns tre huvudsakliga sätt att skapa ett Path-objekt:

1. Från en sträng.
2. Med klassmetoder som Path.home() och Path.cwd().
3. Med / operatorn.

Från en sträng:
'''python
import pathlib
path = pathlib.Path("/Users/Santi/Documents/hello.txt")
'''
Windows-hantering:
Om du använder bakåtstreck "C:\\Users\\David\\Desktop\\hello.txt" tolkas det som en escape-sekvens och kastar ett SyntaxError.
Lös det genom att använda framåtsreck eller råa strängar:
'''python
import pathlib
path1 = pathlib.Path(r"C:\\Users\\David\\Desktop\\hello.txt")
path2 = pathlib.Path("C:/Users/David/Desktop/hello.txt")
'''

Med klassmetoder som Path.home() och Path.cwd():
'''python
home1 = pathlib.Path.home()
home2 = pathlib.Path.cwd()
print(home1) # WindowsPath("C:\\Users\\David")
print(home2) # WindowsPath(r"C:\\USers\\David\\Documents")
'''
Path.home() returnerar sökvägen till användarens hemmamapp.
Path.cwd() returnerar den aktuella arbetskatalogen.

Med / operatorn:
Operatorn används för att koppla samman ett Path-objekt på vänster sida med en sträng eller ett annat Path-objekt på höger sida:
'''python
import pathlib
home = pathlib.Path.home()
filename = "hello.txt"
path = home / "Desktop" / filename
'''

---

Absoluta vs. relativa sökvägar:

- En absolut sökväg börjar från rotkatalogen
- En relativ sökväg utgår från en annan katalog

'''python
# Relativ Windows-sökväg
path = pathlib.Path(r"Photos/image.jpg")

# Relativ macOS- eller Linux-sökväg
path = pathlib.Path("Photos/image.jpg")
'''

- Metoden .is_absolute() returnerar True eller False.
- Du kan slå ihop en absolut och relativ sökväg med /

'''python
home = pathlib.Path.home()
print(home / pathlib.Path(r"Photos\\iamge.png"))
'''

---

Komponenter i en sökväg

'''python
path = pathlib.Path.home() / "hello.txt"

# Lista upp alla föräldrakataloger upp till roten
print(list(path.parents))

# Skriv ut närmaste föräldermapp
print(path.parent)

# Skriv rotkatalogen som en sträng. Returnerar en tom sträng '' för relativa sökvägar
print(path.anchor)

# Skriv ut hela namnet på filen eller mappen
print(path.name)

# Skriv ut filnamnet utan ändelse
print(path.stem)

# Skriv ut filändelsen inklusive punkt
print(path.suffix)
'''

---

Kontrollera om en sökväg finns

'''python
path = pathlib.Path.home() / "hello.txt"

# Kontrollera om sökvägen finns. Returnerar True om sökvägen finns
print(path.exists()) 

# Kontrollera om sökvägen pekar på en fil. Returnerar True om sökvägen pekar på en fil
print(path.is_file())

# Kontrolera om sökvägen pekar på en katalog
print(path.is_dir())
'''

"""

import pathlib

# path = pathlib.Path("/Users/Santi/Documents")

# print(path)

# path1 = pathlib.Path(r"C:\\Users\\David\\Desktop\\hello.txt")
# path2 = pathlib.Path("C:/Users/David/Desktop/hello.txt")

# print(path1)
# print(path2)

# home1 = pathlib.Path.home()
# home2 = pathlib.Path.cwd()

# print(home1) # WindowsPath("C:\\Users\\David")
# print(home2) # WindowsPath(r"C:\\USers\\David\\Documents")

# home = pathlib.Path.home()
# filename = "hello.txt"
# path = home / "Desktop" / filename

# print(path)

# # Relativ Windows-sökväg
# path = pathlib.Path(r"Photos/image.jpg")

# print(path)

# # Relativ macOS- eller Linux-sökväg
# path = pathlib.Path("Photos/image.jpg")

# print(path)

# home = pathlib.Path.home()
# print(home / pathlib.Path(r"Photos\\image.png"))

# path = pathlib.Path.home() / "hello.txt"

# # Lista upp alla föräldrakataloger upp till roten
# print(list(path.parents))

# # Skriv ut närmaste föräldermapp
# print(path.parent)

# # Skriv rotkatalogen som en sträng. Returnerar en tom sträng '' för relativa sökvägar
# print(path.anchor)

# # Skriv ut hela namnet på filen eller mappen
# print(path.name)

# # Skriv ut filnamnet utan ändelse
# print(path.stem)

# # Skriv ut filändelsen inklusive punkt
# print(path.suffix)

path = pathlib.Path.cwd() / "chapter_12_2.py"

print(path)

# Kontrollera om sökvägen finns. Returnerar True om sökvägen finns
print(path.exists()) 

# Kontrollera om sökvägen pekar på en fil. Returnerar True om sökvägen pekar på en fil
print(path.is_file())

# Kontrolera om sökvägen pekar på en katalog
print(path.is_dir())