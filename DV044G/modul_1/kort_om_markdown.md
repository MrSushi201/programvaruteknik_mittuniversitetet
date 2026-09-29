# Kort om Markdown

Markdown är ett språk för att lägga till formateringselement i textdokument. Dokumenten sparas oftast med filändelsen ".md" eller ".markdown" och omvandlas av en markdown-processor till HTML för visning i webbläsare eller konvertering till format som PDF.

---

## Varför Markdown används

Markdown är platformsoberoende och framtidssäkert. Det används inom en mängd områden:

- Webbplatser och dokumentation, används ofta tillsammans med webbplatsgenerator som Jekyll, MkDocs eller Docusaurus
- README-filer, fungerar som standard för projektbeskrivningar i kodbas eller kodförråd som GitHub
- Anteckningar och dokument, stöds av anteckningsappar som Obsidian, Simplenote, iA Writer och Joplin
- Böcker, presentationer och e-pos, kan omvandlas till e-böcker via Leanpub, bildspel via Marp/Remark eller snygga e-postmeddelanden

---

## Översikt över grundläggande syntax

### Rubriker

Skapas genom att placera 1 till 6 fyrkantsmärken "#" framför texten beroende på rubriknivå:

- "# Rubrik nivå 1"
- "## Rubrik nivå 2"
- "### Rubrik nivå 3"

Placera alltid ett mellanslag mellan "#" och rubriktexten, samt tomma rader före och efter rubriken för maximal kompatibilitet mellan olika apparattyper. Alternativt kan nivå 1 och 2 skapas med "=" eller "--" på raden under texten.

### Textformatering

- Kursiv text *text* eller *text*
- Fet text **text** eller **text**
- Fet och kursiv text ***text*** eller ***text***
- Genomstruken text ~~text~~

### Stycken och radbrytningar

- Stycken, skapas genom att lämna en tom rad mellan textblock. Stycken ska inte indenteras med mellanslag eller tabbar
- Radbrytning, skapas genom att avsluta en rad med två eller fler mellanslag, eller genom att använda HTML-taggen ( br )

### Listor

- Numrerade listor, skriv siffror följda av punkt (till exempel 1. Första punkten)
- Onumrerade listor, använd bindestreck ( - ), stjärnor ( * ) eller plus-tecken ( + )
- Checklistor, använd - [ ] för ej ikryssad ruta eller - [x] för ikryssad

### Citatblock

- Skapas med ett större-än-tecken ( > ) framför raden. Citat kan även nästlas med ( >> ) eller innehålla andra formateringselement

### Kod

- Kod i löpande text, omsluts med enkla backsticks `kod``
- Kodblock, indentera raderna med fyra mellanslag eller en tabb, eller omslut hela blocket med tre backsticks ( ``` )

### Länkar och bilder

- Länkar, [ länktext ] ("url")
- Referenslänkar, delar upp länken i textdelen [ länktext ] och url-definitionen
- Bilder, inleds med ett utropstecken ![ alt-text ]

### Tabeller och avdelare

- Tabeller, skapas med vertikala staplar ( | ) och bindestreck ( - ) för att skilja rubrikraden från innehållet
- Vågrät linje, skapas med tre eller fler stjärnor ( *** ), bindestreck ( --- ) eller understreck ( ___ ) på egen rad

### Escaping av tecken

- Om du vill visa ett tecken som annars tolkas som formatering (till exempel ( * ) eller ( # )), sätter du en backslash ( \ ) framför tecknet

---

## Varianter

Det är värt att hålla i åtanke att olika verktyg och plattformar implementerar olika varianter ("flavors") av Markdown. Grundsyntaxen stöds nästan överallt, men utökade funktioner som tabeller eller kodblock kan skilja sig något beroende på vilken processor som används.

---
