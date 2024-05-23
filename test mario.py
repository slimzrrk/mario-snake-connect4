import pygame
import sys

# define the size of the board
ROWS = 6
COLS = 7

# define the size of the circles and gaps between them
CIRCLE_SIZE = 80
GAP_SIZE = 10

# define the size of the window
WIDTH = COLS * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE
HEIGHT = (ROWS + 1) * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE

# define the colors
BACKGROUND_COLOR = (0, 0, 255)
CIRCLE_COLOR = (255, 255, 255)
PLAYER_1_COLOR = (255, 0, 0)
PLAYER_2_COLOR = (255, 255, 0)
BLACK = (0, 0, 0)

# initialize pygame
pygame.init()

# create the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# set the title of the window
pygame.display.set_caption("Connect 4")

# load the winning music
pygame.mixer.music.load("SUPER_MARIO_WIN.mp3")

# define a function to draw the board
def draw_board(board):
    # clear the screen
    SCREEN.fill(BACKGROUND_COLOR)

    # draw the circles
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.circle(SCREEN, CIRCLE_COLOR, (col * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2, (row + 1) * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2), CIRCLE_SIZE // 2)

    # draw the pieces
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 1:
                pygame.draw.circle(SCREEN, PLAYER_1_COLOR, (col * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2, (row + 1) * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2), CIRCLE_SIZE // 2 - 5)
            elif board[row][col] == 2:
                pygame.draw.circle(SCREEN, PLAYER_2_COLOR, (col * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2, (row + 1) * (CIRCLE_SIZE + GAP_SIZE) + GAP_SIZE + CIRCLE_SIZE // 2), CIRCLE_SIZE // 2 - 5)

    # update the screen
    pygame.display.update()

# define a function to drop a piece into the board
def drop_piece(board, row, col, player):
    board[row][col] = player

# define a function to check if a move is valid
def is_valid_move(board, col):
    return board[0][col] == 0

# define a function to get the next open row in a column
def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            return row
    return None

# define a function to check if a player has won
def is_winner(board, player):
    piece = player
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
    # check diagonal (up-right)
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
    return False

# define the main function
def main():
    # initialize the board
    board = [[0 for col in range(COLS)] for row in range(ROWS)]

    # set the current player to 1
    current_player = 1

    # set the game over flag to False
    game_over = False

    # draw the initial board
    draw_board(board)

    # run the game loop
    while not game_over:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if the user clicks the close button, exit the game
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()
                else: 
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()
                # if the user clicks the mouse, drop a piece into the board
                if current_player == 1:
                    col = event.pos[0] // (CIRCLE_SIZE + GAP_SIZE)
                    if is_valid_move(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        if is_winner(board, 1):
                            game_over = True
                            pygame.mixer.music.play()
                else:
                    col = event.pos[0] // (CIRCLE_SIZE + GAP_SIZE)
                    if is_valid_move(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        if is_winner(board, 2):
                            game_over = True
                            pygame.mixer.music.play()

                # switch players
                current_player = 3 - current_player

                # draw the updated board
                draw_board(board)

    # wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# run the main function
if __name__ == '__main__':
    main()

