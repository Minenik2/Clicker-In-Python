class Hero():
    def __init__(self, name, lvl, cost, power, role):  # konstruktør
        self.name = name
        self.lvl = lvl
        self.cost = cost
        self.power = power
        self.role = role

    def changeName(self, name):  # endre variabel
        self.name = name

    def returnName(self):  # returnere variabel
        return self.name

    def changeLvl(self, lvl):
        self.lvl = lvl

    def returnLvl(self):
        return self.lvl

    def changeCost(self, cost):
        self.cost = cost

    def returnCost(self):
        return self.cost

    def changePower(self, power):
        self.power = power

    def returnPower(self):
        return self.power

    def changeRole(self, role):
        self.role = role

    def returnRole(self):
        return self.role

    def returnAll(self):  # returner alle variablene i en lesbar form
        return f"Name: {self.name}, Lvl: {self.lvl}, Cost: {self.cost}, Power: {self.power}"

    # returnerer alle variablene i en form som man kan enkelt bruke til lagring
    def returnAllForSave(self):
        return f"{self.name}, {self.lvl}, {self.cost}, {self.power}"
