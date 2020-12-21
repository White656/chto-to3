import pygame

color = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]


def draw():
    w, n = map(int, input().split())
    size = w
    w += n * w
    z = 0
    while n > z:
        pygame.draw.circle(screen, color[z % 3], (w, w), w - z * size)
        z = z + 1

    pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    try:

        screen = pygame.display.set_mode((250, 250))
        pygame.display.set_caption('Мишень')
        draw()
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
    except ValueError as er:
        print('Неправильный формат ввода')
    pygame.quit()
