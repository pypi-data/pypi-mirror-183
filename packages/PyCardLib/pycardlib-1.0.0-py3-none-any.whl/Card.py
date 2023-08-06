STANDARD_SUITS = [
    "Spades",
    "Hearts",
    "Diamonds",
    "Clubs"
]

STANDARD_RANKS = [
    "Ace",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King"
]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def __int__(self):
        if self.rank in STANDARD_RANKS:
            return STANDARD_RANKS.index(self.rank) + 1

    get_value = __int__
