import pygame

# Define some colors.
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")

# лев стик
# Axis 0 - лево/право (-1;1)
# Axis 1 - верх/низ (-1;1)
# прав стик
# Axis 3 - лево/право (-1;1)
# Axis 4 - верх/низ (-1;1)
# тиггеры
# Axis 2 - лев тиггер
# Axis 5 - прав тиггер


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("My Game")

done = False


clock = pygame.time.Clock()

pygame.joystick.init()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            0

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()
    print(joystick_count)

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
