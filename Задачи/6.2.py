import pygame


def draw(screen, x):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render(f"{x}", True, (255, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 200, 200
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    run = True
    video_expose = 1
    draw(screen, video_expose)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEOEXPOSE:
                draw(screen, video_expose)
                video_expose += 1
        pygame.display.flip()

    # завершение работы:
    pygame.quit()
