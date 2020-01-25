import pygame
import random
import os
import time

pygame.init()
pygame.mixer.init()




# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,255,0)

screen_width = 900
screen_height = 600
game_window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.update()

bgimage = pygame.image.load("Images/check.jpg")
bgimage = pygame.transform.scale(bgimage, (screen_width, screen_height))


fps =40
pygame.display.set_caption("Snake World")
font=pygame.font.SysFont(None,40)
clock=pygame.time.Clock()

def welcome_screen():
    exit_game=False
    while not exit_game:
        game_window.fill((233,220,229))
        bgimge = pygame.image.load("Images/snake1.png")
        bgimge = pygame.transform.scale(bgimge, (screen_width, screen_height))
        game_window.blit(bgimge,(0,0))
        # text_sceen("Wecome To Snakes",black, 180, 200)
        # text_sceen("Press Space To Play", red, 180, 250)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:

                    game_loop()
        pygame.display.update()
        clock.tick(60)



#displaying message on screen
def text_sceen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])


def plot_head(game_window,color1,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, color1, [x, y, snake_size, snake_size])

def game_loop():
    # for continously playing music we use -1
    pygame.mixer.music.load('Music/Nagin.mp3')
    pygame.mixer.music.play(-1)

    # if a file is not present then it make it
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")


    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    score = 0
    velocity_x = 0
    velocity_y = 0
    initvelocity = 5
    snake_size = 20
    snake_length = 1
    snake_list = []
    food_x = random.randint(10, screen_width / 2)
    food_y = random.randint(10, screen_height /2 )

    while not exit_game:
        if game_over:
            pygame.mixer.music.pause()

            game_window.fill(white)
            bgimge = pygame.image.load("Images/gameover.jpg")
            bgimge = pygame.transform.scale(bgimge, (screen_width, screen_height)).convert_alpha()
            game_window.blit(bgimge, (0, 0))

            text_sceen("Your Score is:"+str(score),red,350,150)
            text_sceen("Press Enter To Play Again!", red, 290, 450)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load('Music/Nagin.mp3')
                        pygame.mixer.music.play()
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        quit()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=initvelocity
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-initvelocity
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-initvelocity
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y = +initvelocity
                        velocity_x = 0



            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

#For eating the food
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=10
                food_x = random.randint(10, screen_width/2)
                food_y = random.randint(10, screen_height/2)
                snake_length+=5
                if score>int(hiscore):
                    hiscore=score
                    with open("hiscore.txt", "w") as x:
                        x.write(str(hiscore))

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('Music/Explosion.mp3')
                pygame.mixer.music.play()
                time.sleep(0.5)




            if snake_x<0 or snake_x>screen_width  or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('Music/Explosion.mp3')
                pygame.mixer.music.play()
                time.sleep(0.5)



            game_window.fill(white)
            game_window.blit(bgimage,(0,0))
            plot_head(game_window, black,snake_list, snake_size)
            pygame.draw.rect(game_window,red,[food_x, food_y, snake_size, snake_size])
            text_sceen("Score:" + str(score), red, 5, 5)
            text_sceen("HighScore:" + str(hiscore), green, 700, 5)


        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
welcome_screen()
# game_loop()
