'''oso_data is the data module for a tic-tac-toe (or OXO) game.
It saves and restores a game board. The functions are:
	saveGame(game) -> None
	restoreGame ->
Note that no limits are placed on the size of the data.
The game implmentation is responsible for validating all data
in and out.'''

import os.path #same as from os import path?
game_file = ".oxogame.dat"

def _getPath(): #why the underscore in front?
	'''Returns a valid path for data file.
	Tries to use the users home folder, defaults to cwd''' #cwd = current working directory?

	try:
		game_path = os.environ['HOMEPATH'] or os.environ['HOME'] #homepath just for windows?
		if not os.path.exists(game_path): #if path doesn't exist, use cwd
			game_path = os.getcwd()
	except (KeyError, TypeError): #why is this a tuple? how is this evaluated?
		game_path = os.getcwd()
	return game_path

def saveGame(game):
	''' saveGame(game) -> None
	saves a game obj in the data file in the users home folder.
	No checking is done on the imput, which is expected to be a
	list of characters'''

	path = os.path.join(_getPath(), game_file) #lookup os.path.join, looks like it just concatenates the filename to the end of the path
	with open(path, 'w') as gf: #'with...as' is a new syntax structure for me. why not gf = open(path, 'w')?
		gamestr = ''.join(game)
		gf.write(gamestr)

def restoreGame():
	''' restoreGame() -> game
	Restores a game from the data file.
	The game object is a list of characters'''

	path = os.path.join(_getPath(), game_file)
	with open(path, 'w') as gf:
		gamestr = gf.read()
		return list(gamestr)

def test():
	print('Path =', _getPath())
	saveGame(list("XO  XO OX"))
	print(restoreGame())

if __name__ == '__main__': test() 

#from Stack Overflow:
#When the Python interpreter reads a source file, it executes all of the code found in it. Before executing the #code, it will define a few special variables. For example, if the python interpreter is running that module (the #source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is #being imported from another module, __name__ will be set to the module's name.

#so why am i running automatic tests like this? do i comment out this line later?


