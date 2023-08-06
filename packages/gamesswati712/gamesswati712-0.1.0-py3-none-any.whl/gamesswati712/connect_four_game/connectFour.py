import numpy as np
import pygame
import sys
import math
import time

ROW_COUNT = 6
COLUMN_COUNT = 7
CONNECT = 4
BLUE = (3, 144, 252)
BLACK = (0,0,0)
RED = (232, 12, 12)
YELLOW = (252, 161, 3)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

#piece = 1 for player 1 and 2 for player 2
def drop_piece(board, row,col, piece):
    board[row][col] = piece

#to check if the column is still free
# numbering of rows is as follows

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

#to check which row the next piece will fall in
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#flip the board - to start from bottom up
def print_board(board):
    #0 is the x axis
    print(np.flip(board, 0))

#to check if we have won
def winning_move(board, piece):
    #check all horizontal locations
    for c in range(COLUMN_COUNT - (CONNECT-1)):
        for r in range(ROW_COUNT): 
            count = 0
            for x in range(CONNECT):
                if board[r][c + x] == piece:
                    count += 1
            if count == CONNECT:
                return True

    #check all vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - (CONNECT-1)): 
            count = 0
            for x in range(CONNECT):
                if board[r+x][c] == piece:
                    count += 1
            if count == CONNECT:
                return True

    #check for positive slope diagonals
    for c in range(COLUMN_COUNT - (CONNECT - 1)):
        for r in range(ROW_COUNT - (CONNECT), ROW_COUNT): 
            count = 0
            for x in range(CONNECT):
                if board[r-x][c+x] == piece:
                    count += 1
            if count == CONNECT:
                return True

    #check for the negative slope diagonals
    for c in range(COLUMN_COUNT - (CONNECT-1)):
        for r in range(ROW_COUNT - (CONNECT - 1)): 
            count = 0
            for x in range(CONNECT):
                if board[r+x][c+x] == piece:
                    count += 1
            if count == CONNECT:
                return True

#drawing the board with pygame graphics
def draw_board(board):
    #draw squares(rectangles here) and then draw circles on top of them
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARESIZE + SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), RADIUS)
            
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARESIZE + SQUARESIZE/2, height - (r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE + SQUARESIZE/2, height - (r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0



#initialising pygame
pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1)* SQUARESIZE 
size = (width, height)

#we have subtracted any arbitrary int value
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

FONTSIZE = 75
myfont = pygame.font.SysFont("monospace",FONTSIZE)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE) )
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, SQUARESIZE/2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, SQUARESIZE/2), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            #Ask for player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = math.floor(posx /SQUARESIZE)
                if is_valid_location(board, col):
                    row = get_next_open_row(board,col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        # print("Player 1 Wins !")
                        pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE) )
                        label = myfont.render("Player 1 won !!", 1,RED)
                        screen.blit(label,(30,10))
                        game_over = True

            # #Ask for player 2 Input
            else:
                posx = event.pos[0]
                col = math.floor(posx /SQUARESIZE)
                if is_valid_location(board, col):
                    row = get_next_open_row(board,col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        # print("Player 2 Wins !")
                        pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE) )
                        label = myfont.render("Player 2 won!!", 1,YELLOW)
                        screen.blit(label,(30,10))
                        game_over = True



            print_board(board)
            draw_board(board)
            #alternate between zero and one 
            turn += 1
            turn = turn % 2
        if game_over:
            pygame.time.wait(5000)
     

















#what to do if user enters a number greater than 6 or less than0 or anything invalid
#screen blit vs screen.display.update
#title