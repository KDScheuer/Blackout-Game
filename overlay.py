import pygame


class Overlay:
    def __init__(self, screen, shots, level, level_details, angle, power, image):
        self.total_shots_font = pygame.font.Font(None, 30)
        self.total_shots = 'Shots Taken: ' + str(shots)
        self.total_shots_surface = self.total_shots_font.render(self.total_shots, True, 'white')

        self.wind_font = pygame.font.Font(None, 30)
        self.wind = 'Wind: ' + str(level_details['Wind'])
        self.wind_surface = self.wind_font.render(self.wind, True, 'white')

        self.level_font = pygame.font.Font(None, 60)
        self.level = level
        self.level_surface = self.level_font.render(self.level, True, 'white')

        self.star_image = image
        self.star_font = pygame.font.Font(None, 25)
        self.star_text_3 = str(level_details['Stars']['3 Star'])
        self.star_text_2 = str(level_details['Stars']['2 Star'])
        self.star_text_1 = str(level_details['Stars']['1 Star']) + '+'
        self.star_text_surface_3 = self.star_font.render(self.star_text_3, True, 'black')
        self.star_text_surface_2 = self.star_font.render(self.star_text_2, True, 'black')
        self.star_text_surface_1 = self.star_font.render(self.star_text_1, True, 'black')

        self.stat_font = pygame.font.Font(None, 30)
        self.angle = 'Angle: ' + str(angle)
        self.power = 'Power: ' + str(power)
        self.angle_surface = self.stat_font.render(self.angle, True, 'yellow')
        self.power_surface = self.stat_font.render(self.power, True, 'yellow')

        self.level_beat_font = pygame.font.Font(None, 100)
        self.level_beat_text = str(self.level) + ' Beat'
        self.level_beat_surface = self.level_beat_font.render(self.level_beat_text, True, 'yellow')

        self.screen = screen

    def update(self):
        self.screen.blit(self.level_surface, (10, 10))
        self.screen.blit(self.wind_surface, (10, 55))
        self.screen.blit(self.total_shots_surface, (10, 80))
        self.screen.blit(self.angle_surface, (150, 650))
        self.screen.blit(self.power_surface, (150, 675))
        self.screen.blit(self.star_image, (-10, 95))
        self.screen.blit(self.star_image, (60, 95))
        self.screen.blit(self.star_image, (130, 95))
        self.screen.blit(self.star_text_surface_3, (35, 140))
        self.screen.blit(self.star_text_surface_2, (105, 140))
        self.screen.blit(self.star_text_surface_1, (170, 140))
        # self.screen.blit(self.star_image, (1000, 0))
        # self.screen.blit(self.star_image, (1075, 0))
        # self.screen.blit(self.star_image, (1150, 0))
        # self.screen.blit(self.star_text_surface_3, (1045, 45))
        # self.screen.blit(self.star_text_surface_2, (1120, 45))
        # self.screen.blit(self.star_text_surface_1, (1190, 45))
