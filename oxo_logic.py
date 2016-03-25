'''This is the main logic for a tic-tac-toe game.
It is not optimised for a quality game it simply
gnereates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMOve()
'''

import os, random
import oxo_data

def newGame():
	return list(" " * 9)

def saveGame(game):
	oxo_data.saveGame(game)

def restoreGame():
	try:
		game = oxo_data.restoreGame() #if previous game exists, return new game
		if len(game) == 9:
			return game
		else: return newGame()
	except IOerror: #what is an IO error?
		return newGame()

def _generateMove(game): # this populates a list of spaces where there are no x or o's, and chooses one randomly
	options = [i for i in range(len(game)) if game[i] == " "] 
	#this is called a 'list comprehension'
	#this is the same as saying:
	#
	#options = []
	#for i in range(len(game)):
	#	if game[i] = " ":
	#		options.append(i)
	#[append index for each index in the range if condition is true]

	return random.choice(options)

def _isWinningMove(game): #this will return if the move wins for somebody.
	wins = ((0,1,2), (3,4,5), (6,7,8),
			(0,3,6), (1,4,7), (2,5,8),
			(0,4,8), (2,4,6))

	for a,b,c in wins:
		chars = game[a] + game[b] + game[c]
		if chars == 'XXX' or chars == 'OOO':
			return True
	return False

def userMove(game, cell): #this mus be receiving the game and cell from the user interface 
	if game[cell] != ' ':
		raise ValueError('Invalid cell') #raise is a new one, but I think it is like throw in js
	else:
		game[cell] = 'X'
	if _isWinningMove(game):
		return 'X' #if this gets returned, it means X won the game?
	else:
		return ''

def computerMove(game):
	cell = _generateMove(game)
	if cell == -1:
		return 'D'
	game[cell]= 'O'
	if _isWinningMove(game):
		return 'O'
	else:
		return ''

def test():
	result = ''
	game = newGame()
	while not result: #is empty string falsey?
		print(game)
		try:
			result = userMove(game, _generateMove(game))
		except ValueError:
			print("Oops, that shouldn't happen")
		if not result:
			result = computerMove(game)

		if not result: continue
		elif result == 'D':
			print("It's a draw")
		else:
			print("Winner is: ", result)
		print(game)

if __name__ == '__main__': 
	test()
