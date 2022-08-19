# --- Some variables ---
import random

newGameAnswers = ["y", "yes", "Yes", "YES",  "Y"]
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player = "X"
winner = None
gameRunning = True

# --- Print the game board ---
def printGameBoard(board):
  print("\n" + board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# --- Take player input ---
def playerInput(board):
  inp = int(input("\nPlease, enter a number between 1 and 9: "))
  if inp >= 1 and inp <= 9 and board[inp-1] == "-":
    board[inp-1] = player
  elif inp < 1 or inp > 9:
    print("\nIt looks like you entered a wrong number...")
    playerInput(board)
  else:
    print("\nOps...player is already in that spot!")
    playerInput(board)

# --- Check for win or tie ---
def checkHorizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[0] != "-":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True

def checkVertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True

def checkDiagonal(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True

def checkTie(board):
  global gameRunning
  if "-" not in board:
    print("\nTie!")
    printGameBoard(board)
    gameRunning = False
    return True
  return False

def checkWinner():
  global gameRunning
  if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
    print(f"\nThe winner is {winner}")
    printGameBoard(board)
    gameRunning = False
    return True
  return False

# --- Switch the player ---
def switchPlayer():
  global player
  if player == "X":
    player = "O"
  else:
    player = "X"

# --- Computer ---
def computer(board):
  while player == "O" and "-" in board:
    pos = random.randint(0,8)
    if board[pos] == "-":
      board[pos] = "O"
      switchPlayer()

# --- Clear the board for a new game ---
def resetBoard(board):
  global gameRunning
  for i in range(len(board)):
    board[i] = "-"
  gameRunning = True

# --- Game Running ---
while gameRunning:
  printGameBoard(board)

  playerInput(board)
  if checkWinner():
    newgame = input("\nNew Game? [Y]es/[N]o: ")
    if newgame in newGameAnswers:
      resetBoard(board)
    else:
      print("\nSee you soon!")
      break
  if checkTie(board):
    newgame = input("\nNew Game? [Y]es/[N]o: ")
    if newgame in newGameAnswers:
      resetBoard(board)
    else:
      print("\nSee you soon!")
      break

  switchPlayer()
  
  computer(board)
  if checkWinner():
    newgame = input("\nNew Game? [Y]es/[N]o: ")
    if newgame in newGameAnswers:
      resetBoard(board)
    else:
      print("\nSee you soon!")
      break
  if checkTie(board):
    newgame = input("\nNew Game? [Y]es/[N]o: ")
    if newgame in newGameAnswers:
      resetBoard(board)
    else:
      print("\nSee you soon!")
      break
