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
speed =1
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

car = pygame.image.load("car_game\\Car_Game_images\\car.png")
#first we fetch the location then assign it
car_loc = car.get_rect()
#positioning the center of the car
car_loc.center = right_lane, height * 0.8

car2 = pygame.image.load("car_game\Car_Game_images\otherCar.png")
#first we fetch the location then assign it
car2_loc = car2.get_rect()
#positioning the center of the car
car2_loc.center = left_lane, height * 0.2


#trees
tree = pygame.image.load("car_game\\Car_Game_images\\tree.png")
tree2 = pygame.image.load("car_game\\Car_Game_images\\tree2.png")
tree3 = pygame.image.load("car_game\\Car_Game_images\\tree3.png")
tree4 = pygame.image.load("car_game\\Car_Game_images\\tree4.png")
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
            speed += 0.30
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
