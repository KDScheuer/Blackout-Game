import pygame


class Overlay:
    def __init__(self, screen, shots, level, level_details, angle, power):
        self.total_shots_font = pygame.font.Font(None, 30)
        self.total_shots = 'Shots Taken: ' + str(shots)
        self.total_shots_surface = self.total_shots_font.render(self.total_shots, True, 'White')

        self.wind_font = pygame.font.Font(None, 30)
        self.wind = 'Wind: ' + str(level_details['Wind'])
        self.wind_surface = self.wind_font.render(self.wind, True, 'White')

        self.level_font = pygame.font.Font(None, 60)
        self.level = level
        self.level_surface = self.level_font.render(self.level, True, 'White')

        self.star_font = pygame.font.Font(None, 35)
        self.star_text = (str(level_details['Stars']['3 Star']) + '     ' + str(level_details['Stars']['2 Star'])
                          + '     ' + str(level_details['Stars']['1 Star']) + '+')
        self.star_text_surface = self.star_font.render(self.star_text, True, 'White')

        self.stat_font = pygame.font.Font(None, 30)
        self.angle = 'Angle: ' + str(angle)
        self.power = 'Power: ' + str(power)
        self.angle_surface = self.stat_font.render(self.angle, True, 'White')
        self.power_surface = self.stat_font.render(self.power, True, 'White')

        self.level_beat_font = pygame.font.Font(None, 100)
        self.level_beat_text = str(self.level) + ' Beat'
        self.level_beat_surface = self.level_beat_font.render(self.level_beat_text, True, 'White')

        self.screen = screen

    def update(self):
        self.screen.blit(self.level_surface, (10, 10))
        self.screen.blit(self.wind_surface, (10, 55))
        self.screen.blit(self.total_shots_surface, (10, 80))
        self.screen.blit(self.angle_surface, (150, 650))
        self.screen.blit(self.power_surface, (150, 675))
        self.screen.blit(self.star_text_surface, (1100, 50))
