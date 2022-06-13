#Rock, Paper, Scissors Python Game
import random
import os

def playGame():
    user = input("what's your choice?('R' for Rock, 'S' for Scissor, 'P' for Paper)")
    computer = random.choice(['P', 'R', 'S'])

    if user == computer:
      print("Your choice: ' + user +' Computer choice: ' + computer +' Its a tie!")

    if win(user,computer):
      print("Your choice: ' + user +' Computer choice: ' + computer +' You won!")
    if lose(user,computer):
      print("Your choice: ' + user +' Computer choice: ' + computer +' You lose!")

def win(player, opponent):
    if player == 'S' and opponent == 'P' or player == 'P' and opponent == 'R' \
      or player == 'R' and opponent == 'S':
        return True

def lose(player, opponent):
    if player == 'P' and opponent == 'S' or player == 'R' and opponent == 'P' \
      or player == 'S' and opponent == 'R':
        return True
replay = "n"

def repeat():
    choice = 1
    while choice > 0:
      replay = input("would you like to play again? ('y' for yes, 'n' for no.)")
      if replay == "y":
          choice = choice + 1
          print("enjoy!")
          playGame()
      elif replay == "n":
          choice = 0
          print("Thank you for playing.")
          os._exit
      else:
          print("please enter 'y' or 'n'")
          choice = 0
          repeat()

playGame()
repeat()