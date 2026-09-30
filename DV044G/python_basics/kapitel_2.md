# 2. Installation av Python

## System Python vs. Fristående installation

- Många operativsystem (som macOS och Linux) levereras med en förinstallerad version som kallas **system Python**. Denna version är ofta föråldrad eller ofullständig, så det är avgörande att installera den senaste officiella versionen av Python 3
- Författarna varnar för att alternativa installationer (som Anaconda eller Homebrew) kan orsaka kompatibilitetsproblem med bokens framtida kodexempel

## Installationssteg för olika operativsystem

- Windows, du laddar ned installeraren från python.org. Det absolut viktigaste steget är att bocka i rutan "Add Python 3.x to PATH" under installationen så att kommandotolken hittar verktygen. Därefter öppnas IDLE från Startmenyn
- macOS, du laddar ned den officiella macOS-installeraren från python.org. IDLE starts sedan via Finder (Program/Application) eller via Spotlight (Cmd + Spacebar och sök på "IDLE")
- Ubuntu Linux, installeras smidigast via terminalen och pakethanteraren med kommandot "sudo apt-get install python3.x idle-python3.x". IDLE startas sedan med kommandot "idle-python3.x" eller "idle3"

## Inledning till IDLE och Python Shell

- IDLE står för Integrated Development and Learning Environment och följer med som Pythons inbyggda utvecklingsmiljö
- När IDLE öppnas möts du av en Python Shell (den interaktiva miljön)
- Symbolen ">>>" kallas för en prompt och indikerar att Python väntar på att få instruktioner från dig

---

## Frågor

Varför rekommenderar boken att du installerar en ny Python 3-version istället för att förlita dig på ditt operativsystems "system Python"?

- För att "system Python" kan vara föråldrad vilket medför kompabilitetsproblem för framtiden

Vilken ruta i installeraren måste du komma ihåg att bocka i när du installerar på Windows?

- Det är "Add Python 3.x to PATH"-rutan

Vad kallas symbolen ">>>" i IDLE och vad signalerar den?

Den kallas för en prompt och indikerar att Python väntar på instruktion från en användare

---
