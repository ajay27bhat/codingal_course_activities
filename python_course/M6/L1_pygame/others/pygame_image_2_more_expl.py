# Import the Pygame library so we can create a game window,
# display images, and add text.
import pygame


# Initialize all the Pygame modules.
# This must be done before using most Pygame features.
pygame.init()


# Create a game window that is 500 pixels wide
# and 500 pixels tall.
screen = pygame.display.set_mode((500, 500))


# Set the title that will appear at the top of the game window.
pygame.display.set_caption("My Pygame Window")


# -------------------------------
# Load and resize the background
# -------------------------------

# Load the background image from the specified file path.
background = pygame.image.load(
    "python_course/M6/L1_pygame/background.jpg"
)

# Resize the background image so that it fills
# the entire 500 x 500 game window.
background = pygame.transform.scale(background, (500, 500))


# -------------------------------
# Load and resize the penguin
# -------------------------------

# Load the penguin image from the specified file path.
penguin = pygame.image.load(
    "python_course/M6/L1_pygame/penguin.png"
)

# Resize the penguin image to 200 x 200 pixels.
penguin = pygame.transform.scale(penguin, (200, 200))


# -------------------------------
# Create the "Hello World" text
# -------------------------------

# Create a font object.
# "None" uses Pygame's default font, and 36 is the font size.
font = pygame.font.Font(None, 36)

# Create an image containing the words "Hello World".
# True makes the text edges smoother.
# "black" sets the text color to black.
text = font.render("Hello World", True, "black")


# -------------------------------
# Start the game loop
# -------------------------------

# This variable controls whether the game keeps running.
# As long as running is True, the game loop will continue.
running = True


# Keep repeating the game loop until the user closes the window.
while running:

    # Check for events that happen in the game window,
    # such as mouse clicks, keyboard presses, or closing the window.
    for event in pygame.event.get():

        # Check if the user clicked the window's close button.
        if event.type == pygame.QUIT:

            # Change running to False to stop the game loop.
            running = False


    # -------------------------------
    # Draw everything on the screen
    # -------------------------------

    # Draw the background image.
    # (0, 0) means the image starts at the top-left corner.
    screen.blit(background, (0, 0))

    # Draw the penguin image.
    # (150, 100) is the position of the penguin.
    screen.blit(penguin, (150, 100))

    # Draw the "Hello World" text.
    # (170, 350) is the position of the text.
    screen.blit(text, (170, 350))


    # -------------------------------
    # Update the display
    # -------------------------------

    # Update the game window so that all the drawings
    # we made above become visible.
    pygame.display.flip()


# When the game loop ends, close and clean up Pygame.
pygame.quit()