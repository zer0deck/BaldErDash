import pygame

WHITE = pygame.Color("white")
pygame.init()
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
    screen.fill(WHITE)
    joystick_count = pygame.joystick.get_count()
    print(joystick_count)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
