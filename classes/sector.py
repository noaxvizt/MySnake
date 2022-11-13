import pygame
import random
from collections import deque
from data.constants import *


class Sector:
    def __init__(self, color, x_position, y_position, x_size, y_size, image_path="data/images/apple.png"):
        self.color = color
        self.image_path = image_path
        self.x_position = x_position
        self.y_position = y_position
        self.x_size = x_size
        self.y_size = y_size
        self.sector = pygame.transform.scale(pygame.image.load(self.image_path), (self.x_size, self.y_size))
        self.rect = self.sector.get_rect(topleft=(self.x_position, self.y_position))
        self.freeze = False
        self.x_velocity = 0
        self.y_velocity = 0

    def Draw(self, screen):
        screen.blit(self.sector, self.rect)

    def Move(self):
        self.rect.move_ip(self.x_size * self.x_velocity, self.y_size * self.y_velocity)
        self.rect.x %= WIDHT
        self.rect.y %= HEIGHT

    def SetXVelocity(self, x_velocity):
        self.x_velocity = x_velocity
        self.y_velocity = 0

    def SetYVelocity(self, y_velocity):
        self.y_velocity = y_velocity
        self.x_velocity = 0

    def DeepCopy(self, image_path="data/images/snakestale.png"):
        now_copy = Sector(self.color, self.x_position, self.y_position, self.x_size, self.y_size, image_path)
        now_copy.sector = pygame.transform.scale(pygame.image.load(now_copy.image_path), (now_copy.x_size, now_copy.y_size))
        now_copy.rect = now_copy.sector.get_rect(topleft=(now_copy.x_position, now_copy.y_position))
        now_copy.rect.x = self.rect.x
        now_copy.rect.y = self.rect.y
        now_copy.freeze = self.freeze
        return now_copy
