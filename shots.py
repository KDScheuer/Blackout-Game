import pygame
import math


class Shot:
    def __init__(self, screen):
        self.start_x_pos = 65
        self.start_y_pos = 690
        self.x_pos = 65
        self.y_pos = 690
        self.current_power = 0
        self.shot_power = 50
        self.current_angle = 0
        self.shot_angle = 45
        self.fired = False
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.3
        self.wind = 0
        self.screen = screen
        self.sprite = pygame.Rect(self.x_pos, self.y_pos, 20, 20)
        self.angle_bar_length = 100
        self.angle_bar_x_pos = 0
        self.angle_bar_y_pos = 0
        image = pygame.image.load('./Assets/power.png')
        self.image = pygame.transform.scale(image, (20, 20))

    def update(self):
        # Draws the Updated Position of the Shot
        self.sprite = pygame.Rect(self.x_pos, self.y_pos, 15, 15)
        pygame.draw.rect(self.screen, 'orange', self.sprite)
        self.screen.blit(self.image, (self.x_pos, self.y_pos))

        # Calculates were the Angle Bar needs to be Placed to Assist the Player
        angle_radians = math.radians(self.shot_angle)
        self.angle_bar_x_pos = self.start_x_pos + self.angle_bar_length * math.cos(angle_radians)
        self.angle_bar_y_pos = self.start_y_pos - self.angle_bar_length * math.sin(angle_radians)

        # Draws the Angle Bar to the Screen
        pygame.draw.line(self.screen, 'yellow', (self.start_x_pos, self.start_y_pos),
                         (self.angle_bar_x_pos, self.angle_bar_y_pos), 3)

    def calculate_shot(self):
        # Calculates the Tajactory of the Shot (Power Divided by 5 to keep it reasonable)
        self.current_power = self.shot_power / 4
        self.current_angle = math.radians(self.shot_angle)
        self.vel_x = self.current_power * math.cos(self.current_angle)
        self.vel_y = -self.current_power * math.sin(self.current_angle)

    def move(self):
        # Draws the shot as it moves across its Trajectory
        self.x_pos += self.vel_x
        self.y_pos += self.vel_y
        self.vel_y += self.gravity
        # Sets Wind Effect the Multiplier is used to fine tune the effect on the shot
        wind_effect = self.wind * 0.1
        self.vel_x += wind_effect
        self.sprite.topleft = (int(self.x_pos), int(self.y_pos))

        # Resets the Shot if it Leaves the Screen on the Bottom or the Right
        if self.y_pos > 720 or self.x_pos > 1270:
            self.reset()

    def reset(self):
        self.fired = False
        self.x_pos = self.start_x_pos
        self.y_pos = self.start_y_pos
