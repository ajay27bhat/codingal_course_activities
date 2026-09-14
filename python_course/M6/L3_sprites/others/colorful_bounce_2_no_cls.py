"""
Activity: Bouncing Color-Changing Sprite

Instructions:
1. Import Pygame and random.
2. Create a 500 x 400 game window.
3. Create a small rectangle sprite.
4. Give the sprite a starting position and movement speed.
5. Move the sprite automatically.
6. Reverse its direction when it touches a window edge.
7. Change the sprite and background colors when it hits an edge.
8. Keep the game running until the user closes the window.
"""

import pygame
import random

# Initialize Pygame and create the window
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Bouncing Sprite")

# Create the sprite
x = 100
y = 100
width = 30
height = 20

speed_x = 2
speed_y = 2

sprite_color = "white"
background_color = "blue"

# Store possible colors in lists
sprite_colors = ["yellow", "magenta", "orange", "white"]
background_colors = ["blue", "lightblue", "darkblue"]

clock = pygame.time.Clock()

# Keep the game running until the window is closed
running = True

while running:

    # Check for events such as closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite
    x += speed_x
    y += speed_y

    # Check if the sprite touches the left or right edge
    if x <= 0 or x + width >= 500:
        speed_x = -speed_x
        sprite_color = random.choice(sprite_colors)
        background_color = random.choice(background_colors)

    # Check if the sprite touches the top or bottom edge
    if y <= 0 or y + height >= 400:
        speed_y = -speed_y
        sprite_color = random.choice(sprite_colors)
        background_color = random.choice(background_colors)

    # Draw the background and sprite
    screen.fill(background_color)
    pygame.draw.rect(
        screen,
        sprite_color,
        (x, y, width, height)
    )

    # Update the display
    pygame.display.flip()

    # Control the movement speed
    clock.tick(60)

# Close Pygame
pygame.quit()