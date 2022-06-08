import math
import random
import pygame
from pygame.freetype import Font


def get_color(value):
    return value // 4 % 2 * 255, value // 2 % 2 * 255, value % 2 * 255


class Tetris(object):
    def __init__(self, row: int, column: int, height: int, width: int, border=3):
        self.row = row + 4
        self.column = column
        self.height = height
        self.width = width
        self.state = 0
        self.border = border
        self.shape = random.choice(self.shape_list)
        self.color = random.randint(1, 7)
        self.center = [self.column // 2, 2]
        self.board = [[0 for _ in range(self.row)] for _ in range(self.column)]
        self.score = 0

    shape_list = [
        [(-1, -1), (0, -1), (0, 0), (1, 0)], # z
        [(1, -1), (0, -1), (0, 0), (-1, 0)], # s
        [(-1, 0), (0, 0), (0, 1), (0, 2)], # j
        [(1, 0), (0, 0), (0, 1), (0, 2)], # l
        [(0, -1), (0, 0), (0, 1), (0, 2)], # ----
        [(0, 0), (0, 1), (1, 0), (1, 1)], # o
        [(0, 0), (0, 1), (0, -1), (1, 0)], # t
    ]

    def get_rect(self, x, y):
        return pygame.Rect(x * self.width + self.border, y * self.height + self.border, self.width - self.border * 2,
                           self.height - self.border * 2)

    def spawn(self):
        self.shape = random.choice(self.shape_list)
        self.color = random.randint(1, 7)
        self.center = [self.column // 2, 2]

    def draw(self, screen):
        for x in range(self.column):
            for y in range(4, self.row):
                pygame.draw.rect(screen, get_color(self.board[x][y]), self.get_rect(x, y))
        for (x, y) in self.shape:
            pygame.draw.rect(screen, get_color(self.color), self.get_rect(self.center[0] + x, self.center[1] + y))

    def draw_text(self, screen, text, color=0x000000FF):
        f1.render_to(screen, (self.width // 2, self.height // 2), str(text), fgcolor=color)

    def check_border(self):
        v = 0b000
        for (x, y) in self.shape:
            if self.center[0] + x < 0:
                v |= 0b100
            if self.center[0] + x >= self.column:
                v |= 0b010
            if self.center[1] + y >= self.row:
                v |= 0b001
        return v

    def check_collision(self):
        v = self.check_border()
        for (x, y) in self.shape:
            if v & 0b100 == 0 and self.board[self.center[0] + x][self.center[1] + y] != 0:
                v |= 0b100
            if v & 0b010 == 0 and self.board[self.center[0] + x][self.center[1] + y] != 0:
                v |= 0b010
            if v & 0b001 == 0 and self.board[self.center[0] + x][self.center[1] + y] != 0:
                v |= 0b001
        return v

    def move(self, x, y):
        self.center[0] += x
        self.center[1] += y
        if self.check_border() != 0 or self.check_collision() != 0:
            self.center[0] -= x
            self.center[1] -= y
            return False
        return True

    def down(self):
        while self.move(0, 1):
            pass

    def flip(self):
        self.shape = [(y, -x) for (x, y) in self.shape]
        if not self.check_collision() != 0:
            return True
        if self.check_border() & 0b100 == 0:
            if self.move(1, 0):
                return True
        elif self.check_border() & 0b010 == 0:
            if self.move(-1, 0):
                return True
        elif self.check_border() & 0b001 == 0:
            if self.move(0, 1):
                return True
        self.shape = [(-y, x) for (x, y) in self.shape]
        return False

    def freeze(self):
        (x0, y0) = self.center
        for (x, y) in self.shape:
            self.board[x0 + x][y0 + y] = self.color

    def check_row(self):
        y = 0
        while y < self.row:
            for x in range(self.column):
                if self.board[x][y] == 0:
                    break
            else:
                self.score += 1
                for y0 in range(1, y + 1)[::-1]:
                    for x in range(self.column):
                        self.board[x][y0] = self.board[x][y0 - 1]
                continue
            y += 1
        return False

    def check_state(self):
        for j in range(self.column):
            if self.board[j][4] != 0:
                self.state |= 0b10

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Tetris')
    tetris = Tetris(20, 10, 20, 20)
    f1 = Font("C:\\Windows\\Fonts\\msyh.ttc", 30)

    run = True
    time = 0

    while run:
        pygame.time.delay(12)
        time = (time + 1) % (45 - int(math.log2(tetris.score + 1)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    tetris.state ^= 0b1
                if event.key == pygame.K_r:
                    tetris.board = [[0 for _ in range(tetris.row)] for _ in range(tetris.column)]
                    tetris.score = 0
                    tetris.spawn()
                    tetris.state = 0
                if event.key == pygame.K_LEFT:
                    tetris.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    tetris.move(1, 0)
                if event.key == pygame.K_DOWN:
                    tetris.down()
                if event.key == pygame.K_UP:
                    tetris.flip()
        if time == 0 and tetris.state == 0:
            if not tetris.move(0, 1):
                tetris.freeze()
                tetris.check_state()
                tetris.spawn()
                tetris.check_row()
        surface.fill(0xA0A0A0)
        tetris.draw(surface)
        f1.render_to(surface, (500, 300), str(tetris.score), fgcolor=0x000000FF)
        if tetris.state & 0b10 != 0:
            tetris.draw_text(surface, "failed!")
        pygame.display.flip()
