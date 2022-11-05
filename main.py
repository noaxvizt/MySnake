import pygame
from collections import deque
import random


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("ЗМЕЙКА")
pygame.display.set_icon(pygame.image.load("data/images/icon.png"))
flRunning = True
fps = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()


class Sector:
    def __init__(self, color, x_position, y_position, x_size, y_size):
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.x_size = x_size
        self.y_size = y_size
        self.sector = pygame.Surface((self.x_size, self.y_size))
        self.sector.fill(color)
        self.rect = self.sector.get_rect(topleft=(self.x_position, self.y_position))
        self.freeze = False
        self.x_velocity = 0
        self.y_velocity = 0

    def Draw(self, screen):
        screen.blit(self.sector, self.rect)

    def Move(self):
        self.rect.move_ip(self.x_size * self.x_velocity, self.y_size * self.y_velocity)

    def SetXVelocity(self, x_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = 0

    def SetYVelocity(self, y_velocity):
        self.y_velocity = y_velocity
        self.x_velocity = 0

    def DeepCopy(self):
        now_copy = Sector(self.color, self.x_position, self.y_position, self.x_size, self.y_size)
        now_copy.rect.x = self.rect.x
        now_copy.rect.y = self.rect.y
        now_copy.freeze = self.freeze
        return now_copy


class Snake(Sector):
    def __init__(self, color, apple):
        super().__init__(color, 20, 20, 20, 20)
        self.head = self.sector
        self.score = 0
        self.tail_queue = deque()
        self.apple = apple

    def Move(self):
        if apple.rect.colliderect(self.rect):
            self.score += 1
            self.AddSector()
            apple.Replace()
        if len(self.tail_queue) == 0:
            pass
        elif len(self.tail_queue) == 1:
            if self.tail_queue[-1].freeze:
                self.tail_queue[-1].freeze = False
            else:
                self.tail_queue[0] = self.DeepCopy()
        else:
            if self.tail_queue[-1].freeze:
                self.tail_queue[-1].freeze = False
                new_tail = self.tail_queue.pop()
                self.tail_queue[-1] = self.DeepCopy()
                last_changed = self.tail_queue.pop()
                self.tail_queue.insert(len(self.tail_queue) - 1, new_tail)
                self.tail_queue.insert(0, last_changed)
            else:
                self.tail_queue[-1] = self.DeepCopy()
                last_changed = self.tail_queue.pop()
                self.tail_queue.insert(0, last_changed)
        super().Move()

    def AddSector(self):
        if len(self.tail_queue) == 0:
            now_sector = self.DeepCopy()
        else:
            now_sector = self.tail_queue[-1].DeepCopy()
        now_sector.freeze = True
        self.tail_queue.append(now_sector)

    def Draw(self, screen):
        super().Draw(screen)
        for i in self.tail_queue:
            i.Draw(screen)


class Apple(Sector):
    def __init__(self, color):
        super().__init__(color, 100, 100, 20, 20)

    def Replace(self):
        x = random.randint(0, 29)
        y = random.randint(0, 19)
        self.rect.x = x * 20
        self.rect.y = y * 20


apple = Apple(GREEN)
snake = Snake(WHITE, apple)
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.SetXVelocity(-1)
            if event.key == pygame.K_RIGHT:
                snake.SetXVelocity(1)
            if event.key == pygame.K_DOWN:
                snake.SetYVelocity(1)
            if event.key == pygame.K_UP:
                snake.SetYVelocity(-1)
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
    clock.tick(fps)
    snake.Move()
    screen.fill("black")
    apple.Draw(screen)
    snake.Draw(screen)
    pygame.display.update()
