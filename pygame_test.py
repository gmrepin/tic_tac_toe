import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Пример графического окна Pygame')
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(screen, (60, 0, 128), (0, 0), (400, 300), 10)

    pygame.draw.line(screen, (60, 0, 128), (800, 0), (500, 300), 10)

    pygame.draw.line(screen, (60, 0, 128), (0, 600), (400, 400), 10)

    pygame.draw.line(screen, (60, 0, 128), (800, 600), (500, 400), 10)

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 300, 100, 100), 10)

    pygame.display.update()


pygame.quit()
