"""
DAY 2
PART 1
"""
import sys
from functools import reduce
def map_to_rock_paper_scissors(hand):
  '''Returns rock, paper, or scissors parsed from character code'''
  x = {
      "A": "rock",
      "B": "paper",
      "C": "scissors",
      "X": "rock",
      "Y": "paper",
      "Z": "scissors",
  }
  return x[hand]
def eval_rock_paper_scissors(player1, player2):
  '''Returns whether player2 has won, lost or drawn'''
  player1 = map_to_rock_paper_scissors(player1)
  player2 = map_to_rock_paper_scissors(player2)
  if player1 == player2:
      return "draw"
  win = {
      "scissors rock": "win",
      "paper scissors": "win",
      "rock paper": "win"
  }
  key = player1 + " " + player2
  if key in win:
      return "win"
  return "lose"
def score_hand(player):
    player = map_to_rock_paper_scissors(player)
    x = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    return x[player]
def score_result(result):
    x = {
        "win": 6,
        "draw": 3,
        "lose": 0
    }
    return x[result]
filename = sys.argv[1]
with open(filename, 'r') as file:
    line = file.readline()
    total_score = 0
    while line:
        print(line)
        # Remove newline char.
        if line[len(line) -1] == '\n':
            line = line[:-1]
        player1, player2 = line.split(" ")
        score = score_result(eval_rock_paper_scissors(player1, player2)) + score_hand(player2)
        total_score += score
        print(score)
        line = file.readline()
    print("End of input")
    print("Total score = %s" % total_score)
