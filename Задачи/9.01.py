import pygame
import random

class Ball(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("white"), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = -1
        self.vy = -1

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if not 0 <= self.rect.x <= width - 20:
            self.vx = -self.vx

        if not 0 <= self.rect.y <= height - 20:
            self.vy = -self.vy


all_sprites = pygame.sprite.Group()


size = width, height = random.randrange(100, 800), random.randrange(100, 800)
screen = pygame.display.set_mode(size)

# for i in range(20):
#     Ball(20, 100, 100)
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 10)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Ball(10, event.pos[0], event.pos[1])
        if event.type == MYEVENTTYPE:
            all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()