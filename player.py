import pygame


class Player:
    def __init__(self, screen):
        self.x_pos = 50
        self.y_pos = 670
        self.shots_fired = 0
        self.screen = screen
        self.sprite = pygame.Rect(self.x_pos, self.y_pos, 50, 50)
        image = pygame.image.load('./Assets/power_station.png')
        self.image = pygame.transform.scale(image, (50, 50))


    def update(self):
        pygame.draw.rect(self.screen, 'white', self.sprite)
        self.screen.blit(self.image, (self.x_pos, self.y_pos))
