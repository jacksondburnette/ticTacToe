'''
Two player ticTacToe


a) We need to print a board (list of 9 ' ' to be filled in with X's and O's)
b) Take in player input.
c) Place their input on the board.
d) Check if the game is won,tied, lost, or ongoing.
e) Repeat c and d until the game has been won or tied.
f) Ask if players want to play again.

currently only Unix systems are supported
'''
#to clear screen while in gameplay
from os import system

#player 1 symbol defaults to X
#player 2 symbol defaults of O
player1 = 'X'
player2 = 'O'

#init board
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#make dictionary to easily map player's move to the correct location in board list
boardEnum = {'a1':0,'b1':1,'c1':2,'a2':3,'b2':4,'c2':5,'a3':6,'b3':7,'c3':8}
#define valid moves
validMoveList = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

def drawBoard():
    '''
    visual representation of board based on type
    '''
    print '    a     b     c  '
    print '       |     |     '
    print '   {x}   | {y}   | {z}  '.format(x=board[0], y=board[1], z=board[2])
    print '1 _____|_____|_____'
    print '       |     |     '
    print '   {e}   | {f}   | {g}  '.format(e=board[3], f=board[4], g=board[5])
    print '2 _____|_____|_____'
    print '       |     |     '
    print '   {h}   | {i}   | {j}  '.format(h=board[6], i=board[7], j=board[8])
    print '3      |     |     '

def findMoveOnBoard(move):
    #ensure move is lowercase
    move = move.lower()
    #get index of move in board list
    index = boardEnum[move]

    return index

def validMove(move):
    #make sure player input is valid
    if move not in validMoveList:
        print 'What? Enter a valid move'
        print 'It should have one letter (A, B or C) and one number (1, 2 or 3).'
        return False
    #get index of move on board
    index = findMoveOnBoard(move)
    #move is valid if the index is empty (i.e. a space character)
    if board[index] == ' ':
        return True
    else:
        return False

def makeBoard(move, sym):
    '''
    INPUT: player's move (e.g. 'a3') and player's symbol (e.g. 'X')
    OUTPUT: board list with player's move
    '''
    index = findMoveOnBoard(move)
    board[index] = sym
    return board

def getMove(name):
    '''
    ask for player input
    '''
    #get players move
    move = raw_input(name + ', your move: ')
    
    return move

def checkStatus(board, sym):
    '''
    INPUT: current board and current player's symbol
    OUTPUT: 0 if no winner, 1 if current player won, 2 if tie game
    '''
    status = 0 #no winner
    #check for win vertically
    if (board[0]==board[3]==board[6]==sym) or (board[1]==board[4]==board[7]==sym) or (board[2]==board[5]==board[8]==sym):
        #winners symbol is any index on the 
        status = 'win'
    #check for win horizontally
    elif (board[0]==board[1]==board[2]==sym) or (board[3]==board[4]==board[5]==sym) or (board[6]==board[7]==board[8]==sym):
        status = 'win'
    #check for win diagonally
    elif (board[0]==board[4]==board[8]==sym) or (board[2]==board[4]==board[6]==sym):
        status = 'win'
    #if board full, tie game
    elif ' ' not in board:
        status = 'tie'

    if status == 'win':
        return 1 #player wins
    elif status == 'tie':
        return 2 #tie game
    else:
        return 0

########################################################main#############################################################################################

#clear screen
system('clear')

#get player's names
name1 = raw_input("Who wants to be X's? ")
name2 = raw_input("Who wants to be O's? ")

#tell players who they are
print name1 + ' = X'
print name2 + ' = O'
print ''

drawBoard()

#explain gameplay
print 'Use the grid system to make your move'
print 'For example, A3 would place your mark in the bottom left hand corner of the board'
print ''
ans = raw_input('GOT IT?!?!?!?! (y/n): ')
#if player doesn't get it, make snarky remark
if ans == 'n':
    print 'I think that you do.'

#start game
player = player1
name = name1
check = checkStatus(board, player)
while check == 0:
    move = getMove(name)
    if validMove(move):
        board = makeBoard(move, player)
        #clear screen to draw next board
        system('clear')
        #tell players who they are
        print name1 + ' = X'
        print name2 + ' = O'
        print ''
        drawBoard()
        check = checkStatus(board, player)
        
        #switch players if no one has won or tied
        if player == player1 and check == 0:
            player = player2
            name = name2
        elif check == 0:
            player = player1
            name = name1
    else:
        print 'That was not a valid move, try again.'

#when the game is done, print message
if check == 1:
    print name + ' wins!'
#if player hasn't won then it's a tie game
else:
    print "cat's game"
