import pygame as pg
import os, sys

W = 600
H = 95
WHITE = (255, 255, 255)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
   # прозрачный цвет
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Car(pg.sprite.Sprite):
    def __init__(self, x, name):
        pg.sprite.Sprite.__init__(self)
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.x = 0
        self.v = 1
        self.dvig = True

    def update(self):
        if self.dvig:
            self.rect = self.rect.move(self.v, 0)
            self.x += self.v
        else:
            self.rect = self.rect.move(-self.v, 0)
            self.x -= self.v

        if self.x == 450 or self.x == -1:
            self.dvig = not self.dvig
            self.image = pg.transform.flip(self.image, True, False)
            # self.image = load_image("boom.png")




sc = pg.display.set_mode((W, H))

car1 = Car(0, 'car2.png')
clock = pg.time.Clock()
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    sc.fill(WHITE)
    sc.blit(car1.image, car1.rect)
    pg.display.update()
    pg.time.delay(20)

    car1.update()