import pygame
import random
import math

pygame.init()

height = 300
width = 550

screen = pygame.display.set_mode([height,width])

pygame.display.set_caption("game pertama ici")

icon = pygame.image.load("roket.jpg")
pygame.display.set_icon(icon)

def player(x,y):
    img_player = pygame.image.load("spaceship.png")
    screen.blit(img_player,(x,y))

x_player = 140
y_player = 510
x_player_point = 0

def enemy(x,y):
    img_enemy = pygame.image.load("musuh.png")
    screen.blit(img_enemy,(x,y))

x_enemy = random.randint(50,200)
y_enemy = random.randint(5,10)
y_enemy_point = 6

def collision(x_player,y_player, x_enemy,y_enemy):
    distance = math.sqrt(math.pow(x_player-x_enemy,2)) + (math.pow(y_player-y_enemy,2))
    if distance < 10:
        return True
    else:
        return False
    
score = 0
font = pygame.font.Font("freesansbold.ttf",16)

def shhow_score(x,y):
    score_number = font.render("SCORE : "+ str(score), True,(225,225,225))
    screen.blit(score_number,(x,y))

x_score = 10
y_score = 10

cloak = pygame.time.Clock()

run = True
while run:
    screen.fill((0,0,0))    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player -= 5
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player -= 0
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player += 0

    x_player += x_player_point
    if x_player >= 270:
        x_player = 260
    if x_player <= 10:
        x_player = 35

    y_enemy += y_enemy_point
    if y_enemy >= 540:
        x_enemy = random.randint(50,200)
        y_enemy = random.randint(5,10)
        score += 1

    tabrakan = collision(x_player,y_player,x_enemy,y_enemy)
    if tabrakan:
        break

    cloak.tick(60)

    player(x_player, y_player)
    enemy(x_enemy,y_enemy)
    shhow_score(x_score,y_score)
    pygame.display.update()

pygame.quit()

print("score anda : ",score)
    