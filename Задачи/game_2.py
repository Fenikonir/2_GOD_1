import os
import random
import sys

import pygame

pygame.init()
size = width, height = 789, 500
screen = pygame.display.set_mode(size)


def terminate():
    print(x)
    pygame.quit()
    sys.exit()


def start_screen():
    screen = pygame.display.set_mode((710, 500))
    fon = pygame.transform.scale(load_image('Fone.png'), (710, 500))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                if 160 <= event.pos[0] <= 160 + 420 and 125 <= event.pos[1] <= 125 + 66:
                    return 1, 2000
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 66 + 25 <= event.pos[1] <= 125 + 66 + 25 + 66:
                    return 3, 1500
                elif 160 <= event.pos[0] <= 160 + 420 and 125 + 2 * 66 + 25 * 2 <= event.pos[
                    1] <= 125 + 3 * 66 + 2 * 25:
                    return 5, 1000
        pygame.display.flip()
        clock.tick(FPS)


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


def lose_screen():
    screen = pygame.display.set_mode((300, 300))
    intro_text = ["Вы проиграли", f"Набрано {x} очков"]

    fon = pygame.Surface((300, 300))
    fon.fill((200, 200, 200))

    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(mobs)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(0, 1)

    def update(self):
        # если ещё в небе
        if not pygame.sprite.spritecollideany(self, horizontal_borders):
            self.rect = self.rect.move(0, mob_speed)
        else:
            lose_screen()


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class GunCar(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x=width // 2, y=height - 5 - 44, weigh=32, heigh=44):
        super().__init__(gun_car)
        self.image = pygame.transform.scale(load_image("cannon.png"), (weigh, heigh))
        # self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        # pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = self.image.get_rect().move(x, y)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(load_image("bullet.png"), (15, 30))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


screen = pygame.display.set_mode(size)
gun_car = pygame.sprite.Group()
gun = GunCar()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Border(0, height - 6, width, height - 6)
bom = pygame.mixer.Sound('Pop_up.wav')
mountain = Mountain()
x = 0
FPS = 100
STEP = 30
MYEVENTTYPE = pygame.USEREVENT + 1

pygame.key.set_repeat(200, 70)
clock = pygame.time.Clock()
mob_speed, takt = start_screen()
pygame.time.set_timer(MYEVENTTYPE, takt)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            Landing((random.randrange(width - 100), 0))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if gun.rect.x <= width + STEP:
                    gun.rect.x += STEP
                else:
                    gun.rect.x = 0
            if event.key == pygame.K_LEFT:
                if gun.rect.x >= 0 - STEP:
                    gun.rect.x -= STEP
                else:
                    gun.rect.x = width - STEP
            if event.key == pygame.K_SPACE:
                gun.shoot()
                bom.play()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if hits:
        x += 10

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    gun_car.draw(screen)
    mobs.draw(screen)
    mobs.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
