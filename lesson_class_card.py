class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknown'

    def __init__(self, number, validDate, holder):
        self.number = number
        self.validDate = validDate
        self.holder = holder

    def pay(self, amount):
        print('С карты', self.number, 'списали', amount)
