import os, sys
import pygame

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
   # прозрачный цвет
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


running = True
image = load_image("gameover.png")
koord = [-600, 0]
screen.blit(image, koord)
v = 200  # пикселей в секунду
x0 = 0
fps = 60
clock = pygame.time.Clock()
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if x0 <= 600:
            koord[0] += v / fps # v * t в секундах
            x0 +=  v / fps
        screen.fill((0, 0, 255))
        clock.tick(fps)
        screen.blit(image, koord)
        pygame.display.flip()
pygame.quit()