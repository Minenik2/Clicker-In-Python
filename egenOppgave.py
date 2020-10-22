from egenOppgaveClassHero import Hero
from egenOppgaveClassFriendship import FriendshipManager

# NEW FEATURE:
# Du kan nå bli venn med heltene du møter! Snakk med dem og hvis det viser seg at helten liker
# responsen din så øker friendship level. Ved friendship level 5 så kan du gi dem kallenavn!
# Hvem trenger venner i virkeligheten uansett ¯\_(ツ)_/¯
# Programmering:
# Klikkeren bruker nå en klasse system for å holde til variabler, ved dette blir det enklere å
# jobbe med nye muligheter for spillutvikling og siden vi later som om variablene ikke kan
# bli akksesert publicly betyr det også at variablene er mer sikret 👀👀👀

# Oppgave:
# lag en clicker (videospill) der brukeren kan gå i krig og skaffe seg penger.
# brukeren kan bruke disse pengene på helter som fører til at intekten hans øker per krig.
# lag også en mulighet for brukeren å see alle heltene han har kjøpt.
# når brukeren kjøper en ny helt skal prisen til den neste helten av samme type øke.
# ha ulike type helter som gir ulike mengder penger per krig.
# gi brukeren muligheten til å kunne lagre data på en fil,
# programmet skal kunnne lese daten for å kunne laste opp brukerens progresjon fra forrige session

# NY OPPGAVE: bruk klasser til å sette verdier på helter, med en innkapsling metode (ikke public variabler)
# plasser klassen i eget .py fil og hent klassen den via 'from x import y'


def lagreData(heroListe, penger):  # funksjon for a lagre data
    fil = open("saveData.csv", "w")  # filen der dataen blir lagret
    fil.write("penger-" + str(penger) + "\n")
    fil.write("friendship")
    for x in friendList:
        fil.write(f", {x.returnAllForSave()}")
    fil.write("\n")
    for x in heroListe:
        fil.write(str(x.returnAllForSave()) + "\n")
    print("data lagret!")


def lasteData(heroListe, valg):  # funksjon for å laste data
    fil = open("saveData.csv")  # filen der dataen blir lastet fra
    for i, linje in enumerate(fil):  # går gjennom filen
        # hvis vi har valgt at vi skal bare ha pengeverdien
        if linje[0:6] == "penger" and valg == "penger":
            linje = linje.split("-")
            penger = int(linje[1])
            return penger  # returnerer pengerverdien fra filen hvis vi har valgt penger
        elif linje[0:10] == "friendship":
            linje = linje.split(",")
            k = 1
            for x in friendList:
                x.changeFriendship(int(linje[k]))
                k += 1
        # hvis vi ikke valgte å laste opp penger
        elif linje[0:6] != "penger":
            # deler opp linjen i en array med innhold for vær verdi
            linje = linje.replace("\n", "")
            linje = linje.split(",")

            i -= 2  # fordi den første linjen er penge-verdien tar vi den ikke med i index tellingen
            heroListe[i].changeName(linje[0])
            heroListe[i].changeLvl(int(linje[1]))
            heroListe[i].changeCost(int(linje[2]))
            heroListe[i].changePower(int(linje[3]))


def erDuSikker(handling, warning):  # en sikkerhet melding for fremtidige meldinger til brukeren
    print("Er du sikker på at du vil " + handling + "? " + warning)
    print("1.Ja\n2.Nei")
    svar = input()
    return svar


def kalleNavnFeilmelding(kallenavn):
    if kallenavn == "friendship":
        kallenavn = input(
            "Skriv nytt kallenavn her (kallenavn 'friendship' vil ødelegge lagrekoden): ")
        kalleNavnFeilmelding(kallenavn)
    return kallenavn


penger = 0  # definerer variabel for penger
personalityList = ["gamer", "philosophical", "modest"]
heroListeNavn = ["Metallica", "Beatles", "R.E.M", "Red Hot Chilli Peppers",
                 "Nirvana", "AC/DC"]  # liste med helter som vi vil ha i spillet
