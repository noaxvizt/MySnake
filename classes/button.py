import pygame
from data.constants import *
from data.events import *


class Button:
    def __init__(self, x_position, y_position, x_size, y_size, image_path):
        self.image_path = image_path
        self.x_position = x_position
        self.y_position = y_position
        self.x_size = x_size
        self.y_size = y_size
        self.clicked = False
        self.sector = pygame.transform.scale(pygame.image.load(self.image_path), (self.x_size, self.y_size))
        self.rect = self.sector.get_rect(topleft=(self.x_position, self.y_position))

    def Draw(self, screen):
        pos = pygame.mouse.get_pos()
        do_action = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                do_action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        screen.blit(self.sector, self.rect)
        return do_action
