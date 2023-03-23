class Player():
    def __init__(self, name, bidItem, bidPrice):
        self.name = name
        self.bidItem = bidItem
        self.bidPrice = bidPrice
        self.bidIndex = []

    def createBidIndex(self):
        self.bidIndex = list(zip(self.bidItem, self.bidPrice))

player1 = Player("Patrick", [0, 1], [6, 0])

