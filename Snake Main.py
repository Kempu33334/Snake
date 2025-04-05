import pygame
import time
import random
import math

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake")

background = pygame.image.load('Snake Background.png')

length_snake = 5
playerX = 200
playerY = 200
playerIMG = pygame.image.load('blue-square.png')
snakeX = []
snakeY = []
playerIMGlist = []
lastkey = "0"

for i in range(length_snake-1):
    snakeX.append(200-(20*i))
    snakeY.append(200)
    playerIMGlist.append(playerIMG)

appleX = 20*round(random.randint(0,380)/20)
appleY = 20*round(random.randint(0,380)/20)

while math.sqrt(math.pow(playerX-appleX,2)+math.pow(playerY-appleY,2)) < 5:
    appleX = 20*round(random.randint(0,380)/20)
    appleY = 20*round(random.randint(0,380)/20)

running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if (lastkey != "right" and lastkey != "d") and lastkey != "0":
                    lastkey = "left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if lastkey != "left" and lastkey != "a":
                    lastkey = "right"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if lastkey != "down" and lastkey != "s":
                    lastkey = "up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if lastkey != "up" and lastkey != "w":
                    lastkey = "down"
    if lastkey != "0":
        for j in range(length_snake-2):
            snakeX[length_snake-j-2] = snakeX[length_snake-j-3]
            snakeY[length_snake-j-2] = snakeY[length_snake-j-3]
        if lastkey == "left" or lastkey == "a":
            playerX -= 20
            playerY = 20*round(playerY/20)
        if lastkey == "right" or lastkey == "d":
            playerX += 20
            playerY = 20*round(playerY/20)
        if lastkey == "up" or lastkey == "w":
            playerY -= 20
            playerX = 20*round(playerX/20)
        if lastkey == "down" or lastkey == "s":
            playerY += 20
            playerX = 20*round(playerX/20)
        for t in range(len(snakeX)-1):
            if playerX == snakeX[t] and playerY == snakeY[t]:
                running = False
    snakeX[0] = playerX
    snakeY[0] = playerY
    if playerX > 380:
        playerX = 380
        break
    if playerX < 0:
        playerX = 0
        break
    if playerY > 380:
        playerY = 380
        break
    if playerY < 0:
        playerY = 0
        break
    if playerX == appleX and playerY == appleY:
        appleX = 20*round(random.randint(0,380)/20)
        appleY = 20*round(random.randint(0,380)/20)
        while math.sqrt(math.pow(playerX-appleX,2)+math.pow(playerY-appleY,2)) < 5:
            appleX = 20*round(random.randint(0,380)/20)
            appleY = 20*round(random.randint(0,380)/20)
        length_snake = length_snake + 1
        snakeX.append(snakeX[-1])
        snakeY.append(snakeY[-1])
        playerIMGlist.append(playerIMG)
    for g in range(length_snake-1):
        screen.blit(playerIMGlist[g], (snakeX[g], snakeY[g]))
    screen.blit(pygame.image.load('apple.jpg'),(appleX,appleY))
    pygame.display.update()
    time.sleep(0.1)
