# from car_game import carGame
# from snake_game import snake
# from Flappy_bird_game import game
# from connect_four_game import connectFour

import button
import pygame
import sys

pygame.init()

# create game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Playzone")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("arialblack", 60)
font2 = pygame.font.SysFont("arialblack", 30)
font2_col = 232, 184, 53


# define colours
TEXT_COL = (255, 255, 255)

# load button images
flappy_img = pygame.image.load("flappy.png").convert_alpha()
connect_img = pygame.image.load("connect.png").convert_alpha()
snake_img = pygame.image.load('snake.png').convert_alpha()
car_img = pygame.image.load('car.png').convert_alpha()
quit_img = pygame.image.load("quit.png").convert_alpha()
# keys_img = pygame.image.load('images\\button_keys.png').convert_alpha()
# back_img = pygame.image.load('images\\button_back.png').convert_alpha()

# create button instances
flappy_button = button.Button(420, 125, flappy_img, 1)
connect_button = button.Button(420, 250, connect_img, 1)
snake_button = button.Button(420, 375, snake_img, 1)
car_button = button.Button(420, 500, car_img, 1)
quit_button = button.Button(420, 625, quit_img, 1)
# keys_button = button.Button(246, 325, keys_img, 1)
# back_button = button.Button(332, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:

    screen.fill((0, 51, 51))

    # check if game is paused
    if game_paused == True:
        # check menu state
        if menu_state == "main":
            # draw pause screen buttons
            if flappy_button.draw(screen):
                print("noww")

                # from ast import main
                import random
                from string import digits
                import sys
                import pygame
                from pygame.locals import *
                import time

                # Global variables
                PAUSE = False
                FPS = 32
                SCREENWIDTH = 1400
                SCREENHEIGHT = 800
                SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
                GROUNDY = SCREENHEIGHT * 0.8
                GAME_SPRITES = {}
                GAME_SOUNDS = {}
                PLAYER = 'player_bird.png'
                BACKGROUND = 'Background-1.png'
                PIPE = 'pipe.jpg'

                def welcomeScreen():
                    playerx = int(SCREENWIDTH / 5)
                    playery = int(
                        (SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
                    messagex = int(
                        (SCREENWIDTH - GAME_SPRITES['player'].get_width()) / 2)
                    messagey = int(SCREENHEIGHT * 0.13)
                    basex = 0

                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                                return

                            else:
                                SCREEN.blit(
                                    GAME_SPRITES['message'], (-70, -10))
                                SCREEN.blit(
                                    GAME_SPRITES['player'], (playerx, playery))
                                # SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                                SCREEN.blit(
                                    GAME_SPRITES['base'], (basex, GROUNDY))
                                pygame.display.update()
                                FPSCLOCK.tick(FPS)

                def mainGame():
                    score = 0
                    playerx = int(SCREENWIDTH / 5)
                    # playery = int(SCREENWIDTH/1.5)
                    playery = int(
                        (SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)

                    basex = 0

                    newPipe1 = getRandomPipe()
                    newPipe2 = getRandomPipe()

                    upperPipes = [
                        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
                        {'x': SCREENWIDTH + 200 +
                            (SCREENWIDTH / 2), 'y': newPipe2[0]['y']}
                    ]

                    lowerPipes = [
                        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
                        {'x': SCREENWIDTH + 200 +
                            (SCREENWIDTH / 2), 'y': newPipe2[1]['y']}
                    ]

                    pipeVelx = -4

                    playerVelY = -9
                    playerMaxVely = 10
                    playerMinVely = -8
                    playerAccY = 1

                    playerFlapAccv = -8
                    playerFlapped = False

                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                                if playery > 0:
                                    playerVelY = playerFlapAccv
                                    playerFlapped = True
                                    GAME_SOUNDS['wing'].play()

                        crashTest = isCollide(
                            playerx, playery, upperPipes, lowerPipes)
                        if crashTest:
                            PAUSE = True
                            return score

                        # scores
                        playerMidPos = playerx + \
                            GAME_SPRITES['player'].get_width() / 2
                        for pipe in upperPipes:
                            pipeMidPos = pipe['x'] + \
                                GAME_SPRITES['pipe'][0].get_width() / 2
                            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                                score += 1
                                print(f"Your score is {score}")
                                GAME_SOUNDS['point'].play()

                        if playerVelY < playerMaxVely and not playerFlapped:
                            playerVelY += playerAccY
                        if playerFlapped:
                            playerFlapped = False

                        playerHeight = GAME_SPRITES['player'].get_height()
                        playery = playery + \
                            min(playerVelY, GROUNDY - playery - playerHeight)

                        # moving the pipes
                        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                            upperPipe['x'] += pipeVelx
                            lowerPipe['x'] += pipeVelx

                        # Adding pipes
                        if 0 < upperPipes[0]['x'] < 5:
                            newpipe = getRandomPipe()
                            upperPipes.append(newpipe[0])
                            lowerPipes.append(newpipe[1])

                        # removing the pipes
                        if upperPipes[0]['x'] < - GAME_SPRITES['pipe'][0].get_width():
                            upperPipes.pop(0)
                            lowerPipes.pop(0)

                        # blit
                        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                            SCREEN.blit(
                                GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                            SCREEN.blit(
                                GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

                        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

                        myDigits = [int(x) for x in list(str(score))]
                        width = 0
                        for digit in myDigits:
                            width += GAME_SPRITES['numbers'][digit].get_width()
                        Xoffset = (SCREENWIDTH - width) / 2

                        for digit in myDigits:
                            SCREEN.blit(
                                GAME_SPRITES['numbers'][digit], (Xoffset, SCREENWIDTH * 0.12))
                            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

                        pygame.display.update()
                        FPSCLOCK.tick(FPS)

                def isCollide(playerx, playery, upperPipes, lowerPipes):
                    if playery > GROUNDY - 151 or playery < 0:
                        GAME_SOUNDS['hit'].play()
                        return True

                    for pipe in upperPipes:
                        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
                        if (playery < pipeHeight + pipe['y'] - 20 and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width() - 110):
                            GAME_SOUNDS['hit'].play()
                            return True

                    for pipe in lowerPipes:
                        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width() - 110:
                            GAME_SOUNDS['hit'].play()
                            return True

                    return False

                def getRandomPipe():
                    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
                    offset = SCREENHEIGHT/3
                    y2 = offset + \
                        random.randrange(
                            0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
                    pipeX = SCREENWIDTH + 10
                    y1 = pipeHeight - y2 + offset
                    pipe = [
                        {'x': pipeX, 'y': -y1},  # upper pipe
                        {'x': pipeX, 'y': y2}  # lower pipe
                    ]
                    return pipe

                if __name__ == "__main__":
                    pygame.init()
                    FPSCLOCK = pygame.time.Clock()
                    pygame.display.set_caption('The Flappy Bird Game')
                    GAME_SPRITES['numbers'] = (

                        pygame.image.load(
                            'Untitled-0.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-1.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-2.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-3.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-4.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-5.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-6.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-7.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-8.png').convert_alpha(),
                        pygame.image.load(
                            'Untitled-9.png').convert_alpha()

                    )

                    # Game Sprites
                    GAME_SPRITES['message'] = pygame.image.load(
                        'initial.png').convert_alpha()
                    GAME_SPRITES['base'] = pygame.image.load(
                        'main_ground.png').convert_alpha()
                    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                            pygame.image.load(PIPE).convert_alpha())
                    GAME_SPRITES['background'] = pygame.image.load(
                        BACKGROUND).convert()
                    GAME_SPRITES['player'] = pygame.image.load(
                        PLAYER).convert_alpha()

                    # Game Sounds
                    GAME_SOUNDS['die'] = pygame.mixer.Sound(
                        'die.mp3')
                    GAME_SOUNDS['hit'] = pygame.mixer.Sound(
                        'hit.mp3')
                    GAME_SOUNDS['point'] = pygame.mixer.Sound(
                        'point.mp3')
                    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound(
                        'swoosh.mp3')
                    GAME_SOUNDS['wing'] = pygame.mixer.Sound(
                        'wing.mp3')

                    def gameOverScreen(score):
                        # SCREEN.fill(0,0,0)
                        font = pygame.font.SysFont('arial', 60)
                        line1 = font.render(
                            f"Score : {score}", True, (0, 0, 0))
                        SCREEN.blit(
                            line1, (SCREENWIDTH/3 + 100, SCREENHEIGHT/2))
                        if score != 0:
                            line2 = font.render(
                                "To Play Again Press Enter", True, (255, 0, 0))
                            SCREEN.blit(
                                line2, (SCREENWIDTH/3 - 20, SCREENHEIGHT/3 + 40))
                        pygame.display.update()
                        # pause = True
                        time.sleep(1)

                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                            elif event.type == KEYDOWN and (event.key == K_RETURN):
                                PAUSE = False
                            else:
                                font = pygame.font.SysFont('arial', 60)
                                line1 = font.render(
                                    "Press Enter to Start", True, (255, 255, 255))
                                SCREEN.blit(
                                    line1, (SCREENWIDTH/3 + 30, SCREENHEIGHT/3 + 40))
                                pygame.display.update()
                                # gameOverScreen(0)
                                PAUSE = True
                        if not PAUSE:
                            welcomeScreen()
                            score = mainGame()
                            gameOverScreen(score)

            if connect_button.draw(screen):
                import numpy as np
                import pygame
                import sys
                import math
                import time

                ROW_COUNT = 7
                COLUMN_COUNT = 12
                CONNECT = 4
                BLUE = (3, 144, 252)
                BLACK = (0, 0, 0)
                RED = (232, 12, 12)
                YELLOW = (252, 161, 3)
                pygame.display.set_caption("Connect Four")


                def create_board():
                    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
                    return board

                # piece = 1 for player 1 and 2 for player 2
                def drop_piece(board, row, col, piece):
                    board[row][col] = piece

                # to check if the column is still free
                # numbering of rows is as follows

                def is_valid_location(board, col):
                    return board[ROW_COUNT - 1][col] == 0

                # to check which row the next piece will fall in
                def get_next_open_row(board, col):
                    for r in range(ROW_COUNT):
                        if board[r][col] == 0:
                            return r

                # flip the board - to start from bottom up
                def print_board(board):
                    # 0 is the x axis
                    print(np.flip(board, 0))

                # to check if we have won
                def winning_move(board, piece):
                    # check all horizontal locations
                    for c in range(COLUMN_COUNT - (CONNECT-1)):
                        for r in range(ROW_COUNT):
                            count = 0
                            for x in range(CONNECT):
                                if board[r][c + x] == piece:
                                    count += 1
                            if count == CONNECT:
                                return True

                    # check all vertical locations
                    for c in range(COLUMN_COUNT):
                        for r in range(ROW_COUNT - (CONNECT-1)):
                            count = 0
                            for x in range(CONNECT):
                                if board[r+x][c] == piece:
                                    count += 1
                            if count == CONNECT:
                                return True

                    # check for positive slope diagonals
                    for c in range(COLUMN_COUNT - (CONNECT - 1)):
                        for r in range(ROW_COUNT - (CONNECT), ROW_COUNT):
                            count = 0
                            for x in range(CONNECT):
                                if board[r-x][c+x] == piece:
                                    count += 1
                            if count == CONNECT:
                                return True

                    # check for the negative slope diagonals
                    for c in range(COLUMN_COUNT - (CONNECT-1)):
                        for r in range(ROW_COUNT - (CONNECT - 1)):
                            count = 0
                            for x in range(CONNECT):
                                if board[r+x][c+x] == piece:
                                    count += 1
                            if count == CONNECT:
                                return True

                # drawing the board with pygame graphics
                def draw_board(board):
                    # draw squares(rectangles here) and then draw circles on top of them
                    for c in range(COLUMN_COUNT):
                        for r in range(ROW_COUNT):
                            pygame.draw.rect(
                                screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                            pygame.draw.circle(
                                screen, BLACK, (c*SQUARESIZE + SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), RADIUS)

                    for c in range(COLUMN_COUNT):
                        for r in range(ROW_COUNT):
                            if board[r][c] == 1:
                                pygame.draw.circle(
                                    screen, RED, (c*SQUARESIZE + SQUARESIZE/2, height - (r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
                            elif board[r][c] == 2:
                                pygame.draw.circle(
                                    screen, YELLOW, (c*SQUARESIZE + SQUARESIZE/2, height - (r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
                    pygame.display.update()

                board = create_board()
                print_board(board)
                game_over = False
                turn = 0

                # initialising pygame
                pygame.init()
                SQUARESIZE = 100
                width = COLUMN_COUNT * SQUARESIZE
                height = (ROW_COUNT + 1) * SQUARESIZE
                size = (width, height)

                # we have subtracted any arbitrary int value
                RADIUS = int(SQUARESIZE/2 - 5)

                screen = pygame.display.set_mode(size)
                draw_board(board)
                pygame.display.update()

                FONTSIZE = 75
                myfont = pygame.font.SysFont("monospace", FONTSIZE)

                while not game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.MOUSEMOTION:
                            pygame.draw.rect(
                                screen, BLACK, (0, 0, width, SQUARESIZE))
                            posx = event.pos[0]
                            if turn == 0:
                                pygame.draw.circle(
                                    screen, RED, (posx, SQUARESIZE/2), RADIUS)
                            else:
                                pygame.draw.circle(
                                    screen, YELLOW, (posx, SQUARESIZE/2), RADIUS)
                            pygame.display.update()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            # print(event.pos)
                            # Ask for player 1 Input
                            if turn == 0:
                                posx = event.pos[0]
                                col = math.floor(posx / SQUARESIZE)
                                if is_valid_location(board, col):
                                    row = get_next_open_row(board, col)
                                    drop_piece(board, row, col, 1)

                                    if winning_move(board, 1):
                                        # print("Player 1 Wins !")
                                        pygame.draw.rect(
                                            screen, BLACK, (0, 0, width, SQUARESIZE))
                                        label = myfont.render(
                                            "Player 1 won !!", 1, RED)
                                        screen.blit(label, (250, 10))
                                        game_over = True

                            # #Ask for player 2 Input
                            else:
                                posx = event.pos[0]
                                col = math.floor(posx / SQUARESIZE)
                                if is_valid_location(board, col):
                                    row = get_next_open_row(board, col)
                                    drop_piece(board, row, col, 2)

                                    if winning_move(board, 2):
                                        # print("Player 2 Wins !")
                                        pygame.draw.rect(
                                            screen, BLACK, (0, 0, width, SQUARESIZE))
                                        label = myfont.render(
                                            "Player 2 won!!", 1, YELLOW)
                                        screen.blit(label, (250, 10))
                                        game_over = True

                            print_board(board)
                            draw_board(board)
                            # alternate between zero and one
                            turn += 1
                            turn = turn % 2
                        if game_over:
                            pygame.time.wait(5000)

            if snake_button.draw(screen):
                import pygame
                #for certain keywords like KEYDOWN
                from pygame.locals import *
                import time
                import random

                #block size and apple size
                SIZE = 40
                SPEED = 40
                HEIGHT = 800
                WIDTH = 1200
                LEVEL = 1
                BACKGROUNDCOLOR = (255,255,255)
                pygame.display.set_caption("Snake Game")


                class Apple:
                    def __init__(self, parent_screen) -> None:
                        self.image = pygame.image.load("apple.jpg").convert()
                        self.parent_screen = parent_screen

                        #position of apple will be in multiples of block size
                        self.x = SIZE * 3
                        self.y = SIZE * 3

                    def draw(self):
                        self.parent_screen.blit(self.image,(self.x, self.y))
                        pygame.display.update()

                    def move(self):
                        # x-increments: width/applesize = 1000/40 = 25
                        # y-increments : height/applesize = 800/40 = 20
                        self.x = random.randint(0,24) * SIZE
                        self.y = random.randint(0,19) * SIZE




                class Snake:
                    def __init__(self, parent_screen,length) -> None:
                        #loading an image
                        self.block = pygame.image.load("block.jpg").convert()
                        #all blocks are at same position- the move logic will unwrap the snake
                        self.x = [SIZE] * length
                        self.y = [SIZE] * length
                        self.parent_screen = parent_screen
                        self.direction = 'down'
                        self.length = length
                    
                    def increase_length(self):
                        self.length += 1
                        #adding new element int he array
                        self.x.append(-1)
                        self.y.append(-1)
                    
                    def draw(self):
                        # self.parent_screen.fill(BACKGROUNDCOLOR)
                        for i in range(self.length):
                            #blit means draw this image
                            self.parent_screen.blit(self.block, (self.x[i],self.y[i]))
                        # pygame.display.update()

                    def move_left(self):
                        self.direction = 'left'
                    
                    def move_right(self):
                        self.direction = 'right'
                    
                    def move_up(self):
                        self.direction = 'up'

                    def move_down(self):
                        self.direction = 'down'

                    def walk(self):
                        for i in range(self.length - 1, 0, -1):
                            self.x[i] = self.x[i-1]
                            self.y[i] = self.y[i-1]
                        global SPEED
                        if self.direction == 'up':
                            self.y[0] -= SPEED
                        if self.direction == 'down':
                            self.y[0] += SPEED
                        if self.direction == 'right':
                            self.x[0] += SPEED
                        if self.direction == 'left':
                            self.x[0] -= SPEED
                        
                        self.draw()
                

                class Game:
                    def __init__(self) -> None:
                        #initiate pygame
                        pygame.init()
                        #inititae pygame sounds
                        pygame.mixer.init()
                        self.play_bg_music()
                        self.surface = pygame.display.set_mode((WIDTH,HEIGHT))
                        # self.surface.fill(BACKGROUNDCOLOR)
                        self.render_background()
                        pygame.display.update()


                        #creating a snake inside the game
                        self.snake = Snake(self.surface,1)
                        self.snake.draw()

                        #creating an apple inside the game
                        self.apple = Apple(self.surface)
                        self.apple.draw()

                    def is_collision(self, x1,y1, x2, y2):
                        #snake - x1,y2
                        #apple - x2,y2
                        if x1 == x2 and y1 == y2:
                            return True
                        return False

                    def render_background(self):
                        #our background img size is larger than our window size, hence it'll work fine
                        bg = pygame.image.load("background.jpg")
                        self.surface.blit(bg,(0,0))


                    def play_sound(self,name):
                        sound = pygame.mixer.Sound(f"{name}.mp3")
                        pygame.mixer.Sound.play(sound)

                    def play_bg_music(self):
                        #sound is a one time thing - like a crash or ding
                        #music is long - like background music
                        pygame.mixer.music.load("bg_music_1.mp3")
                        pygame.mixer.music.play()

                    def display_score(self):
                        font = pygame.font.SysFont('arial', 40)
                        score = font.render(f"Score : {self.snake.length}", True, (255,255,255))
                        self.surface.blit(score,(800,10))

                    def play(self):
                        self.render_background()
                        self.snake.walk()
                        self.apple.draw()
                        self.display_score()
                        pygame.display.update()

                        #collision with apple
                        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                            self.play_sound("ding")
                            self.snake.increase_length()
                            self.apple.move()

                        #snake colliding with itself
                        for i in range(3, self.snake.length - 1):
                            if self.is_collision(self.snake.x[0], self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                                # self.play_sound("crash")
                                raise "Game Over"
                        
                        if self.snake.x[0] >= WIDTH or self.snake.x[0] < 0 or self.snake.y[0] >= HEIGHT or self.snake.y[0]< 0:
                            # self.play_sound("crash")
                            raise "Game Over"

                    def show_game_over(self):
                        # self.surface.fill(BACKGROUNDCOLOR)
                        self.render_background()
                        font = pygame.font.SysFont('arial', 40)
                        line1 = font.render(f"Score : {self.snake.length}", True, (255,255,255))
                        self.surface.blit(line1,(WIDTH/4,HEIGHT/2))
                        line2 = font.render("To Play Again Hit Enter", True, (255,255,255))
                        self.surface.blit(line2,(WIDTH/2,HEIGHT/2))
                        pygame.display.update()
                        #to stop the music
                        pygame.mixer.music.stop()
                        # pygame.mixer.music.pause()

                    def reset(self):
                        #reinitialise
                        self.snake = Snake(self.surface, 1)
                        self.apple = Apple(self.surface)

                    def main(self):
                        running = True
                        pause = False
                        #event loop - it waits for the user input 
                        #also without this loop the window will not stay on the screen 
                        while running:
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        running = False
                                    if event.key == K_RETURN:
                                        pause = False
                                        self.play_bg_music()

                                        # pygame.mixer.music.unpause()
                                    if not pause:
                                        if event.key == K_UP and self.snake.direction != 'down':
                                            self.snake.move_up()
                                        if event.key == K_DOWN and self.snake.direction != 'up':
                                            self.snake.move_down()
                                        if event.key == K_RIGHT and self.snake.direction != 'left':
                                            self.snake.move_right()
                                        if event.key == K_LEFT and self.snake.direction != 'right':
                                            self.snake.move_left()
                                elif event.type == QUIT:
                                    running = False
                            #even if we dont press any key the snake will move
                            
                            try:
                                if not pause:
                                    self.play()
                            except Exception as e:
                                self.show_game_over()
                                pause = True
                                self.reset()
                            #the while loop runs very fast so we introduce some delay
                            time.sleep(0.2)
                            

                if __name__ == "__main__":
                    game = Game()
                    game.main()

            if car_button.draw(screen):
                import pygame
                from pygame.locals import *
                import random
                import sys
                from string import digits
                import time

                size = width, height = (800,800)
                road_w = int (width/1.6)
                roadmark_w = int (width/80)
                right_lane = width/2 + road_w/4
                left_lane = width/2 - road_w/4
                speed =2
                speed_tree= 1
                level = 1

                #initialise our pygame application
                pygame.init()
                running = True 

                #setting our window size
                screen = pygame.display.set_mode(size)

                #title
                pygame.display.set_caption("Car Game")

                #background color
                screen.fill((60,220,0))

                #load images

                car = pygame.image.load("car1.png")
                #first we fetch the location then assign it
                car_loc = car.get_rect()
                #positioning the center of the car
                car_loc.center = right_lane, height * 0.8

                car2 = pygame.image.load("otherCar.png")
                #first we fetch the location then assign it
                car2_loc = car2.get_rect()
                #positioning the center of the car
                car2_loc.center = left_lane, height * 0.2


                #trees
                tree = pygame.image.load("tree2.png")
                tree2 = pygame.image.load("tree2.png")
                tree3 = pygame.image.load("tree3.png")
                tree4 = pygame.image.load("tree4.png")
                # tree5 = pygame.image.load("car_game\\Car_Game_images\\tree5.png")

                tree_loc = tree.get_rect()
                tree_loc2 = tree2.get_rect()
                tree_loc3 = tree3.get_rect()
                tree_loc4 = tree4.get_rect()

                tree_loc.center = left_lane - 230, height * 0.32
                tree_loc2.center = left_lane - 250, height * 0.80
                tree_loc3.center = right_lane + 220, height * 0.50
                tree_loc4.center = right_lane + 240, height * 0.1


                counter = 0
                FPSCLOCK = pygame.time.Clock()
                pause = False

                while running:
                    if not pause:
                        counter += 1
                        if counter == 2500:
                            speed += 0.70
                            speed_tree += 0.35
                            counter = 0
                            level += 1
                            print("Level Up!", speed)
                        #animate enemy vehicle(Everytime we go through the while loop the car moves 1 pixel down)
                        
                        y = car2_loc.center[1]
                        y1 = tree_loc.center[1]
                        y2 = tree_loc2.center[1]
                        y3 = tree_loc3.center[1]
                        y4 = tree_loc4.center[1]

                        car2_loc.center = car2_loc.center[0], y+speed
                        tree_loc.center = tree_loc.center[0], y1+speed_tree 
                        tree_loc2.center = tree_loc2.center[0], y2+speed_tree 
                        tree_loc3.center = tree_loc3.center[0], y3+speed_tree 
                        tree_loc4.center = tree_loc4.center[0], y4+speed_tree 


                        if car2_loc[1] > height:
                            if random.randint(0,1) == 0:
                                car2_loc.center = right_lane, -300

                            else:
                                car2_loc.center = left_lane, -300

                        if tree_loc[1] > height:
                            tree_loc.center = left_lane - 230, -200
                        if tree_loc2[1] > height:
                            tree_loc2.center = left_lane - 250, -900
                        if tree_loc3[1] > height:
                            tree_loc3.center = right_lane + 220, -500
                        if tree_loc4[1] > height:
                            tree_loc4.center = right_lane + 240, -50
                            

                        #end game condition
                        #250 is the image size
                        if car2_loc[0] == car_loc[0] and car2_loc[1] > car_loc[1] - 250 and car2_loc[1] < car_loc[1] +240:
                            print("GAME OVER !")
                            car_loc.center = right_lane, height * 0.8
                            car2_loc.center = left_lane, height * 0.2
                            pause = True
                            time.sleep(2)

                            screen.fill((60,220,0))

                            #road
                            pygame.draw.rect(
                                screen,
                                #color
                                (50,50,50),
                                #(starting horizontal, starting vectical, horizontal width, vertical height)
                                ((width/2 - road_w/2, 0,road_w, height))
                            )
                            #roadmark
                            pygame.draw.rect(
                                screen,
                                (255, 240, 60),
                                (width/2 - roadmark_w/2, 0, roadmark_w, height)
                            )
                            #side white marks
                            pygame.draw.rect(
                                screen,
                                (255, 255, 255),
                                (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
                            )
                            pygame.draw.rect(
                                screen,
                                (255, 255, 255),
                                (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
                            )
                            
                            print("fdfdj")
                            

                            # break
                    if pause:
                        font = pygame.font.Font('freesansbold.ttf', 30)
                        line1 = font.render("Press Enter to Start Again", True, (255,0,0))
                        screen.blit(line1,(width/4,height/2))
                        pygame.display.update()
                        FPSCLOCK.tick(32)

                    #iterate over all the events of our application
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                        #Select all the keys of the keyboard
                        if event.type == KEYDOWN:
                            if event.key == K_RETURN:
                                speed = 1
                                level = 1
                                pause = False
                            if not pause:
                                if event.key in [K_a, K_LEFT]:
                                    car_loc = car_loc.move([-int(road_w/2),0])
                                if event.key in [K_d, K_RIGHT]:
                                    car_loc = car_loc.move([int(road_w/2),0])
                        
                    #draw graphics
                    if not pause:
                        screen.fill((60,220,0))

                        #road
                        pygame.draw.rect(
                            screen,
                            #color
                            (50,50,50),
                            #(starting horizontal, starting vectical, horizontal width, vertical height)
                            ((width/2 - road_w/2, 0,road_w, height))
                        )

                        #roadmark
                        pygame.draw.rect(
                            screen,
                            (255, 240, 60),
                            (width/2 - roadmark_w/2, 0, roadmark_w, height)
                        )
                        #side white marks
                        pygame.draw.rect(
                            screen,
                            (255, 255, 255),
                            (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
                        )
                        pygame.draw.rect(
                            screen,
                            (255, 255, 255),
                            (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
                        )

                    
                        #draw images 
                        screen.blit(car, car_loc)
                        screen.blit(car2, car2_loc)
                        screen.blit(tree, tree_loc)
                        screen.blit(tree2, tree_loc2)
                        screen.blit(tree3, tree_loc3)
                        screen.blit(tree4, tree_loc4)




                        #level
                        fontsize = 30
                        font = pygame.font.Font('freesansbold.ttf', fontsize)
                        line1 = font.render(f"Level   :  {level}", True, (255, 151, 138))
                        screen.blit(line1,(width*0.3 -fontsize/2 ,40))
                                
                        pygame.display.update()

                #collapsing our application window as soon as we are done using it
                pygame.quit()
           
            if quit_button.draw(screen):
                run = False
    else:
        draw_text("PIXEL PLAYZONE", font, font2_col, 300, 250)
        draw_text("Press SPACE to start", font2, TEXT_COL, 415, 370)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
