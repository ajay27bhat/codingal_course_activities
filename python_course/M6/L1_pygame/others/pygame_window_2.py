"""
Activity: Create a Pygame Window

Instructions:
1. Import and initialize Pygame.
2. Create a game window with a width of 400 and height of 500.
3. Create a game loop to keep the window open.
4. Check for events inside the loop.
5. Close the game when the user clicks the close button.
6. Update the display inside the loop.
"""

import pygame

# Initialize Pygame and create the window
pygame.init()
screen = pygame.display.set_mode((400, 500))

# Keep the game running until the window is closed
running = True

while running:

    # Check for events such as closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Close Pygame
pygame.quit()