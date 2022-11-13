import pygame
from classes.snake import Snake
from classes.apple import Apple
from classes.sector import Sector
from data.constants import *
from classes.button import Button
from data.events import *




def main_loop():
    global now_mode
    now_mode = 1
    flRunning = True
    # 1 - start window
    # 2 - game
    # 3 - end window
    pygame.init()
    start_menu_init()

    while flRunning:
        if now_mode == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    break
            if now_mode == 1:
                start_menu_run()
        if now_mode == 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake_g.SetXVelocity(-1)
                    if event.key == pygame.K_RIGHT:
                        snake_g.SetXVelocity(1)
                    if event.key == pygame.K_DOWN:
                        snake_g.SetYVelocity(1)
                    if event.key == pygame.K_UP:
                        snake_g.SetYVelocity(-1)
                elif event.type == LOSE_OF_GAME:
                    print("shit")
                    now_mode = 3
                    lose_init(snake_g.score)
                    break
                elif event.type == WIN_OF_GAME:
                    print("sex")
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    break
            if now_mode == 2:
                game_run()
        if now_mode == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    break
            if now_mode == 3:
                lose_run()
        pygame.display.update()


def start_menu_init():
    global screen_sm, fps_sm, start_game_but_sm,clock_sm, background_sm, high_scores_but_sm

    screen_sm = pygame.display.set_mode((WIDHT, HEIGHT))
    fps_sm = 60
    start_game_but_sm = Button(200, 170, 200, 70, "data/images/play_button.png")
    high_scores_but_sm = Button(200, 250, 200, 70, "data/images/rate_button.png")
    clock_sm = pygame.time.Clock()
    background_sm = pygame.image.load("data/images/menu_background.png")


def start_menu_run():
    clock_sm.tick(fps_sm)
    screen_sm.blit(background_sm, (0, 0))
    if start_game_but_sm.Draw(screen_sm):
        global now_mode
        now_mode = 2
        game_init()
        return
    if high_scores_but_sm.Draw(screen_sm):
        print(1)


def game_init():
    global screen_g, fps_g, clock_g, apple_g, snake_g
    screen_g = pygame.display.set_mode((WIDHT, HEIGHT))
    pygame.display.set_caption("ЗМЕЙКА")
    pygame.display.set_icon(pygame.image.load("data/images/icon.png"))

    fps_g = START_FPS
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    clock_g = pygame.time.Clock()
    apple_g = Apple(GREEN)
    snake_g = Snake(WHITE, apple_g)


def game_run():
    fps_g = int((1 + snake_g.score / 30) * START_FPS)
    clock_g.tick(fps_g)
    snake_g.Move()
    screen_g.fill("black")
    apple_g.Draw(screen_g)
    snake_g.Draw(screen_g)


def lose_init(end_score):
    global screen_l, fps_l, retry_but_l, clock_l, background_l

    screen_l = pygame.display.set_mode((WIDHT, HEIGHT))
    fps_l = 60
    retry_but_l = Button(200, 170, 200, 70, "data/images/retry_button.png")
    clock_l = pygame.time.Clock()
    background_l = pygame.image.load("data/images/youdied_background.png")


def lose_run():
    clock_l.tick(fps_sm)
    screen_l.blit(background_l, (0, 0))
    if retry_but_l.Draw(screen_sm):
        global now_mode
        now_mode = 1
        start_menu_init()
