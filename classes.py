import pygame
import random

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Inside the Paddle class:
    def move_up(self):
        self.rect.y -= 5

    def move_down(self):
        self.rect.y += 5

class Ball(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2
        self.screen_width = screen_width
        self.screen_height = screen_height
    # Inside the Ball class:
    def update(self, player_paddle, ai_paddle):
        # Check for collision with the player paddle
        if pygame.sprite.collide_rect(self, player_paddle):
            self.speed_x *= -1
        # Check for collision with the AI paddle
        if pygame.sprite.collide_rect(self, ai_paddle):
            self.speed_x *= -1

        # Check for collision with the top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
        # Check for collision with the player paddle
        if pygame.sprite.collide_rect(self, player_paddle):
            self.speed_x *= -1
        # Check for collision with the AI paddle
        if pygame.sprite.collide_rect(self, ai_paddle):
            self.speed_x *= -1
