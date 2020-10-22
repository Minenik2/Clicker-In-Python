# Clicker-In-Python
An rpg clicker in python mainly coded in Norwegian.
You can go out and fight monster, the fight will give you money to upgrade heroes.
There's also a freindship mechanic were you can rename heroes names if you have high enough friendship with them.
To get high friendship level you will need to talk to them and give a proper answer that you think they will like.
You can see all the heroes you bought and upgrade heroes. You can also save data and load last saved data.

# Programming:
The clicker uses a class system to hold different variabels for heroes like cost, power and name.
You can easlity add more heroes and rename existing one by looking into the 'heroListeNavn' list.
This list takes in the names of the heroes you want to be in the game.
The other list is 'heroListeRoller' it assigns a role to each hero name you have. Make sure that
for each hero name you want to add there's also a corespoinding role for the hero.
The program will automatically assign numbers like cost, power and friendship level to
each hero. Each time you buy a new hero the cost to upgrade the hero increases and the
program does the calculations for you. If you wish to check out how these calculations 
are performed please look into line 94 to line 106 in egenOppgave.py

The cost of the next hero will always be 2.5 times more than the previus hero.
If the heros cost is over 5000 it's power will be 0.2% of it's cost.
When you buy a hero it's cost increases with 1.2 (120%) of it's previus cost

Friendship system was a little bit tricky to implement, I could have gone for a
more basic apporach with a pool of same questions being asked the player.
Instead I tried to make it interesting by using different personalities to ask different questions.
The questions can still repeat because I just haven't made enough of them.
I would redesign the whole friendship system to have like 10 basic questions for everyone
like, "do you like cooking?", "do you like studying?", "do you like training?" and then
have different responses for different personalities. All these questions are in a sense
a yes or no question and therefore it leads to simplictic implimentation of this system.
Think something along the lines of illusion games like in koikatsu party where you can
choose between a yes or no answer and the girl will increase happiness if she likes the response.


# Explained in Norwegian below:
NEW FEATURE:
Du kan nå bli venn med heltene du møter! Snakk med dem og hvis det viser seg at helten liker
responsen din så øker friendship level. Ved friendship level 5 så kan du gi dem kallenavn!
Hvem trenger venner i virkeligheten uansett ¯\_(ツ)_/¯
Programmering:
Klikkeren bruker nå en klasse system for å holde til variabler, ved dette blir det enklere å
jobbe med nye muligheter for spillutvikling og siden vi later som om variablene ikke kan
bli akksesert publicly betyr det også at variablene er mer sikret 👀👀👀

Oppgave:
lag en clicker (videospill) der brukeren kan gå i krig og skaffe seg penger.
brukeren kan bruke disse pengene på helter som fører til at intekten hans øker per krig.
lag også en mulighet for brukeren å see alle heltene han har kjøpt.
når brukeren kjøper en ny helt skal prisen til den neste helten av samme type øke.
ha ulike type helter som gir ulike mengder penger per krig.
gi brukeren muligheten til å kunne lagre data på en fil,
programmet skal kunnne lese daten for å kunne laste opp brukerens progresjon fra forrige session

NY OPPGAVE: bruk klasser til å sette verdier på helter, med en innkapsling metode (ikke public variabler)
plasser klassen i eget .py fil og hent klassen den via 'from x import y'
