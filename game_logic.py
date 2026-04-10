import random

class Card:
    def __init__(self, card_id, symbol):
        self.id = card_id
        self.symbol = symbol
        self.is_flipped = False
        self.is_matched = False

    def __str__(self):
        return self.symbol if (self.is_flipped or self.is_matched) else "❓"

class MemoryGame:
    def __init__(self, pairs_count=8):
        self.pairs_count = pairs_count
        self.cards = []
        self.first_pick = None
        self.second_pick = None
        self.moves = 0
        self.matches = 0
        self.setup_game()

    def setup_game(self):
        # Using fruit emojis for memory matching
        symbols = ['🍎', '🍌', '🍉', '🍇', '🍓', '🍒', '🍑', '🍍', '🥝', '🍅', '🥥', '🥭']
        selected_symbols = random.sample(symbols, self.pairs_count)
        
        # Create pairs and shuffle
        deck = selected_symbols * 2
        random.shuffle(deck)
        
        self.cards = [Card(i, symbol) for i, symbol in enumerate(deck)]
        self.first_pick = None
        self.second_pick = None
        self.moves = 0
        self.matches = 0

    def flip_card(self, index):
        card = self.cards[index]
        
        # Ignore if already flipped or matched
        if card.is_matched or card.is_flipped:
            return

        # If two cards are already picked from a previous turn, check and hide them now
        if self.first_pick is not None and self.second_pick is not None:
            self.check_match()

        # Flip the selected card
        card.is_flipped = True
        
        if self.first_pick is None:
            self.first_pick = index
        elif self.second_pick is None:
            self.second_pick = index
            self.moves += 1

    def check_match(self):
        if self.first_pick is not None and self.second_pick is not None:
            card1 = self.cards[self.first_pick]
            card2 = self.cards[self.second_pick]
            
            if card1.symbol == card2.symbol:
                card1.is_matched = True
                card2.is_matched = True
                self.matches += 1
            else:
                card1.is_flipped = False
                card2.is_flipped = False
                
            self.first_pick = None
            self.second_pick = None

    def is_game_over(self):
        return self.matches == self.pairs_count
