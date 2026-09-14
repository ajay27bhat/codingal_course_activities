import pygame
import random

pygame.init()

# -------------------------
# Setup
# -------------------------

# Screen
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invader")

# Images
background = pygame.image.load("python_course/M6/L5_L6/background.jpg")
player_img = pygame.image.load("python_course/M6/L5_L6/player.png")
enemy_img = pygame.image.load("python_course/M6/L5_L6/enemy.png")
bullet_img = pygame.image.load("python_course/M6/L5_L6/bullet.png")

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 64)

clock = pygame.time.Clock()

# -------------------------
# Player
# -------------------------

player_x = 370
player_y = 380
player_speed = 0

# Move player
def move_player(x, speed):
    x += speed

    if x < 0:
        x = 0

    if x > 736:
        x = 736

    return x


# -------------------------
# Enemies
# -------------------------


enemies = []

for i in range(6):

    x = random.randint(0, 736)
    y = random.randint(50, 150)

    # [x position, y position, speed]
    enemies.append([x, y, 4])

def move_enemies(enemies):

    for e in enemies:

        e[0] += e[2]

        # Change direction at the edge
        if e[0] <= 0 or e[0] >= 736:
            e[2] = -e[2]
            e[1] += 40

    return enemies


# -------------------------
# Bullet
# -------------------------

bullet_x = 0
bullet_y = 380
bullet_fired = False


# -------------------------
# Game Loop
# -------------------------

running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_speed = -5

            if event.key == pygame.K_RIGHT:
                player_speed = 5

            if event.key == pygame.K_SPACE:
                if not bullet_fired:
                    bullet_x = player_x + 16
                    bullet_y = player_y
                    bullet_fired = True

        # Key released
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player_speed = 0

            if event.key == pygame.K_RIGHT:
                player_speed = 0


    # Game updates

    # Update Player
    player_x = move_player(player_x, player_speed)

    # Update Enemies
    enemies = move_enemies(enemies)

    # Update Bullet
    if bullet_fired:
    
        bullet_y -= 10

        # Reset bullet when it leaves screen
        if bullet_y < 0:
            bullet_fired = False


    # -------------------------
    # Draw
    # -------------------------

    # Background
    screen.blit(background, (0, 0))

    # Enemies
    for e in enemies:
        screen.blit(enemy_img, (e[0], e[1]))

    # Bullet
    if bullet_fired:
        screen.blit(bullet_img, (bullet_x, bullet_y))

    # Player
    screen.blit( player_img, (player_x, player_y))


    # Update screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)


pygame.quit()