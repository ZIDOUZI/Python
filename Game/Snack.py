import random

import pygame


class Snake:
    def __init__(self, row: int, column: int, x: int, y: int, length=3, border=3, dire=(0, 1), width=500, height=500):
        self.row = row
        self.column = column
        self.width = width // column
        self.height = height // row
        self.screen = pygame.display.set_mode((width, height))
        self.state = "playing"
        self.border = border

        self.dire = dire
        self.body = [(x, y)]
        for i in range(length - 1):
            self.body.append((x - self.dire[0] * (i + 1), y - self.dire[1] * (i + 1)))
        self.food: tuple[int, int] = (random.randint(0, self.column - 1), random.randint(0, self.row - 1))

    def move(self):
        assert self.dire[0] ** 2 + self.dire[1] ** 2 == 1
        if not 0 <= self.body[0][0] + self.dire[0] < self.column or not 0 <= self.body[0][1] + self.dire[1] < self.row:
            self.state = "game over"
        else:
            self.body.insert(0, (self.body[0][0] + self.dire[0], self.body[0][1] + self.dire[1]))
            if self.body[0] in self.body[1:]:
                self.state = "game over"
            if self.body[0] == self.food:
                self.spawn_food()
            else:
                self.body.pop()

    def draw(self, screen):
        for i in range(self.column):
            for j in range(self.row):
                pygame.draw.rect(screen, (0, 0, 0), self.get_rect(i, j))
        pygame.draw.ellipse(screen, 0xFFFFFF, self.get_rect(*self.food))
        if self.state == "playing":
            col = 0xFFFFFF
        elif self.state == "game over":
            col = 0xFF0000
        else:
            col = 0x00FF00
        for i in self.body:
            pygame.draw.rect(screen, col, self.get_rect(*i))

    def get_rect(self, x, y):
        assert 0 <= x < self.column and 0 <= y < self.row
        return pygame.Rect(x * self.width + self.border, y * self.height + self.border, self.width - self.border * 2,
                           self.height - self.border * 2)

    def spawn_food(self):
        self.food = (random.randint(0, self.column - 1), random.randint(0, self.row - 1))
        while self.food in self.body:
            self.food = (random.randint(0, self.column - 1), random.randint(0, self.row - 1))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("snake")

    surface = pygame.display.set_mode((500, 400))
    clock = pygame.time.Clock()
    snake = Snake(20, 24, 10, 10, width=480, height=400)

    run = True
    time = 0

    while run:
        time = (time + 1) % 10
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    if snake.state == "playing":
                        snake.state = "paused"
                    elif snake.state == "paused":
                        snake.state = "playing"
                if event.key == pygame.K_UP:
                    snake.dire = (0, -1)
                if event.key == pygame.K_DOWN:
                    snake.dire = (0, 1)
                if event.key == pygame.K_LEFT:
                    snake.dire = (-1, 0)
                if event.key == pygame.K_RIGHT:
                    snake.dire = (1, 0)
        if time == 0 and snake.state == "playing":
            snake.move()
            surface.fill((0, 0, 0))
            snake.draw(surface)
            pygame.display.flip()
