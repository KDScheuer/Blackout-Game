import pygame


class Button:
    def __init__(self, text, pos, font=None):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font or pygame.font.Font(None, 50)
        self.base_color = (100, 100, 100)
        self.hovering_color = (255, 255, 0)
        self.update_text(text)
        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def update_text(self, new_text):
        self.text = self.font.render(new_text, True, self.base_color)
        self.input_text = new_text

    def check_for_input(self, position):
        if (position[0] in range(self.rect.left, self.rect.right) and
                position[1] in range(self.rect.top, self.rect.bottom)):
            return True
        return False

    def change_color(self, position):
        if self.rect.collidepoint(position):
            # Updated this line
            self.update_text(self.input_text)
            self.text = self.font.render(self.input_text, True, self.hovering_color)
        else:
            # Updated this line
            self.update_text(self.input_text)
            self.text = self.font.render(self.input_text, True, self.base_color)
