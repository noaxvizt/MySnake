import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("ЗМЕЙКА")
pygame.display.set_icon(pygame.image.load("data/images/icon.png"))
flRunning = True
fps = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()


class Snake():
    def __init__(self, color):
        self.x_position = 10
        self.y_position = 10
        self.x_size = 10
        self.y_size = 10
        self.x_velocity = 0
        self.y_velocity = 0
        self.color = color
        self.rect = pygame.Surface((self.x_size, self.y_size))
        self.rect.fill(color)

    def Draw(self, screen, ):
        screen.blit(self.rect, (self.x_position, self.y_position))

    def Move(self, fps):
        dt = 1 / fps
        self.x_position += self.x_size * self.x_velocity
        self.y_position += self.y_size * self.y_velocity

    def SetXVelocity(self, x_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = 0

    def SetYVelocity(self, y_velocity):
        self.y_velocity = y_velocity
        self.x_velocity = 0


class Apple():
    def __init__(self, color):
        self.x_position = 100
        self.y_position = 100
        self.x_size = 10
        self.y_size = 10
        self.color = color
        self.rect = pygame.Surface((self.x_size, self.y_size))
        self.rect.fill(color)

    def Draw(self, screen):
        screen.blit(self.rect, (self.x_position, self.y_position))


snake = Snake(WHITE)
apple = Apple(GREEN)
while flRunning:
    screen.fill("black")
    snake.Draw(screen)
    apple.Draw(screen)
    pygame.display.update()
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
    snake.Move(fps)
