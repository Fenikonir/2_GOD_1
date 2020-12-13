import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.use = True
        self.krest = True

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        if self.use:
            self.screen = screen
            for i in range(self.width):
                for j in range(self.height):
                    kv = pygame.Rect(self.left + self.cell_size * i, self.top + self.cell_size * j, self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, (255, 255, 255), kv, width=1)
                    self.board[j][i] = [self.left + self.cell_size * i, self.top + self.cell_size * j, 0]
            self.use = False


    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j][0] < mouse_pos[0] < self.board[i][j][0] + self.cell_size and self.board[i][j][1] < mouse_pos[1] < self.board[i][j][1] + self.cell_size:
                    return self.board[i][j]
        return None

    def on_click(self, cell_coords, krest):
        if cell_coords != None:
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j] == cell_coords and self.board[i][j][2] != 1:
                        if krest:
                            color = (0, 0, 255)
                            self.board[i][j][2] = 1
                            x0 = cell_coords[0] + 2
                            y0 = cell_coords[1] + 2
                            x1 = cell_coords[0] + self.cell_size - 2
                            y1 = cell_coords[1] + self.cell_size - 2
                            pygame.draw.line(screen, color, (x0, y0), (x1, y1), width=1)
                            pygame.draw.line(screen, color, (x1, y0), (x0, y1), width=1)
                            self.krest = False
                            break
                        else:
                            color = (255, 0, 0)
                            self.board[i][j][2] = 1
                            x = int(cell_coords[0] + self.cell_size / 2)
                            y = int(cell_coords[1] + self.cell_size / 2)
                            a = self.cell_size / 2 - 2
                            pygame.draw.circle(screen, color, (x, y), a, 1)
                            self.krest = True

            pygame.display.flip()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if self.krest:
            self.on_click(cell, self.krest)
        else:
            self.on_click(cell, self.krest)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Инициализация игры")
    board = Board(5, 7)
    board.render(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        board.render(screen)
        pygame.display.flip()
