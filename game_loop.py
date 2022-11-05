import pygame
from classes.snake import *
from classes.apple import *
from classes.sector import *


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDHT, HEIGHT))
    pygame.display.set_caption("ЗМЕЙКА")
    pygame.display.set_icon(pygame.image.load("data/images/icon.png"))
    flRunning = True
    fps = START_FPS
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    clock = pygame.time.Clock()
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
                break
        clock.tick(fps)
        snake.Move()
        screen.fill("black")
        apple.Draw(screen)
        snake.Draw(screen)
        pygame.display.update()
