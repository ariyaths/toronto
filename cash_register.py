class CashRegister:

    def __init__(self, loonies, toonies, fives, tens, twenties):
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def getTotal(self):
        return self.loonies + 2*self.toonies + 5*self.fives + 10*self.tens + \
               20*self.twenties

    def add(self, amount, denomination):
        print(eval("self." + denomination), str(denomination))
        exec("self." + denomination+" += " + str(amount))
        print(eval("self." + denomination), str(denomination))

    def remove(self, amount, denomination):
        print(eval("self." + denomination), str(denomination))
        exec("self." + denomination+" -= " + str(amount))
        print(eval("self." + denomination), str(denomination))

    def switch(self, argument):
        switcher = {
            "loonies": 1,
            "toonies": 2,
            "fives": 5,
            "tens": 10,
            "twenties": 20
        }
        return switcher.get(argument, "Invalid Denomination")


if __name__ == "__main__":
    # A cash register with 5 loonies, 5 toonies, 5 fives, 5 tens, and 5 twenties
    # for a total of $190.
    register = CashRegister(5, 5, 5, 5, 5)
    print(register.getTotal())
    register.add(3, 'toonies')
    register.remove(2, 'twenties')

    print(register.getTotal())
    print(register.switch("toonies"))
