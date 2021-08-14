# from card import Card
from random import randint

class Deck:


    def __init__( self ):
        self.suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.values = list(range(1,14))
        self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        self.cards = []

        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        for i in range(0,len(self.cards)):
            x = randint(0,len(self.cards)-1)
            self.cards[i],self.cards[x] = self.cards[x],self.cards[i]
    
    def draw_card(self):
        if len(self.cards) != 0:
            return self.cards.pop()
        else: 
            return None

    def draw_card_at_index(self, index):
        if len(self.cards) != 0:
            return self.cards.pop(index)
        else: 
            return None



class Card:

    def __init__( self , suit , value):
        
        self.suit = suit
        self.value = value
        if value == 11:
            self.rank = 'Jack'
            self.value = 11
        elif value == 12:
            self.rank = 'Queen'
            self.value = 12
        elif value == 13:
            self.rank = 'King'
            self.value = 13
        elif value == 1:
            self.rank = 'Ace'
            self.value = 14
        else:
            self.rank = str(value)

    def __repr__(self):
        return(f'{self.rank} of {self.suit}, point value {self.value}')

    def __str__(self):
        return(f'{self.rank} of {self.suit}, point value {self.value}')
