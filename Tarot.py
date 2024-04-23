pips = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'Page', 'Queen', 'King']
suits = ['Pentacles', 'Swords', 'Wands', 'Cups']
arcana = ['0 - Fool', 'I - Magician', 'II - High Priestess', 'III - Empress', 'IV - Emperor', 'V - Hierophant', 'VI - Lovers', 'VII - Chariot', 'VIII - Strength', 'IX - Hermit', 'X - Wheel of Fortune', 'XI - Justice', 'XII - The Hanged Man', 'XIII - Death', 'XIV - Temperance', 'XV - Devil', 'XVI - The Tower', 'XVII - The Star', 'XVIII - The Moon', 'XIX - The Sun', 'XX - Judgement', 'XXI - The World']

class Minor_Tarot_Card():

    def __init__ (self, pips,suits):
        self.suits = suits
        self.pips = pips

    def __str__(self):
        return self.pips + " of " + self.suits
        
class Major_Tarot_Card:

    def __init__ (self, arcana):
        self.arcana = arcana

    def __str__(self):
        return self.arcana

class Tarot_Deck:

    def __init__(self):

        self.minor_arcana = []
        self.major_arcana = arcana

        for pip in pips:
            for suit in suits:
                minor_tarot_card = Minor_Tarot_Card(pip,suit)
                self.minor_arcana.append(minor_tarot_card)

        self.all_cards = self.minor_arcana + self.major_arcana
