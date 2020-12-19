import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Перетаскивание")
    kv = pygame.Rect(0, 0, 100, 100)
    pygame.draw.rect(screen, (0, 255, 0), kv, width=0)
    pos = (0, 0)
    running = True
    drawing = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = event.pos
                if pos[0] < pos_mouse[0] < pos[0] + 100 and pos[1] < pos_mouse[1] < pos[1] + 100:
                    drawing = True

            if event.type == pygame.MOUSEMOTION and drawing:
                kv[0] += event.rel[0]
                kv[1] += event.rel[1]
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                pos = (kv[0], kv[1])
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (0, 255, 0), kv, width=0)
        pygame.display.flip()