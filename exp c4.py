import numpy as np
import pygame
import sys
import os

# define the board dimensions
ROWS = 6
COLS = 7

# define the circle size and gap size
CIRCLE_SIZE = 80
GAP_SIZE = 10

# define the board size
SQUARESIZE = (CIRCLE_SIZE+GAP_SIZE)
RADIUS = int(CIRCLE_SIZE/2)

# define the colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# initialize pygame
pygame.init()

# set the screen dimensions
width = COLS * SQUARESIZE
height = (ROWS+1) * SQUARESIZE
size = (width, height)

# set the screen
screen = pygame.display.set_mode(size)

# define the draw_board function
def draw_board(board):
    for col in range(COLS):
        for row in range(ROWS):
            pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, (row+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[row][col] == 0:
                pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE+SQUARESIZE/2), int((row+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col*SQUARESIZE+SQUARESIZE/2), int((row+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col*SQUARESIZE+SQUARESIZE/2), int((row+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

# define the is_valid_move function
def is_valid_move(board, col):
    return board[ROWS-1][col] == 0

# define the get_next_open_row function
def get_next_open_row(board, col):
    for row in range(ROWS):
        if board[row][col] == 0:
            return row

# define the drop_piece function
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# define the is_winner function
def is_winner(board, piece):
    # check horizontal
    for row in range(ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # check vertical
    for row in range(ROWS-3):
        for col in range(COLS):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    # check diagonal (down-right)
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    # check diagonal (down-left)
    for row in range(ROWS-3):
        for col in range(3, COLS):
            if board[row][col]== piece and board[row+1][col-1] == piece and board[row+2][col-2] == piece and board[row+3][col-3] == piece:
                return True
    return False


# create the board
board = np.zeros((ROWS, COLS), dtype=int)

# set the game_over flag to False
game_over = False

# set the turn flag to 0 (player 1)
turn = 0

# draw the board
draw_board(board)

# start the game loop
while not game_over:
    # get the events
    for event in pygame.event.get():
        # if the user quits the game, exit
        if event.type == pygame.QUIT:
            sys.exit()

        # if the user clicks the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if it is player 1's turn
            if turn == 0:
                # get the column of the mouse click
                posx = event.pos[0]
                col = int(posx/SQUARESIZE)

                # check if the move is valid
                if is_valid_move(board, col):
                    # get the row to drop the piece
                    row = get_next_open_row(board, col)

                    # drop the piece
                    drop_piece(board, row, col, 1)

                    # check if the player wins
                    if is_winner(board, 1):
                        print("Player 1 wins!")
                        game_over = True

            # if it is player 2's turn
            else:
                # get the column of the mouse click
                posx = event.pos[0]
                col = int(posx/SQUARESIZE)

                # check if the move is valid
                if is_valid_move(board, col):
                    # get the row to drop the piece
                    row = get_next_open_row(board, col)

                    # drop the piece
                    drop_piece(board, row, col, 2)

                    # check if the player wins
                    if is_winner(board, 2):
                        print("Player 2 wins!")
                        game_over = True

            # alternate the turn
            turn = (turn + 1) % 2

            # redraw the board
            draw_board(board)

