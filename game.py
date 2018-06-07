class Game:
  cards = ["green", "yellow","blue", "red"]
  def __init__(self):
    cards = ["green", "yellow","blue", "red"]
    self.state = cards
    self.game_over = False 
  def __repr__(self):
    return "Game({})".format(self.state)
  def make_deck(self, cards):
    deck = []
    for i in range(10):
      for color in ['blue', 'green', 'yellow', 'red']:
        if i == 0:
          card = StandardCard
          deck.append(card)
        else:
          card = SkipCard
          deck.append(card)
          card = Draw2
          deck.append(card)
    for i in range(4):
      card = WildCard()
      deck.append(card)
    for i in range(4):
      card = WildCard()
      card.draw_4 = True
      deck.append(card)
    return deck
   def shuffle_deck(self):
      return deck.shuffle()
   def deal(self, players):
        self.hands = [self.deck[i::players] for i in range(0, players)]
      
          
