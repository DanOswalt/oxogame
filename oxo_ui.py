'''CLI User Interface for Tic-Tac-Toe game
Use as the mian program, no reusable function'''

import os
import oxo_logic #doesn't interact with data file
import argparse as ap
import tkinter
import tkinter.messagebox as mb

menu = ["Start new game",
		"Resume saved game",
		"Display help",
		"Quit"]

def getMenuChoice(aMenu):
	'''getMenuChoice(aMenu) -> int

	takes a list of strings as input, 
	displays as a numbered menu and
	loops until user selects a valid number'''

	if not aMenu: raise ValueError('No menu content')
	while True:
		print('\n\n')
		for index, item in enumerate(aMenu, start=1):
			print(index, "\t", item)

		try:
			choice = int(input('\nChoose a menu option: '))
			if 1 <= choice <= len(aMenu):
				return choice
			else: print('Choose a number between 1 and', len(aMenu))
		except ValueError:
			print("Choose the number of a menu option")

def main():
    top = tkinter.Tk()
    top.withdraw()
    while True:
        choice = getMenuChoice(menu)
        executeChoice(choice)

def startGame():
	return oxo_logic.newGame()

def resumeGame():
	return oxo_logic.restoreGame()

def displayHelp():
	print('''
	Start new game: starts a new game of Tic-Tac-Toe
	Resume saved game: restores the last saved game and commences play
	Display help: show this page
	Quit: quits the application''')

def quit():
	print('Goodbye...')
	raise SystemExit #any different that sys.exit()?

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def executeChoice(choice):
	'''executeChoice(int) -> None

	Execute whichever option the user selected.
	If the choice produeces a valid game then
	play the game until it completes'''

	dispatch = [startGame, resumeGame, displayHelp, quit]
	game = dispatch[choice - 1]() #can put function names in an array, nice!
	if game:
		playGame(game)

def printGame(game):
    clear()
    display = '''
     1 | 2 | 3     {} | {} | {}
    -----------   --------------
     4 | 5 | 6     {} | {} | {}
    -----------   --------------
     7 | 8 | 9     {} | {} | {}'''

    print(display.format(*game))

def playGame(game):
    result = ''
    while not result:
        printGame(game)
        choice = input('Cell[1-9 or q to quit]: ')
        if choice.lower()[0] == 'q':
            save = mb.askyesno("Save game", "Save game before quitting?")
            if save:
                oxo_logic.saveGame(game)
            quit()
        else:
            try:
            	cell = int(choice) - 1
            	if not (0 <= cell <= 8):
            		raise ValueError
            except ValueError:
                print('Choose a number between 1 and 9 or q to quit')
                continue

            try:
                result = oxo_logic.userMove(game, cell)
            except ValueError:
                mb.showerror("Invalid cell", "Choose an empty cell")
                continue
            if not result:
                result = oxo_logic.computerMove(game)
            if not result:
                continue
            elif result == 'D':
                printGame(game)
                mb.showinfo("Result", "It's a draw")
                print("It's a draw")
            else:
                printGame(game)
                mb.showinfo("Result", "Winner is {}".format(result))

if __name__ == '__main__': main()

