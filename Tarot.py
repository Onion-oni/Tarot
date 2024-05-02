pips = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'Page', 'Queen', 'King']
suits = ['Pentacles', 'Swords', 'Wands', 'Cups']
arcana = ['0 - Fool', 'I - Magician', 'II - High Priestess', 'III - Empress', 'IV - Emperor', 'V - Hierophant', 'VI - Lovers', 'VII - Chariot', 'VIII - Strength', 'IX - Hermit', 'X - Wheel of Fortune', 'XI - Justice', 'XII - The Hanged Man', 'XIII - Death', 'XIV - Temperance', 'XV - Devil', 'XVI - The Tower', 'XVII - The Star', 'XVIII - The Moon', 'XIX - The Sun', 'XX - Judgement', 'XXI - The World']

class MinorTarotCard():

    def __init__ (self, pips,suits):
        self.suits = suits
        self.pips = pips

    def __str__(self):
        return self.pips + " of " + self.suits
        
class MajorTarotCard:

    def __init__ (self, arcana):
        self.arcana = arcana

    def __str__(self):
        return self.arcana

class TarotDeck:

    def __init__(self):

        self.minor_arcana = []
        self.major_arcana = arcana

        for pip in pips:
            for suit in suits:
                minor_tarot_card = MinorTarotCard(pip,suit)
                self.minor_arcana.append(minor_tarot_card)
        self.all_cards = self.minor_arcana + self.major_arcana
        
    def draw(self,x):
        #x is the number of cards for a spread
        counter = 0
        spread = []
        self.all_cards = self.minor_arcana + self.major_arcana
        while counter != x:
            #self.all_cards.random()
            spread.append(self.all_cards.pop())
            counter = counter + 1
        else:
            return spread
