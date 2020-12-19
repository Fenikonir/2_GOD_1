import pygame

if __name__ == '__main__':
    try:
        type = int(input("Если уровнение линейное, напишите 1, если квадратное, напишите 2: "))
    except ValueError:
        print("Неправильный формат ввода")
    if type == 1:
        k, b = int(input("Введите k: ")), int(input("Введите b: "))
        if k != 1:
            text = f'y = {k}x'
        else:
            text = f'y = x'
        if b != 0:
            text += f" + {b}"
    else:
        a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))
        if a != 1:
            text = f'y = {a}x^2'
        else:
            text = f'y = x^2'
        if b != 0:
            if b != 1:
                text += f" + {b}x"
            else:
                text += f" + x"
        if c != 0:
            text += f" + {c}"
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("График")
    pygame.draw.line(screen, (255, 255, 0), (0 + 10, height // 2), (width - 10, height // 2), width=1)
    pygame.draw.line(screen, (255, 255, 0), (width // 2, 0 + 10), (width // 2, height - 10), width=1)
    x = 30
    y = 30
    for i in range(1, 56):
        pygame.draw.line(screen, (255, 255, 0), (298, y + i * 20), (302, y + i * 20), width=1)
        pygame.draw.line(screen, (255, 255, 0), (x + i * 20, 298), (x + i * 20, 302), width=1)

    pygame.draw.polygon(screen, (255, 255, 0),
                        [[300, 10], [295, 15],
                         [305, 15]])
    pygame.draw.polygon(screen, (255, 255, 0),
                        [[590, 300], [585, 295],
                         [585, 305]])
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('y', True,
                      (255, 255, 0))
    text2 = f1.render('x', True,
                      (255, 255, 0))

    text3 = f1.render(text, True,
                    (255, 255, 0))
    screen.blit(text1, (310, 10))
    screen.blit(text2, (580, 310))
    screen.blit(text3, (10, 10))

    running = True
    if type == 1:
        x = 0
        nachalo_levo = (300, 300 - b * 10)
        nachalo_pravo = (300, 300 - b * 10)
        while x != 30:
            x_levo = nachalo_levo[0] - x * 10
            x_pravo = nachalo_levo[0] + x * 10
            y_levo = nachalo_levo[1] + k * x * 10
            y_pravo = nachalo_levo[1] - k * x * 10
            pygame.draw.line(screen, (255, 255, 255), nachalo_levo, (x_levo, y_levo), width=1)
            pygame.draw.line(screen, (255, 255, 255), nachalo_pravo, (x_pravo, y_pravo), width=1)
            x += 1
    else:
        x = 0
        nachalo_levo = (300, 300 - c * 10)
        nachalo_pravo = (300, 300 - c * 10)
        perv_touch = True
        while x != 30:
            x_levo = nachalo_levo[0] - x * 10
            x_pravo = nachalo_levo[0] + x * 10
            y_levo = nachalo_levo[1] - a * x ** 2 - b * x
            y_pravo = nachalo_pravo[1] - a * x ** 2 - b * x
            if perv_touch:
                kord_pred_levo = nachalo_levo
                kord_pred_pravo = nachalo_pravo
                perv_touch = False
            pygame.draw.line(screen, (255, 255, 255), kord_pred_levo, (x_levo, y_levo), width=1)
            pygame.draw.line(screen, (255, 255, 255), kord_pred_pravo, (x_pravo, y_pravo), width=1)
            kord_pred_levo = (x_levo, y_levo)
            kord_pred_pravo = (x_pravo, y_pravo)


            x += 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

