import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("ANNA")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 15, 15))

    pygame.display.flip()

pygame.quit()