import pygame
import random

pygame.init()

# -------------------------
# Setup
# -------------------------

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invader")

# Images
background = pygame.image.load(
    "python_course/M6/L5_L6/background.jpg"
)

player_img = pygame.image.load(
    "python_course/M6/L5_L6/player.png"
)

enemy_img = pygame.image.load(
    "python_course/M6/L5_L6/enemy.png"
)

bullet_img = pygame.image.load(
    "python_course/M6/L5_L6/bullet.png"
)

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 64)

clock = pygame.time.Clock()


# -------------------------
# Player
# -------------------------

player_x = 370
player_y = 380
player_speed = 0


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

    # [x, y, speed]
    enemies.append([x, y, 4])


def move_enemies(enemies):

    for e in enemies:

        e[0] += e[2]

        # Enemy reaches the edge
        if e[0] <= 0 or e[0] >= 736:

            e[2] = -e[2]
            e[1] += 40

    return enemies


# -------------------------
# Collision
# -------------------------

def check_collision(enemies, bullet_x, bullet_y):

    for e in enemies:

        enemy_rect = pygame.Rect(
            e[0], e[1], 64, 64
        )

        bullet_rect = pygame.Rect(
            bullet_x, bullet_y, 32, 32
        )

        if bullet_rect.colliderect(enemy_rect):

            # Put enemy back at the top
            e[0] = random.randint(0, 736)
            e[1] = random.randint(50, 150)

            return True

    return False


# -------------------------
# Game Over
# -------------------------

def check_game_over(enemies):

    for e in enemies:

        if e[1] >= 340:
            return True

    return False


# -------------------------
# Draw Score
# -------------------------

def draw_score(screen, score):

    text = font.render(
        "Score: " + str(score),
        True,
        "white"
    )

    screen.blit(text, (10, 10))


# -------------------------
# Draw Game Over
# -------------------------

def draw_game_over(screen):

    text = game_over_font.render(
        "GAME OVER",
        True,
        "white"
    )

    x = (800 - text.get_width()) // 2
    y = (500 - text.get_height()) // 2

    screen.blit(text, (x, y))


# -------------------------
# Bullet
# -------------------------

bullet_x = 0
bullet_y = 380
bullet_fired = False


# -------------------------
# Score
# -------------------------

score = 0
game_over = False
running = True


# -------------------------
# Game Loop
# -------------------------

while running:

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Move left
            if event.key == pygame.K_LEFT:
                player_speed = -5

            # Move right
            if event.key == pygame.K_RIGHT:
                player_speed = 5

            # Shoot
            if event.key == pygame.K_SPACE:

                if not bullet_fired:
                    bullet_x = player_x + 16
                    bullet_y = player_y
                    bullet_fired = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player_speed = 0

            if event.key == pygame.K_RIGHT:
                player_speed = 0


    # -------------------------
    # Update Game
    # -------------------------

    if not game_over:

        # Move player
        player_x = move_player(
            player_x,
            player_speed
        )

        # Move enemies
        enemies = move_enemies(enemies)

        # Check game over
        game_over = check_game_over(enemies)

        # Move bullet
        if bullet_fired:

            bullet_y -= 10

            # Bullet leaves screen
            if bullet_y < 0:
                bullet_fired = False

        # Check collision
        if bullet_fired:

            hit = check_collision(
                enemies,
                bullet_x,
                bullet_y
            )

            if hit:
                score += 1
                bullet_fired = False


    # -------------------------
    # Draw
    # -------------------------

    screen.blit(
        background,
        (0, 0)
    )

    # Draw enemies
    if not game_over:

        for e in enemies:

            screen.blit(
                enemy_img,
                (e[0], e[1])
            )

    # Draw bullet
    if bullet_fired:

        screen.blit(
            bullet_img,
            (bullet_x, bullet_y)
        )

    # Draw player
    screen.blit(
        player_img,
        (player_x, player_y)
    )

    # Draw score
    draw_score(
        screen,
        score
    )

    # Draw Game Over
    if game_over:

        draw_game_over(
            screen
        )

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
