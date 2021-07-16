import pygame

pygame.init()

# Configuramos la pantalla
screen = pygame.display.set_mode((800, 600))

# Título e icono
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("./images/space-invaders.png")
pygame.display.set_icon(icon)

# Background
backgroundImg = pygame.image.load("./images/background.png")

def background():
    screen.blit(backgroundImg,(0, 0))

# Player
playerImg = pygame.image.load("./images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Enemigo
enemyImg = pygame.image.load("./images/enemy.png")
enemyX = 64
enemyY = 50
enemyX_change = 2
enemyY_change = 5

def enemy(x,y):
    screen.blit(enemyImg, (x, y))


# Loop de la aplicación
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT: 
                playerX_change = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # RGB
    #screen.fill((0, 0, 30))
    background()

    playerX += playerX_change

    if playerX >= 736:
        playerX = 736
    elif playerX <= 0:
        playerX = 0

 
    player(playerX, playerY)


    # Movimiento del enemigo   
    enemyX += enemyX_change
    

    if int(enemyX) >= 736:
        enemyX_change = -2
        enemyY += enemyY_change
    elif int(enemyX) <= 0:
        enemyX_change = 2
        enemyY += enemyY_change

      
    enemy(enemyX , enemyY)


    pygame.display.update()




