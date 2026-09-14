"""
Activity: Move and Color a Sprite

Instructions:
1. Import and initialize Pygame.
2. Create a 500 x 500 game window.
3. Create a square that can move using the arrow keys.
4. Keep the square inside the window.
5. Change the square's color when it touches an edge.
6. Use a game loop to keep the program running.
7. Close the game when the user closes the window.
"""

import pygame

# Initialize Pygame and create the window
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Color Changing Sprite")

# Set the starting position and size of the square
x = 30
y = 30
size = 60

# Control the speed of the game loop
clock = pygame.time.Clock()

# Keep the game running until the window is closed
running = True

while running:

    # Check for events such as closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which arrow keys are being pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 2
    if keys[pygame.K_RIGHT]:
        x += 2
    if keys[pygame.K_UP]:
        y -= 2
    if keys[pygame.K_DOWN]:
        y += 2

    # Keep the square inside the window
    x = min(max(0, x), 500 - size)
    y = min(max(0, y), 500 - size)

    # Change the color when the square touches an edge
    color = "white"

    if x == 0:
        color = "blue"
    elif x == 500 - size:
        color = "yellow"
    elif y == 0:
        color = "red"
    elif y == 500 - size:
        color = "green"

    # Draw the square and update the display
    screen.fill("black")
    pygame.draw.rect(screen, color, (x, y, size, size))
    pygame.display.flip()

    # Limit the game loop to 60 frames per second
    clock.tick(60)

# Close Pygame
pygame.quit()