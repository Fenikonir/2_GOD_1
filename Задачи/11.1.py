import os, sys
import pygame

pygame.init()
size = width, height = 500, 500
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


def drawing(koord):
    screen.fill((255, 255, 255))
    img = pygame.transform.flip(image, smotr_vpravo, False)
    screen.blit(img, koord)


pygame.mixer.music.load('Speech On.wav')

running = True
image = load_image("creature.png")
smotr_vpravo = False
koord = [0, 0]
screen.blit(image, koord)
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                koord[1] -= 10
                pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                koord[1] += 10
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                if not smotr_vpravo:
                    smotr_vpravo = True
                koord[0] -= 10
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                if smotr_vpravo:
                    smotr_vpravo = False
                pygame.mixer.music.play()
                koord[0] += 10
            drawing(koord)
    pygame.display.flip()
pygame.quit()
