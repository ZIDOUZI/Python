import random
import pygame
from pygame.freetype import Font


class MineSweeper:
    # 初始化
    def __init__(self, row=10, column=10, mines=10, width=800, height=600):
        self.row = row
        self.column = column
        self.height = height
        self.width = width
        self.mines = mines
        self.flagged = 0
        self.revealed = 0
        self.board = [[Cell(i, j, width // row, height // column) for j in range(self.row)] for i in range(self.column)]
        self.generate_mines()
        self.state = "playing"
        self.time = 0.0

    # 生成地雷
    def generate_mines(self):
        for i in range(self.mines):
            while True:
                x = random.randint(0, self.row - 1)
                y = random.randint(0, self.column - 1)
                if not self.board[x][y].is_mine:
                    self.board[x][y].is_mine = True
                    break

    # 标记一个格子
    def flag(self, x, y):
        if self.board[x][y].flag():
            self.flagged += 1

    # 翻开一个格子
    def reveal(self, x, y):
        if self.board[x][y].reveal():
            self.state = "lost"
        if self.get_mine_count(x, y) == 0:
            for (i, j) in self.around(x, y):
                if not self.board[i][j].is_revealed:
                    self.reveal(i, j)
        self.revealed += 1

    def clean(self, x, y):
        cells = list(map(lambda arg: self.board[arg[0]][arg[1]], self.around(x, y)))
        if self.get_mine_count(x, y) == sum(1 for cell in cells if cell.is_flagged):
            for cell in cells:
                if not cell.is_revealed and not cell.is_mine:
                    self.reveal(cell.x, cell.y)
        if self.get_mine_count(x, y) == sum(1 for cell in cells if not cell.is_revealed):
            for cell in cells:
                if not cell.is_flagged:
                    self.flag(cell.x, cell.y)

    # 获取指定坐标周围八格坐标
    def around(self, x: int, y: int):
        count = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.row and 0 <= y + j < self.column:
                    count.append((x + i, y + j))
        return count

    # 获取指定坐标周围的地雷数
    def get_mine_count(self, x, y):
        return sum(1 for (i, j) in self.around(x, y) if self.board[i][j].is_mine)

    # 绘制
    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.column):
                self.board[i][j].draw(screen)
                if self.board[i][j].is_revealed and not self.board[i][j].is_mine and self.get_mine_count(i, j) > 0:
                    self.board[i][j].draw_text(screen, f2, self.get_mine_count(i, j))

    # 循环
    def cycle(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j].is_mine and self.board[i][j].is_revealed:
                    self.state = "lost"
                if self.flagged == self.mines or self.revealed == self.row * self.column - self.mines:
                    self.state = "win"
        if self.state == "playing" and (self.flagged != 0 or self.revealed != 0):
            self.time += 0.1

    # 绘制文本
    def draw_text(self, screen, text, color=0x000000FF):
        f1.render_to(screen, (self.width // 2, self.height // 2), str(text), fgcolor=color)


class Cell:
    # 初始化
    def __init__(self, x, y, height=10, width=10, border=2):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.border = border
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False

    # 绘制
    def draw(self, screen):
        if self.is_flagged:
            pygame.draw.rect(screen, (0, 0, 255), self.rect())
        elif self.is_revealed and self.is_mine:
            pygame.draw.rect(screen, (255, 0, 0), self.rect())
        elif self.is_revealed:
            pygame.draw.rect(screen, (0, 255, 0), self.rect())
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect())

    # 获取矩形
    def rect(self):
        return pygame.Rect(self.x * self.width, self.y * self.height, self.width - self.border,
                           self.height - self.border)

    # 翻开格子
    def reveal(self):
        if not self.is_flagged:
            self.is_revealed = True
        return self.is_mine

    # 标记格子
    def flag(self):
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged
        return self.is_mine

    # 在格子中绘制文本
    def draw_text(self, screen, font, text, color=0x000000FF):
        font.render_to(screen, (self.x * self.width + self.width // 2, self.y * self.height + self.height // 2),
                       str(text), fgcolor=color)


if __name__ == '__main__':
    pygame.init()

    f1 = Font("C:\\Windows\\Fonts\\msyh.ttc", 30)
    f2 = Font("C:\\Windows\\Fonts\\msyh.ttc", 20)

    pygame.display.set_caption('MineSweeper')

    (w, h, r, c) = (500, 500, 10, 10)
    surface = pygame.display.set_mode((500, 700))
    mw = MineSweeper(r, c, 10, w, h)

    done = False

    while not done:
        pygame.time.delay(100)
        surface.fill(0x000000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mw.state == "playing":
                    if event.button == 1:
                        x0, y0 = event.pos
                        x0 = x0 * r // w
                        y0 = y0 * r // h
                        mw.reveal(x0, y0)
                    elif event.button == 2:
                        x0, y0 = event.pos
                        x0 = x0 * r // w
                        y0 = y0 * r // h
                        mw.clean(x0, y0)
                    elif event.button == 3:
                        x0, y0 = event.pos
                        x0 = x0 * r // w
                        y0 = y0 * r // h
                        mw.flag(x0, y0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    mw = MineSweeper(r, c, 10, w, h)
                    mw.state = "playing"
        mw.draw(surface)
        mw.cycle()
        if mw.state == "lost":
            for m in range(r):
                for n in range(c):
                    if mw.board[m][n].is_mine:
                        mw.board[m][n].draw(surface)
            mw.draw_text(surface, "失败!")
        elif mw.state == "win":
            mw.draw_text(surface, "胜利!")
        f1.render_to(surface, (250, 550), "{}/{}".format(mw.flagged, mw.mines), fgcolor=0xFF0000FF)
        f1.render_to(surface, (250, 580), "{:.0f}".format(mw.time), fgcolor=0x00FF00FF)
        pygame.display.flip()
