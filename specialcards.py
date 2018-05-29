class SkipCard:
   def __init__(self,color):
      self.color = color
   def as_string(self):
      return self.color + "Skip"
    
class Draw2Card:
   def __init__(self,color):
      DrawCard.color = color
   def as_string(self):
      return self.color + "Draw 2"
      
class ReversCard:
   def __init__(self,coloe):
      self.color = coloe
   def as_string(self):
      return self.color + "Reverse"

      
      
