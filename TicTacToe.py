#from IPython.display import clear_output
import os


def display_board(board):
    #clear_output()
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    pass

def player_input():

    marker = ''

    #keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        marker = marker.upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)
    
    pass

def place_marker(board, marker, position):
    #test_board = ['#','X','O','X','O','X','O','X','O','X']

    board[position] = marker
    
    pass

def win_check(board, mark):

    win_condition_list = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3],[1,4,7],[2,5,8],[3,6,9]]

    for winrow in win_condition_list:

        win_match = 0

        for space in winrow:
            if board[space] == mark:
                win_match += 1
            else:
                break

        if win_match == 3:
            return True
            
    pass

import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
        
    pass

def space_check(board, position):

    return board[position] == ' '
    
    pass

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if we return true
    return True
    
    pass

def player_choice(board):

    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a space 1-9: "))

    return position

def replay():
    playagain = ''
    while (playagain.upper() != 'Y' and playagain.upper() != 'N'):
        playagain = input("Do you want to play again, Y or N?")
        
    return playagain.upper() == 'Y'
    
    pass

#while loop to keep running the game
print('Welcome to Tic Tac Toe!')

while True:

    #play game

    ## board
    the_board = (['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])
    player1_marker, player2_marker = player_input()
    print('Player 1 is ' + player1_marker)
    print('Player 2 is ' + player2_marker)

    ##who's first    ##choose markers X or O
    turn = choose_first()
    print(turn + ' will go first. ')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ##gameplay
    while game_on:

        if turn == 'Player 1':

            ###player one turn

            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker
            place_marker(the_board, player1_marker,position)

            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
            # check for tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
            #no tie no win? next player's turn
                    turn = 'Player 2'
        
        else:
            
            ###player one turn

            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place the marker
            place_marker(the_board, player2_marker,position)

            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
            # check for tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
            #no tie no win? next player's turn
                    turn = 'Player 1'

    if not replay():
        break
    #break out of the while loop on replay()
