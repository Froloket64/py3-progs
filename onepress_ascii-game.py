###  -- A simple ASCII game involving pressing one button --  ###

## TODO
# 1. FIXME Fix the button-hold bug, when the bar end is getting pushed
# 2. FIXME Fix the weird execution continuation bug thing [HARDLY REPRODUCABLE]

## IMPORTS
from blessings import Terminal  ## Controlling the cursor
from pynput import keyboard  ## Listening to keyboard events
from string import ascii_lowercase as letters  ## <useful>
from os import system  ## Clearing the console
from time import sleep  ## Well, sleeping (waiting)


## DEFININIONS
term = Terminal()

chars = 'bfd'

board = {}
for char in chars:
	board.update({char: 0})


bar_size = 50  ## Size of progress bars


## Stuff to do on keypress
def on_press(key):
	global running  ##  Access vars from
	global board    ##  global namespace

	if 'char' in dir(key):  ## If a key has the `char` attribute (only the printable ones do)
		if key.char in chars:
			board.update({key.char: board[key.char] + 1})

		if key.char in letters:  ## The worst way to hide keypresses (not print the characters)
			print('\b ' + term.move_up())  ## <Print the backspace esc.-seq. and move the cursor up> (PS: just adding `end=""` didn't work for some reason)

	if key == keyboard.Key.esc:  ## Esc:
		running = False  ## Finish the app


listener = keyboard.Listener(
	on_press=on_press,
	on_release=None
)


## GAME
listener.start()

won = ''

running = True
while running:
	# system('clear')
	print( term.clear() + '' )  ## Use that instead if ur allergic to `os.system`

	print('Press YOUR button to progress YOUR bar\n')


	progress = []
	for letter in board.keys():
		amount = board[letter]
		progress.append(f'{letter} [{"=" * amount}{"-" * (bar_size - amount)}]')

	for line in progress:
		print(line)
		if line.count('=') >= bar_size:
			won = line[0]

	if won:
		print( term.move(2 + chars.index(won) + 1, 3 + bar_size + 3), "| WON!" )
		break
	
	sleep(0.05)  ## In my terminal, if I dont' put this line, the text constently flashes which is not what I would like

print(term.move(2 + len(chars), 0))

listener.stop()