# 12.1. Filer och filsystemet
"""
Varför behövs filer?
Tidigare har indata kommit från programmet självt eller från användaren via IDLE.
Filer behövs när:

1. Indatavärdena är okända när programmet skrivs.
2. Programmet hanterar mer data än vad en användare rimligen kan skriva in manuellt.
3. Utdata måste sparas och delas med andra efter att programmet har körts klart.

---

Filens anatomi:

- En fil är i sin grundläggande form en sekvens av bytes (heltal mellan 0 och 255) som utgör filens innehåll.
- Det finns ingenting i själva filen som dikterar hur dessa bytes ska tolkas.
Det är programmerarens uppgift att tolka innehållet korrekt när filen öppnas (t.ex, som text, bild eller ljud).

---

Filsystemet och dess hierarki:

- Filsystemet tillhandahåller en abstrakt representation av filer på datorn och styr lagring och hämtning av data.
- Filer organiseras i en hierarki av mappar/kataloger (directories/folders) med rotsöksvägen (root directory) högst upp.
- Sökvägar (file paths) skrivs olika beroende på operativsystem:
  - Windows: C:\\Users\\David\\Documents\\hello.txt
  - macOS: /Users/David/Documents/hello.txt
  - Ubunto Linux: /home/david/documents/hello.txt
"""