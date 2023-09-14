# Define the base class player
class Player:
  def play(self):
    printf("the player is playing cricket.")

# Define the derived Class Batsman
class Batsman(Player):
  def play(self):
    print("the batsman is bating.")

# Define the derived Class Bowler
class Bowler (Player):
  def play(self):
    print("the bowler is bowling.")

# create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play method for each 
object()
batsman.play()
bowler.play()
