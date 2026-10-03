# Laboration 1 - Krav
PROMPT = input("Enter your credentials: ")
credentials = PROMPT
username = credentials[:credentials.find(" ", credentials.find(" ") + 1)] # credentials.find(" ", credentials.find(" ") + 1) letar efter indexet för det andra mellanslaget i **credentials**. Det innebär att uttrycket "slice"ar fram till indexet för det andra mellanslaget, vilket ger oss **username**
password = credentials[credentials.find(" ", credentials.find(" ") + 1) + 1:] # Samma logik som ovan, men istället för att "slice"a fram till indexet för det andra mellanslaget, så "slice"ar uttrycket från det index + 1 istället och fram till slutet av **credentials**, vilket ger oss **password**
formatted_username = (username[:username.find(" ")][0].upper()) + (username[:username.find(" ")].lower()[1:]) + "_" + (username[username.find(" ") + 1:][0].upper()) + (username[username.find(" ") + 1:].lower()[1:]) # Som jag har tolkat uppgiften så får vi endast formattera inmatningen här... Det är därför det ser ut på följande sätt. Sedan så vet jag inte heller om .split()-metoden är okej att använda fast den finns nämnd i "Additional Resources" under kapitel 4
print(f"Welcome, Agent {formatted_username}!")
