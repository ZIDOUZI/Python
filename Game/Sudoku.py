import pygame
from pygame.freetype import Font


class Sudoku:
    def __init__(self, height, width, border=2):
        self.height = height
        self.width = width
        self.border = border
        self.selected = [0, 0]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.spawn()

    def spawn(self):
        self.board = [
            [2, 0, 0, 0, 8, 4, 5, 0, 0],
            [3, 0, 1, 0, 6, 0, 0, 4, 0],
            [0, 0, 0, 0, 2, 0, 3, 7, 0],
            [0, 2, 8, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 4, 7, 6, 0, 0, 8],
            [0, 7, 0, 8, 0, 0, 0, 9, 3],
            [5, 0, 2, 0, 0, 0, 9, 0, 0],
            [0, 3, 0, 0, 0, 5, 4, 0, 0],
            [0, 0, 0, 7, 0, 8, 2, 6, 0],
        ]
        for i in range(9):
            for j in range(9):
                self.board[i][j] = -self.board[i][j]

    def draw(self, screen):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen, 0x888888,
                                 (self.height * i * 3 + self.border, self.width * j * 3 + self.border,
                                  self.height * 3 - self.border * 2, self.width * 3 - self.border * 2))
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(screen, 0xFFFFFF, self.get_rect(i, j))
                if self.board[i][j] != 0:
                    self.draw_text(screen, abs(self.board[i][j]), i, j)
        pygame.draw.rect(screen, 0xFF0000, self.get_rect(*self.selected), 3)

    def draw_text(self, screen, text, x, y, color=0xFF):
        f1.render_to(screen, self.get_rect(x + 0.5, y + 0.5), str(text), fgcolor=color)

    def get_rect(self, x, y):
        return pygame.Rect(self.height * x + self.border, self.width * y + self.border, self.width - self.border * 2,
                           self.height - self.border * 2)

    def choose(self, x, y):
        self.selected = [x, y]

    def set(self, value):
        if self.board[self.selected[0]][self.selected[1]] >= 0:
            self.board[self.selected[0]][self.selected[1]] = value
            return True
        return False

    def check(self, l):  # 判断表中是否有重复值，0除外
        for i in range(1, 10):
            if l.count(i) >= 2:
                return False
        return True

    def check_row(self):  # 检测横向是否有重复值，无则为返回0，有则返回1
        for i in self.board:
            return self.check(i)

    def check_column(self):  # 检测纵向是否重复值，无则为返回0，有则返回1
        for i in range(9):
            l = []
            for j in range(9):
                l.append(self.board[j][i])
            if not self.check(l):
                return False
        return True

    def check_square(self):  # 检测九宫格是否有重复值，无则为返回0，有则返回1
        for i in range(3):
            for j in range(3):
                l = []
                for k in range(3):
                    for m in range(3):
                        l.append(self.board[i * 3 + k][j * 3 + m])
                if not self.check(l):
                    return False


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((630, 630))
    f1 = Font("C:\\Windows\\Fonts\\msyh.ttc", 30)

    sudoku = Sudoku(70, 70)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sudoku.choose(pos[0] // 70, pos[1] // 70)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sudoku.set(1)
                elif event.key == pygame.K_2:
                    sudoku.set(2)
                elif event.key == pygame.K_3:
                    sudoku.set(3)
                elif event.key == pygame.K_4:
                    sudoku.set(4)
                elif event.key == pygame.K_5:
                    sudoku.set(5)
                elif event.key == pygame.K_6:
                    sudoku.set(6)
                elif event.key == pygame.K_7:
                    sudoku.set(7)
                elif event.key == pygame.K_8:
                    sudoku.set(8)
                elif event.key == pygame.K_9:
                    sudoku.set(9)
                if event.key == pygame.K_UP:
                    sudoku.selected[1] -= 1
                    if sudoku.selected[1] < 0:
                        sudoku.selected[1] = 8
                if event.key == pygame.K_DOWN:
                    sudoku.selected[1] += 1
                    if sudoku.selected[1] > 8:
                        sudoku.selected[1] = 0
                if event.key == pygame.K_LEFT:
                    sudoku.selected[0] -= 1
                    if sudoku.selected[0] < 0:
                        sudoku.selected[0] = 8
                if event.key == pygame.K_RIGHT:
                    sudoku.selected[0] += 1
                    if sudoku.selected[0] > 8:
                        sudoku.selected[0] = 0
        surface.fill(0x000000)
        sudoku.draw(surface)
        if sudoku.check_row() and sudoku.check_column() and sudoku.check_square():
            f1.render_to(surface, (0, 0), "Success!", fgcolor=0x000000FF)
        pygame.display.update()
