"""
Activity: Sprite Collision Game

Instructions:
1. Import and initialize Pygame.
2. Create a 500 x 400 game window.
3. Load and scale a background image.
4. Create a Sprite class using pygame.sprite.Sprite.
5. Create two sprite objects and add them to a sprite group.
6. Move the first sprite using the arrow keys.
7. Keep the sprite inside the game window.
8. Check for collision using colliderect().
9. Remove the second sprite when a collision happens.
10. Display a centered "You win!" message.
11. Keep the game running until the window is closed.
"""

import pygame
import random

# Initialize Pygame and create the window
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

# Load the background image and font
background = pygame.image.load("python_course/M6/L4_adv/bg.jpg")
background = pygame.transform.scale(background, (500, 400))

font = pygame.font.SysFont("Times New Roman", 72)


# Create a Sprite class
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((30, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    # Move the sprite
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        # Keep the sprite inside the window
        self.rect.x = max(0, min(self.rect.x, 470))
        self.rect.y = max(0, min(self.rect.y, 380))


# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create two sprites
player = Sprite("black")
target = Sprite("red")

# Give the sprites random positions
player.rect.x = random.randint(0, 470)
player.rect.y = random.randint(0, 380)

target.rect.x = random.randint(0, 470)
target.rect.y = random.randint(0, 380)

# Add the sprites to the group
all_sprites.add(player, target)

clock = pygame.time.Clock()

running = True
won = False

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player until the game is won
    if not won:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.move(-5, 0)

        if keys[pygame.K_RIGHT]:
            player.move(5, 0)

        if keys[pygame.K_UP]:
            player.move(0, -5)

        if keys[pygame.K_DOWN]:
            player.move(0, 5)

        # Check for collision
        if player.rect.colliderect(target.rect):
            all_sprites.remove(target)
            won = True

    # Draw the background and sprites
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    # Display the win message
    if won:
        text = font.render("You win!", True, "black")

        x = (500 - text.get_width()) // 2
        y = (400 - text.get_height()) // 2

        screen.blit(text, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()