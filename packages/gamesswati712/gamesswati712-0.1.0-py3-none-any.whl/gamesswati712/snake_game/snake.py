import pygame
#for certain keywords like KEYDOWN
from pygame.locals import *
import time
import random

#block size and apple size
SIZE = 40
SPEED = 40
HEIGHT = 800
WIDTH = 1000
LEVEL = 1
BACKGROUNDCOLOR = (255,255,255)

class Apple:
    def __init__(self, parent_screen) -> None:
        self.image = pygame.image.load("snake_game\\snakeGame-images\\apple.jpg").convert()
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
        self.block = pygame.image.load("snake_game\\snakeGame-images\\block.jpg").convert()
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
        bg = pygame.image.load("snake_game\\snakeGame-images\\background.jpg")
        self.surface.blit(bg,(0,0))


    def play_sound(self,name):
        sound = pygame.mixer.Sound(f"snake_game\\snakeGame-sounds\\{name}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_bg_music(self):
        #sound is a one time thing - like a crash or ding
        #music is long - like background music
        pygame.mixer.music.load("snake_game\\snakeGame-sounds\\bg_music_1.mp3")
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















# collision logic - collision with last block
# what is raise "game over"
# border conditions
# increase the speed
   
    
    
    

    

