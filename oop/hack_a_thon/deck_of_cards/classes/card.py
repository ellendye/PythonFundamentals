class Card:

    def __init__( self , suit , value):
        
        self.suit = suit
        self.value = value
        if value == 11:
            self.rank = 'Jack'
        if value == 12:
            self.rank = 'Queen'
        if value == 13:
            self.rank = 'King'
        if value == 1:
            self.rank = 'Ace'
        else:
            self.rank = str(value)

    def __repr__(self):
        return(f'{self.suit[0]} of {self.suit}')

    def __str__(self):
        return(f'{self.rank} of {self.suit}')
