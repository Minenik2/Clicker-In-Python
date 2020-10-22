import random


class FriendshipManager():
    def __init__(self, personality, name, friendship):  # konstruktør
        self.friendship = friendship
        self.name = name
        self.personalityType = personality
        if personality == "gamer":
            self.quiz = [["Tenker du at spill burde bli designet for spillerne eller for å tjene mest penger?",
                          ["Hvordan kan et spill funke uten brukere?",
                           "Uten penger så vil spillutviklere sulte!"], 1,
                          "Enig hvis ingen liker spillet, så vil ingen spille det, og derfor vil det miste inntekten uansett",
                          "Oh, ja.. det er en måte å tenke på..."
                          ], ["Hva synes du er en viktig del i et spill?",
                              ["Hvis spillet har en form for gambling der jeg kan betale ekte penger og få 0.06% sjanse for å ha det gøy så er det nokk for meg",
                               "Spillet må inneholde utforskning, der spilleren har en mulighet til å finne noe nytt og oppdage verden rundt seg som spilleren befinner seg i"
                               ], 2,
                              "Det er en av de gode sidene ved videospill, du kan finne ut noe fantastisk i spillet og dermed kansje finne noe fantastisk om deg selv",
                              "spill skal ikke være en form for å forstærke en lidelse"]]
        elif personality == "modest":
            self.quiz = [["Liker du å koke mat hjemme?",
                          ["Jeg klarer ikke å lage mat, bestiller alltid pre-lagdt mat eller går ut til restaurant",
                           "Jeg elsker å lage mat hjemme, det er alltid så mange ulike oppskrifter man kan finne"
                           ], 2, "Enig! Mat er best når den er hjemmelaget",
                          "Jeg kan tenke meg at å bestille mat er ikke så dårlig"],
                         "Tar du alltid en kopp kaffe om morningen?",
                         ["Ja, kaffe på morningen er det beste for å putte meg i topp form!",
                          "Nei, jeg liker ikke smaken av kaffe, spesielt om morningen"], 2,
                         "Jeg klarer bare ikke å drikke mørk kaffe i det hele tatt >-<",
                         "oh det er kult at noen kan sette pris på kaffe :/"
                         ]

        elif personality == "philosophical":
            self.quiz = [["Mennesker tenker alltid på en futuristic utopia, men hva om teknologien faktisk kom så langdt der man man kunne programmere minnene til mennesker?",
                          ["Det hadde vært fantastisk, man kunne ha husket på ting som var viktig og tenk alle de ulike talentene man kan mestre hvis man bare har over 10 år erfaring med en gang",
                           "Fælt, vi hadde begynt å straffe mennesker ved å slette minne, tenk å glemme hele live sitt og leve resten uten å ha husket. Eller værre finne ut at alle dinne minner har vært en løyn"], 2,
                          "Mennesket er et individ bare på grunn av sitt immaterielle minne. Men minne kan ikke defineres, men det definerer menneskeheten.",
                          "Uansett hvordan du ser på det, er all informasjonen som en person akkumulerer i løpet av en levetid bare en dråpe i bøtta."
                          ], ["Uansett hvor du går, så er alle tilkoblet",
                              ["Objektet lever så lenge det er en variabel som husker på dem",
                               "Uhmmmmm... ok, dette er ikke noe for meg"
                               ], 1,
                              "hvis du ikke blir husket, eksisterte du aldri",
                              "jeg bare stiller spørsmål det er ditt valg å finne svaret"]]
        else:
            self.personalityType = "notInDatabase"
            self.friendship = -1

    def returnPersonality(self):
        return self.personalityType

    def talk(self):
        print(f"{self.name}: '{self.quiz[0][0]}'")
        i = 1
        # k blir satt random for at det skall koppe opp et random spørsmål
        k = random.randint(0, len(self.quiz) - 1)
        for x in self.quiz[k][1]:
            print(f"{i}. {x}")
            i += 1
        choose = input("")
        print("riktig svar", self.quiz[k][2])
        if choose == str(self.quiz[k][2]):
            print(f"{self.name}: '{self.quiz[k][3]}'")
            if self.friendship < 10:
                self.friendship += 1
            print(f"Friendship increased! {self.friendship}/10")
        else:
            print(f"{self.name}: '{self.quiz[k][4]}'")
            print(f"Personen likte ikke svaret :c")

    def changeFriendship(self, friendship):
        self.friendship = friendship

    def returnFriendship(self):
        return self.friendship

    def returnAllForSave(self):
        return self.friendship
