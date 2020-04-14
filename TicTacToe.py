# Importing Modules
import random
import os
from os import system
import time

# Takes a list, prints filled board
def drawBoard(board):
	system('clear')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')


#Asks user input for x and o
def pickingMarker():
	a = ''
	while a != 'x' and a != 'o':
		a = input("Do you want X or O: ").lower()
	if a == 'x':
		return['X', 'O']
	else:
		return['O', 'X']

#Determining first turn 
def first_turn():
	#if random.randint(0,1) == 1:
	return 'player'
	#else:
	#	return 'computer'

def make_move(board, letter, move):
	board[move] = letter

def open_spaces(board, move):
	return board[move] == ' '

def check_for_win(b, l):
	return  (b[7] == l and b[8] == l and b[9] == l or
	b[4] == l and b[5] == l and b[6] == l or
	b[1] == l and b[2] == l and b[3] == l or
	b[7] == l and b[5] == l and b[3] == l or
	b[9] == l and b[5] == l and b[1] == l or
	b[7] == l and b[4] == l and b[1] == l or
	b[8] == l and b[5] == l and b[2] == l or
	b[9] == l and b[6] == l and b[3] == l)

def ask_to_play_again():
	b = ''
	while b != 'y' and b != 'n':
		b = input('Do you want to play again, Y or N: ')

	if b == 'y':
		return True
	else:
		return False

def check_board_full(board):
	for i in range(1,10):
		if open_spaces(board, i):
			return 'False'
			break
	return 'True'

def get_player_move(board):
	a = ''
	while a == '':
		move = int(input("Num of position(1-9): "))
		if open_spaces(gameBoard, move):
			return move
		else:
			print("There is already a marker in their location, Try Again")


def chooseRandomMoveFromList(board, movesList):
	possible_moves = []
	for i in movesList:
		if open_spaces(board, i):
			possible_moves.append(i)

	if len(possible_moves) != 0:
		return possible_moves
	else:
		return None

def get_computer_move(board, computer_letter):
	if computer_letter == 'X':
		player_letter = 'O'
	else:
		computer_letter = 'O'

	move = chooseRandomMoveFromList(board, [1,2,3,4,5,6,7,8,9])
	move = random.choice(move)
	#move = random.choice(move)
	if move != None:
		return move
	

while True:
	gameBoard = [' '] * 10
	system('clear')

	print('This is the numbering system')
	print('   |   |')
	print(' ' + '7' + ' | ' + '8' + ' | ' + '9' )
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + '1' + ' | ' + '2' + ' | ' + '3' )
	print('   |   |')
	time.sleep(1)

	player_letter, computer_letter = pickingMarker()
	turn = first_turn() 
	game_is_playing = True
	while game_is_playing == True:

		if turn == 'player':
			drawBoard(gameBoard)
			move = get_player_move(gameBoard)
			make_move(gameBoard, player_letter, move)
			drawBoard(gameBoard)

		if check_for_win(gameBoard, player_letter):
			drawBoard(gameBoard)
			print("You have won!!!")
			system('say Congratulations')
			game_is_playing = False
		else:
			#if check_board_full(gameBoard)3
			#	print("The game is a tie")
			#	break
			turn = 'computer'

		if turn == 'computer':
			time.sleep(1)
			move = get_computer_move(gameBoard, computer_letter)
			make_move(gameBoard, computer_letter, move)

			if check_for_win(gameBoard, computer_letter):
				print("Sorry, the computer has won")
				game_is_playing = False
			else:
				 #if check_board_full(gameBoard):
				 #	drawBoard(gameBoard)
				 #	print("The game is a tie")
				 #	break
				 turn = 'player'
	
	if not ask_to_play_again():
		break






 




