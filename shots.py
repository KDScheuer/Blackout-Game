import pygame
import math


class Shot:
    def __init__(self, screen):
        self.start_x_pos = 65
        self.start_y_pos = 690
        self.x_pos = 65
        self.y_pos = 690
        self.current_power = 0
        self.shot_power = 0
        self.current_angle = 0
        self.shot_angle = 45
        self.fired = False
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.1
        self.screen = screen
        self.sprite = pygame.Rect(self.x_pos, self.y_pos, 15, 15)
        self.angle_bar_length = 100
        self.angle_bar_x_pos = 0
        self.angle_bar_y_pos = 0

    def update(self):
        # Draws the Updated Position of the Shot
        self.sprite = pygame.Rect(self.x_pos, self.y_pos, 15, 15)
        pygame.draw.rect(self.screen, 'orange', self.sprite)

        # Calculates were the Angle Bar needs to be Placed to Assist the Player
        angle_radians = math.radians(self.shot_angle)
        self.angle_bar_x_pos = self.start_x_pos + self.angle_bar_length * math.cos(angle_radians)
        self.angle_bar_y_pos = self.start_y_pos - self.angle_bar_length * math.sin(angle_radians)

        # Draws the Angle Bar to the Screen
        pygame.draw.line(self.screen, 'white', (self.start_x_pos, self.start_y_pos),
                         (self.angle_bar_x_pos, self.angle_bar_y_pos), 5)

    def calculate_shot(self):
        # Calculates the Tajactory of the Shot (Power Divided by 5 to keep it reasonable)
        self.current_power = self.shot_power / 5
        self.current_angle = math.radians(self.shot_angle)
        self.vel_x = self.current_power * math.cos(self.current_angle)
        self.vel_y = -self.current_power * math.sin(self.current_angle)

    def move(self):
        # Draws the shot as it moves across its Trajectory
        self.x_pos += self.vel_x
        self.y_pos += self.vel_y
        self.vel_y += self.gravity
        self.sprite.topleft = (int(self.x_pos), int(self.y_pos))

        # Resets the Shot if it Leaves the Screen on the Bottom or the Right
        if self.y_pos > 720 or self.x_pos > 1270:
            self.reset()

    def reset(self):
        self.fired = False
        self.x_pos = self.start_x_pos
        self.y_pos = self.start_y_pos
        self.shot_power = 0
