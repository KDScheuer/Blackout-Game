import pygame


class WindEffect:
    def __init__(self, screen):
        self.screen = screen
        self.x_pos = 0
        self.y_pos = 20
        self.speed = 0
        self.effect_rect = pygame.Rect((self.x_pos, self.y_pos), (100, 10))

    def move(self):
        self.x_pos += self.speed
        self.effect_rect = pygame.Rect((self.x_pos, self.y_pos), (100, 10))

    def update(self):
        if self.x_pos > 1270 and self.speed > 0:
            self.x_pos = -110
        elif self.x_pos < -120 and self.speed < 0:
            self.x_pos = 1400
        self.move()
        pygame.draw.rect(self.screen, 'gray', self.effect_rect)