heroListeRoller = ["Warrior", "Mage", "Priest", "Hunter",
                   "Monk", "Druid"]  # liste med ulike klasser
assert len(heroListeNavn) <= len(
    heroListeRoller), "For lite heltRoller! Vennligst legg til mer heltRoller i 'heroListeRoller'!"
costNewHero = 5  # costNewHero bestemmer hvor mye helten koster
powerNewHero = 1  # powerNewHero er med på å bestemme hvor mye penger helten gir per kamp

friendList = []  # definerer liste på venner
heroListe = []  # definerer liste på helter

# heroListe = [Hero(name, lvl, cost, power), Hero(name, lvl, cost, power), Hero(name, lvl, cost, power)]
i = 0
for x in heroListeNavn:
    # lager helten og putter den i heroListen
    heroListe.append(
        Hero(x, 0, costNewHero, powerNewHero, heroListeRoller[i]))
    i += 1
    costNewHero = round(costNewHero * 2.5)  # øker prisen til den neste helten
    if costNewHero > 5000:  # hvis prisen til helten er over 5000
        # skaler kraften til helten med prisen
        powerNewHero = round(costNewHero * 0.002)
    else:
        powerNewHero += 1  # else: adder kraften

# friendListe = [FriendManager(personality, name, friendship), ... , ...]
i = 0
k = 0  # k teller friendList[k] idexen
for x in heroListe:
    if i == len(personalityList):
        break  # man kan kutte ut break for at den skal gjenta seg for evig, og da vil vær helt for en presonality, men da vil også personality gjenta seg
        i = 0
    # lager personlighet til heltene og putter dem i egen liste, en egen klasse har ansvar for bare friendship stats
    friendList.append(FriendshipManager(
        personalityList[i], heroListe[k].returnName(), 0))
    i += 1
    k += 1


print("Hei hvis du har spilt clikkere før så blir dette enkelt å forstå\nVil du gå gjennom tutorial?")  # tutorial
choose = input("Skriv 1 \n1.yes \n2.no\n")
if choose == "1":
    print("\n\n\nDette videospillet handler om et tall, mer spesifikt dine penger.\nBruk penger til å tjene mer penger fordi sånn er livet\nTjen så mye penger du klarer!")
    print("Du har 3 muligheter: krige (1) det gir deg penger, sjekke dine stats (2) blant annet hvor mye penger du har, eller kjøpe mer helter (3) de gir deg mer penger")


