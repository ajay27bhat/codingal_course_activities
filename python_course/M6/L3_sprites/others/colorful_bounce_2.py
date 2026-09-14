"""
Activity: Sprite with Custom Events

Instructions:
1. Import and initialize Pygame.
2. Create a custom event for changing colors.
3. Create a Sprite class using pygame.sprite.Sprite.
4. Create the sprite's image and rectangle.
5. Move the sprite using its speed values.
6. Make the sprite bounce when it touches an edge.
7. Create a custom event when the sprite touches an edge.
8. Create a method to change the sprite's color.
9. Create a sprite group and add the sprite.
10. Handle the custom event inside the game loop.
11. Update and draw the sprite.
12. Keep the game running until the window is closed.
"""

import pygame
import random

# Initialize Pygame and create the window
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Events")

# Create a custom event
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1


# Create a Sprite class
class Sprite(pygame.sprite.Sprite):

    # Set up the sprite
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

        self.speed_x = 2
        self.speed_y = 2

    # Move the sprite
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Make the sprite bounce at the edges
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.speed_x = -self.speed_x
            pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed_y = -self.speed_y
            pygame.event.post(pygame.event.Event(COLOR_CHANGE_EVENT))

    # Change the sprite's color
    def change_color(self):
        colors = ["yellow", "magenta", "orange", "white"]
        self.image.fill(random.choice(colors))


# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create and add the sprite
sprite = Sprite()
all_sprites.add(sprite)

background_color = "blue"

clock = pygame.time.Clock()

# Keep the game running
running = True

while running:

    # Check for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Handle the custom event
        elif event.type == COLOR_CHANGE_EVENT:
            sprite.change_color()
            background_color = random.choice(
                ["blue", "lightblue", "darkblue"]
            )

    # Update and draw the sprite
    all_sprites.update()

    screen.fill(background_color)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()