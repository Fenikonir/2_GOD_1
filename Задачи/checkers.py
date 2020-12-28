import os, sys
import pygame

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clik = pygame.mixer.Sound('Pop_up.wav')

class WBall(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, radius, x, y):
        super().__init__(white_chek)
        self.radius = radius
        self.image = pygame.transform.scale(load_image("white_chek.png"), (radius, radius))
        # self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        # pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, radius, radius)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            # pygame.draw.rect(screen, (100, 255, 100), self.rect.x, self.rect.y, self.radius)
            clik.play()

class BBall(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, radius, x, y):
        super().__init__(black_chek)
        self.radius = radius
        self.image = pygame.transform.scale(load_image("black_chek.png"), (radius, radius))
        # self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        # pygame.draw.circle(self.image, pygame.Color("red"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, radius, radius)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            clik.play()




class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 20
        self.top = 20
        self.cell_size = 45
        self.use = True
        self.black_on = False

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        if self.use:
            self.screen = screen
            pygame.draw.rect(screen, (255, 255, 255),
                             (self.left, self.top, self.cell_size * 8, self.cell_size * 8),
                             width=4)
            for i in range(self.width):
                for j in range(self.height):
                    if not self.black_on:
                        color = (255, 255, 255)
                    else:
                        color = (128, 128, 128)
                    kv = pygame.Rect(self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size,
                                     self.cell_size)
                    pygame.draw.rect(screen, color, kv)
                    if color == (128, 128, 128) and j <= 2:
                        BBall(self.cell_size, self.left + self.cell_size * i, self.top + self.cell_size * j)
                    elif color == (128, 128, 128) and j >= 5:
                        WBall(self.cell_size, self.left + self.cell_size * i, self.top + self.cell_size * j)
                    self.black_on = not self.black_on
                self.black_on = not self.black_on
            self.use = False


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


white_chek = pygame.sprite.Group()
black_chek = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шашки")
    pygame.mixer.music.load('Ring05.wav')
    pygame.mixer.music.play()
    board = Board(8, 8)
    board.render(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        white_chek.draw(screen)
        white_chek.update(event)
        black_chek.draw(screen)
        black_chek.update(event)
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
