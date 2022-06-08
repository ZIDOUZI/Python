import math
import pygame
import random
from pygame.freetype import Font


class Game2048:
    def __init__(self, row=4, column=4, width=500, height=500, border=3):
        self.row = row
        self.column = column
        self.width = width // column
        self.height = height // row
        self.border = border
        self.board = [[Cell(i, j, self.width, self.height, 0) for j in range(column)] for i in range(row)]
        self.max = 2
        self.score = 0
        self.state = "playing"
        self.spawn()

    # 检查是否有相邻的相同数字
    def check(self):
        for i in range(self.row - 1):
            for j in range(self.column):
                if self.board[i][j].value == self.board[i + 1][j].value:
                    return False
        for j in range(self.column - 1):
            for i in range(self.row):
                if self.board[i][j].value == self.board[i][j + 1].value:
                    return False
        return True

    def spawn(self):
        all_cell = [cell for row in self.board for cell in row]
        l = list(filter(lambda cell: cell.value == 0, all_cell))
        if len(l) == 0 and self.check():
            self.state = "lost"
            return
        random.choice(l).set_value(random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))
        self.max = max(self.max, *map(lambda cell: cell.value, list(filter(lambda cell: cell.value != 0, all_cell))))
        if self.max == 2048:
            self.state = "win"

    def up(self):
        changed = False
        for i in range(self.row):
            result = merge(self.board[i])
            self.score += result[0]
            if result[1]:
                changed = True
        if changed:
            self.spawn()

    def down(self):
        changed = False
        for i in range(self.row):
            result = merge(self.board[i][::-1])
            self.score += result[0]
            if result[1]:
                changed = True
        if changed:
            self.spawn()

    def left(self):
        changed = False
        for j in range(self.column):
            column = [self.board[i][j] for i in range(self.row)]
            result = merge(column)
            self.score += result[0]
            if result[1]:
                changed = True
        if changed:
            self.spawn()

    def right(self):
        changed = False
        for j in range(self.column):
            column = [self.board[i][j] for i in range(self.row)]
            result = merge(column[::-1])
            self.score += result[0]
            if result[1]:
                changed = True
        if changed:
            self.spawn()

    def draw(self, screen):
        for row in self.board:
            for cell in row:
                cell.draw(screen, self.border)

    def draw_text(self, screen, text, color=0x000000):
        f1.render_to(screen, (self.width // 2, self.height // 2), str(text), fgcolor=color)


class Cell:

    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value: int = value

    def set_value(self, value):
        self.value = value

    def draw(self, screen, border=10):
        pygame.draw.rect(screen, int(math.log2(max(2, 2 * self.value))) * 0x945D100 - 0x1,
                         (self.x * self.width + border, self.y * self.height + border, self.width - border * 2,
                          self.height - border * 2))
        if self.value != 0:
            self.draw_text(screen, self.value)

    def draw_text(self, screen, text, color=0x000000FF):
        f1.render_to(screen, (self.x * self.width + self.height // 8, self.y * self.height + self.height // 3),
                     str(text), fgcolor=color)


def merge(l: list[Cell]):
    i = 0
    sum_ = 0
    changed = False
    while i < len(l) - 1:
        if l[i].value == l[i + 1].value != 0:
            l[i].value *= 2
            sum_ += l[i + 1].value
            l[i + 1].value = 0
            changed = True
            i -= 1
        elif l[i].value == l[i + 1].value == 0:
            i += 1
        elif l[i].value == 0:
            l[i].value, l[i + 1].value = l[i + 1].value, 0
            i -= 1
            changed = True
        elif l[i + 1].value == 0:
            i += 1
        elif l[i].value != l[i + 1].value:
            i += 1
        else:
            raise Exception("Something went wrong")
        if i == -1:
            i = 0
    return sum_, changed


if __name__ == '__main__':

    pygame.init()
    pygame.display.set_caption("2048")

    (w, h, r, c) = (500, 500, 4, 4)

    surface = pygame.display.set_mode((500, 600))
    f1 = Font("C:\\Windows\\Fonts\\msyh.ttc", 50)
    g = Game2048(r, c, w, h)
    done = False

    while not done:
        pygame.time.delay(100)
        surface.fill(0x000000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    g = Game2048(w, h, r, c)
                elif event.key == pygame.K_UP:
                    g.up()
                elif event.key == pygame.K_DOWN:
                    g.down()
                elif event.key == pygame.K_LEFT:
                    g.left()
                elif event.key == pygame.K_RIGHT:
                    g.right()
        g.draw(surface)
        f1.render_to(surface, (200, 530), "{}".format(g.score), fgcolor=0xFFFFFFFF)
        if g.state == "lost":
            g.draw_text(surface, "Game Over", color=0xFF0000FF)
        if g.state == "win":
            g.draw_text(surface, "You Win", color=0xFF0000FF)
        pygame.display.flip()