def spillet(penger, heroListe):  # funksjon for hele spillet
    print("Dine penger: " + str(penger))
    print("1.krig\n2.sjekk stats\n3.kjøp mer helter\n4.friendship\n5.Lagre/laste Data")
    choose = input()
    if choose == "1":  # 1.krig
        nyPenger = 1
        for x in heroListe:
            # beregner poeng : heroListe.lvl * heroListe.power
            nyPenger += x.returnLvl() * x.returnPower()
        penger += nyPenger
        # skriver ut hvor mye penger brukeren fikk
        print("\n\n\nDu fikk " + str(nyPenger) + " penger ut av krigen!")
    elif choose == "2":  # 2.skjekk stats
        print("\n\n\nDine penger: " + str(penger))
        print("Dette viser dinne medlemmer gjo mer helter du har gjo mer penger kan du få!")
        print("Lvl: hvor høyt lvl din helt er, Cost: hvor mye det koster å lvle opp helter, Power: kraften til helten din")
        print("gjo større disse tallene er gjo bedre!")
        for x in heroListe:
            print(x.returnAll())
    elif choose == "3":  # 3.kjøp mer helter
        print("\n\n\nVelg hvem du vil kjøpe")
        print("Dine penger: " + str(penger))
        i = 1
        for x in heroListe:  # printer ut heltene som brukeren kan kjøpe
            print(str(i) + ". '" + x.returnName() + "' cost: " +
                  str(x.returnCost()) + " penger")
            i += 1
        choose = input()
        i = 1
        for x in heroListe:
            if choose == str(i):  # sjekker om brukeren ønsker å kjøpe helten
                # sjekker hvis brukeren har pengene : heroListe.cost
                if penger >= x.returnCost():
                    # fjerner penger fra brukeren
                    penger = penger - x.returnCost()
                    # øker prisen til det brukeren kjøpte slik at den blir dyrere neste gang brukeren kjøper det
                    # heroListe.cost = round(heroListe.cost * 1.2) // visualisere
                    x.changeCost(round(x.returnCost() * 1.2))
                    # heroListe.lvl += 1 // visualisere
                    x.changeLvl(x.returnLvl() + 1)  # øker level til helten
                    print("\n\n\ndu kjøpte " + x.returnName() + "!")
                    break
                else:
                    # hvis brukeren ikke har penger skriver ut feilmelding
                    print("\n\n\ndu har ikke nokk penger :C")
                    break
            i += 1
    elif choose == "4":  # Friendship
        print("\n\n\nVelg om vil snakke med helter eller gi nytt navn")
        print("1.snakk med helter\n2.gi nytt navn til helter")
        choose = input("")
        if choose == "1":  # snakk med helter
            print("\n\n\nVelg hvem du vil snakke med")
            print("Dine penger: " + str(penger))
            i = 1
            k = 0  # k teller frienList[k] idexen
            for x in heroListe:  # printer ut heltene som brukeren kan kjøpe
                print(str(i) + ". '" + x.returnName() + "' Friendship: " +
                      str(friendList[k].returnFriendship()) + "/10" + " Personality: " + friendList[k].returnPersonality())
                i += 1
                k += 1
                if k >= len(friendList):
                    break
            choose = input()
            i = 1
            k = 0  # k teller frienList[k] idexen
            for x in heroListe:
                if choose == str(i):  # sjekker om brukeren ønsker å snakke med helten
                    if x.returnLvl() > 0:
                        friendList[k].talk()  # hvis ja kjører snakk funksjonen
                    else:
                        print("Beklager du må kjøpe helten først :c")
                i += 1
                k += 1
                if k >= len(friendList):
                    break
        elif choose == "2":
            print("\n\n\nVelg hvem du vil gi et nytt kallenavn til")
            print("NB: Friendship må være 5 eller høyrere")
            i = 1
            k = 0  # k teller frienList[k] idexen
            for x in heroListe:  # printer ut heltene som brukeren kan kjøpe
                print(str(i) + ". '" + x.returnName() + "' Friendship: " +
                      str(friendList[k].returnFriendship()) + "/10" + " Personality: " + friendList[k].returnPersonality())
                i += 1
                k += 1
                if k >= len(friendList):
                    break
            choose = input()
            i = 1
            k = 0  # k teller frienList[k] idexen
            for x in heroListe:
                if choose == str(i):  # sjekker om brukeren ønsker å snakke med helten
                    if friendList[k].returnFriendship() >= 5:
                        # hvis ja kjører endrer navn
                        nyttKallenavn = input("Skriv nytt kallenavn her: ")
                        x.changeName(kalleNavnFeilmelding(nyttKallenavn))
                    else:
                        print("Beklager du må ha minst 5/10 friendship med helten :c")
                i += 1
                k += 1
                if k >= len(friendList):
                    break

    elif choose == "5":  # lagre eller laste opp spillet
        print("\n\n\nVil du lagre eller laste dataene dine?")
        print("1.lagre\n2.laste")
        choose = input("")
        if choose == "1":
            if erDuSikker("lagre spillet", "Allerede lagret informasjon går tapt") == "1":
                lagreData(heroListe, penger)  # lagrer data
        elif choose == "2":
            # overskriver klasse verdier med nye verdier
            lasteData(heroListe, "helter")
            # overskriver penger med ny verdi
            penger = lasteData(heroListe, "penger")
            print("Data lastet!")
    spillet(penger, heroListe)  # fotsetter spillet


spillet(penger, heroListe)  # starter spillet
