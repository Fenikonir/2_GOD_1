import os, sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

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

def drawing(mouse_pos):

    screen.blit(image, mouse_pos)

running = True
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
            screen.fill((0, 0, 0))
            image = load_image("arrow.png")
            drawing(event.pos)

    # отрисовка и изменение свойств объектов
    # ...

    # обновление экрана
    pygame.display.flip()
pygame.quit()