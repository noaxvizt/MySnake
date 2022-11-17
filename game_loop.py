import pygame
from classes.snake import Snake
from classes.apple import Apple
from classes.sector import Sector
from data.constants import *
from classes.button import Button
from data.events import *
from classes.scoring import ScoreCenter


def main_loop():
    global now_mode, my_font, scoreHelper, my_font1
    scoreHelper = ScoreCenter()
    now_mode = 1
    flRunning = True
    # 1 - start window
    # 2 - game window
    # 3 - end window
    # 4 - rate window
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 36)
    my_font1 = pygame.font.SysFont('Comic Sans MS', 20)
    start_menu_init()

    while flRunning:
        if now_mode == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
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
                    pass
                    now_mode = 3
                    lose_init(snake_g.score)
                    break
                elif event.type == WIN_OF_GAME:
                    pass
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    exit()
                    break
            if now_mode == 2:
                game_run()
        if now_mode == 3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    exit()
                    break
            if now_mode == 3:
                lose_run()

        if now_mode == 4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    flRunning = False
                    break
            if now_mode == 4:
                high_score_run()
        pygame.display.update()


def start_menu_init():
    global screen_sm, fps_sm, start_game_but_sm,clock_sm, background_sm, high_scores_but_sm

    screen_sm = pygame.display.set_mode((WIDHT, HEIGHT))
    fps_sm = 60
    start_game_but_sm = Button(200, 170, 200, 70, "data/images/play_button.png")
    high_scores_but_sm = Button(200, 250, 200, 70, "data/images/high_score_button.png")
    clock_sm = pygame.time.Clock()
    background_sm = pygame.image.load("data/images/menu_background.png")


def start_menu_run():
    global now_mode
    clock_sm.tick(fps_sm)
    screen_sm.blit(background_sm, (0, 0))
    if start_game_but_sm.Draw(screen_sm):
        now_mode = 2
        game_init()
        return
    if high_scores_but_sm.Draw(screen_sm):
        now_mode = 4
        high_score_init()
        return


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
    global screen_l, fps_l, retry_but_l, clock_l, background_l, text_surface1, text_surface2

    screen_l = pygame.display.set_mode((WIDHT, HEIGHT))
    fps_l = 60
    retry_but_l = Button(200, 170, 200, 70, "data/images/retry_button.png")
    clock_l = pygame.time.Clock()
    background_l = pygame.image.load("data/images/youdied_background.png")
    if end_score > scoreHelper.GetHighScore():
        text_surface1 = my_font.render(f"Your score is {end_score}", False, (0, 0, 0))
        text_surface2 = my_font.render(f"New record!!!", False, (0, 0, 0))
    else:
        text_surface1 = my_font.render(f"Your score is {end_score}", False, (0, 0, 0))
        text_surface2 = my_font.render(f"High score is {scoreHelper.GetHighScore()}", False, (0, 0, 0))
    scoreHelper.UpdateScore("said", end_score)


def lose_run():
    clock_l.tick(fps_sm)
    screen_l.blit(background_l, (0, 0))
    screen_l.blit(text_surface1, (150, 280))
    screen_l.blit(text_surface2, (150, 330))
    if retry_but_l.Draw(screen_sm):
        global now_mode
        now_mode = 1
        start_menu_init()


def high_score_init():
    global screen_hc, fps_hc, back_but_hc, clock_hc, background_hc, table_of_results_hc, text_surfaces_hc, text_surface1_hc

    screen_hc = pygame.display.set_mode((WIDHT, HEIGHT))
    fps_hc = 60
    back_but_hc = Button(30, 330, 100, 70, "data/images/home_button.png")
    clock_hc = pygame.time.Clock()
    background_hc = pygame.image.load("data/images/menu_background.png")
    text_surface1_hc = my_font.render(f"Top score", False, (0, 0, 0))
    table_of_results_hc = []
    if len(scoreHelper.lis_of_score) == 0:
        table_of_results_hc = ["No data"]
    elif len(scoreHelper.lis_of_score) <= 5:
        table_of_results_hc = scoreHelper.lis_of_score[:]
    else:
        table_of_results_hc = scoreHelper.lis_of_score[:5]
    text_surfaces_hc = []
    for i in range(len(table_of_results_hc)):
        text_surfaces_hc.append((my_font1.render(str(table_of_results_hc[i][1]) + '    ' + table_of_results_hc[i][0], False, (0, 0, 0)), (200, 200 + 40 * i)))


def high_score_run():
    clock_hc.tick(fps_sm)
    screen_hc.blit(background_hc, (0, 0))
    screen_hc.blit(text_surface1_hc, (150, 150))
    for i in text_surfaces_hc:
        screen_hc.blit(*i)
    if back_but_hc.Draw(screen_hc):
        global now_mode
        now_mode = 1
        start_menu_init()