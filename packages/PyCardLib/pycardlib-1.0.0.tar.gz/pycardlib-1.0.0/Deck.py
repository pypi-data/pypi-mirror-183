import random
from PyCardLib.Card import Card, STANDARD_SUITS, STANDARD_RANKS


STANDARD_DECK = [Card(suit, rank) for suit in STANDARD_SUITS for rank in STANDARD_RANKS]
EMPTY_DECK = []


class Deck:
    def __init__(self, cards=None, shuffle: bool = True, suits: list = None, ranks: list = None):
        """
        Creates a new deck
        :param cards:
        :param shuffle:
        :param suits:
        :param ranks:
        """
        self.cards = cards or EMPTY_DECK
        self._suits = suits or STANDARD_SUITS
        self._ranks = ranks or STANDARD_RANKS
        shuffle and self.shuffle()

    def __add__(self, other):
        if type(other) is Deck:
            return Deck(self.cards + other.cards)
        elif type(other) is Card:
            return Deck(self.cards + [other])
        else:
            raise TypeError("Cannot add Deck and %s" % type(other))

    def __sub__(self, other):
        if type(other) is Card:
            self.cards.remove(other)
            return other
        else:
            raise TypeError("Cannot remove %s from Deck" % type(other))

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return str(len(self)) + " card deck"

    def draw(self):
        """
        Draws a card from the deck
        :return: The card drawn
        """
        if len(self) == 0:
            raise ValueError("Cannot draw from empty deck")
        return self.cards.pop()

    def shuffle(self):
        """
        Shuffles the deck
        """
        random.shuffle(self.cards)

    def sort(self, suit_order=None, rank_order=None):
        """
        Sorts the deck
        :param suit_order: An optional list of suits to sort by
        :param rank_order: An optional list of ranks to sort by
        """
        suit_order = suit_order or STANDARD_SUITS
        rank_order = rank_order or STANDARD_RANKS
        self.cards.sort(key=lambda card: (suit_order.index(card.suit), rank_order.index(card.rank)))

    def deal(self, hands: int = 1, cards_per: int = 1):
        """
        Deals cards from the deck into a list of hands
        :param hands: The number of hands to deal into (default 1)
        :param cards_per: The number of cards to deal to each hand (default 1)
        :return: A list of hands, each containing cards_per number of cards
        """
        if hands * cards_per > len(self):
            raise ValueError("Not enough cards to deal. Tried to deal %d cards to %d hands, but only %d cards in deck"
                             % (cards_per, hands, len(self)))
        return [[self.draw() for _ in range(cards_per)] for _ in range(hands)]

    def deal_all(self, hands: int = 1, ensure_equal: bool = False):
        """
        Deals all cards from the deck into a list of hands
        :param hands: The number of hands to deal into (default 1)
        :param ensure_equal: If each hand should have the same number of cards (default False)
        :return: A list of hands, and if ensure_equal is True, a list of the cards left over (last in the list)
        """
        cards_per_hand = len(self) // hands
        cards_left_over = len(self) % hands
        hands = self.deal(hands, cards_per_hand)
        if ensure_equal:
            hands.append(self.deal(cards_per=cards_left_over))
        else:
            for _ in range(cards_left_over):
                hands[_].append(self.draw())
        return hands

    def reset(self):
        """
        Resets the deck, provided that the deck was created with a list of suits and ranks
        """
        if self._suits and self._ranks:
            self.cards = [Card(suit, rank) for suit in self._suits for rank in self._ranks]

    def remove(self, card):
        """
        Removes a card or cards from the deck
        :param card: The card or list of cards to remove
        """
        if type(card) is list:
            for c in card:
                self.remove(c)
        elif type(card) is Card:
            self.cards.remove(card)
        else:
            raise TypeError("Cannot remove %s from Deck" % type(card))

    add = __add__
    size = __len__
