import math
import random
import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("media/space_stars.jpg")

# Background sound
mixer.music.load("media/retro27.mp3")
mixer.music.play(-1)

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("media/rocket.png")
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("media/arcade-game.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("media/ufo.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet
bullet_img = pygame.image.load("media/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Score font
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)
restart_font = pygame.font.Font("freesansbold.ttf", 32)

# Sounds
explosion_sound = mixer.Sound("media/explosion.mp3")  # play when UFO hit
crash_sound = mixer.Sound("media/crash.mp3")  # play when alien reaches bottom


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(400, 250))
    screen.blit(over_text, text_rect)

    restart_text = restart_font.render("Press ENTER to Restart", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(400, 350))
    screen.blit(restart_text, restart_rect)


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < 27


# Game loop
running = True
game_over = False

while running:
    # Background image
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart if game over
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Reset everything
                game_over = False
                score_value = 0
                playerX = 370
                playerY = 480
                playerX_change = 0
                bulletY = 480
                bullet_state = "ready"
                enemyX = [random.randint(0, 735) for _ in range(num_of_enemies)]
                enemyY = [random.randint(50, 150) for _ in range(num_of_enemies)]
                enemyX_change = [1 for _ in range(num_of_enemies)]
                enemyY_change = [40 for _ in range(num_of_enemies)]

                mixer.music.play(-1)  # restart background music

        # Normal controls only if game not over
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -4
                elif event.key == pygame.K_RIGHT:
                    playerX_change = 4
                elif event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    playerX_change = 0

    if not game_over:
        # Player Movement
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        # Enemy Movement + Collision
        for i in range(num_of_enemies):

            # Game over condition
            if enemyY[i] > 440:
                mixer.music.stop()  # stop background music
                crash_sound.play()  # play crash sound
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over = True
                break

            enemyX[i] += enemyX_change[i]

            if enemyX[i] <= 0:
                enemyX_change[i] = 1
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -1
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_sound.play()  # play explosion on hit
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 735)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        # Draw player
        player(playerX, playerY)

        # Show score
        show_score(textX, textY)
    else:
        game_over_text()

    # Update display
    pygame.display.update()
