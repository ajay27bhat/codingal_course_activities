"""
Activity: Add an Image, Background, and Text Using Pygame

Instructions:
1. Import and initialize Pygame.
2. Create a 500 x 500 game window.
3. Set a title for the window.
4. Load a background image and resize it to fit the window.
5. Load a penguin image and resize it.
6. Display "Hello World" on the screen.
7. Use a game loop to keep the window open.
8. Close the game when the user clicks the close button.
"""

import pygame

# Initialize Pygame and create the game window
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Pygame Window")

# Load and resize the background image
background = pygame.image.load(
    "python_course/M6/L1_pygame/background.jpg"
)
background = pygame.transform.scale(background, (500, 500))

# Load and resize the penguin image
penguin = pygame.image.load(
    "python_course/M6/L1_pygame/penguin.png"
)
penguin = pygame.transform.scale(penguin, (200, 200))

# Create the text to display
font = pygame.font.Font(None, 36)
text = font.render("Hello World", True, "black")

# Keep the game running until the window is closed
running = True

while running:

    # Check for events such as closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the background, image, and text
    screen.blit(background, (0, 0))
    screen.blit(penguin, (150, 100))
    screen.blit(text, (170, 350))

    # Update the screen
    pygame.display.flip()

pygame.quit()