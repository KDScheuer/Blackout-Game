import pygame
import os
from button import Button
from levels import levels
from player import Player


def player_progress():
    progress = {}
    if os.path.exists('Blackout_Save_Data.txt'):
        with open('Blackout_Save_Data.txt', 'r') as f:
            for line in f.readlines():
                level, score = line.split(',')
                progress[level] = int(score)
    else:
        with open('Blackout_Save_Data.txt', 'w') as f:
            for level in ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']:
                f.write(level + ',' + '0' + '\n')
                progress[level] = 0
    return progress


def block_x(level, progress):
    # Get Global Variables to Establish Block 1 Game Loop
    global screen, clock, running

    # Initialize Player
    player = Player(screen)

    # Import Buildings for Level
    buildings = [rect for building, rect in levels[level]['Buildings'].items()]

    # Set Menu Caption on Window
    pygame.display.set_caption('BLACKOUT / Block 1')

    # Block 1 Game Loop
    while running:
        # Display Background Color
        screen.fill('black')

        # Draw Buildings to Screen
        for building in buildings:
            pygame.draw.rect(screen, 'gray', building)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw Player to Screen
        player.update()

        # Update Screen and Limit Frame Rate
        pygame.display.update()
        clock.tick(60)


def menu(progress):
    # Get Global Variables to Establish Menu Game Loop
    global screen, clock, running

    # Set Menu Caption on Window
    pygame.display.set_caption('BLACKOUT / Menu')

    # Initializing Menu Text and Variables
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    title = "BLACKOUT"
    title_color = (255, 255, 0)
    star_desc_color = (100, 100, 50)
    title_surface = title_font.render(title, True, title_color)

    # Getting Total Stars that the Player has earned
    earned_stars = 0
    total_stars = 15
    for value in progress.values():
        earned_stars += value

    # Initializing Players Earned Stars
    stars = str(earned_stars) + '/' + str(total_stars) + ' stars'
    star_font = pygame.font.Font(None, 75)
    star_surface = star_font.render(stars, True, star_desc_color)

    # Initializing Game Description
    description1 = '''After a city wide black-out, the city needs you to reconnect the'''
    description_font1 = pygame.font.Font(None, 40)
    description_surface1 = description_font1.render(description1, True, star_desc_color)
    description2 = '''buildings and restore power reconnect the buildings and restore power'''
    description_surface2 = description_font1.render(description2, True, star_desc_color)

    # Menu Game Loop
    while running:
        # Display Background Color
        screen.fill('black')

        # Getting Mouse Position
        mouse_pos = pygame.mouse.get_pos()

        # Updating Level Buttons
        block1_text = 'BLOCK 1' + '    Stars: ' + str(progress['Block 1'])
        block1_surface = button_font.render(block1_text, True, title_color)
        block1_button = Button(text=block1_text, pos=(790 - block1_surface.get_width() // 2, 350))
        block2_text = 'BLOCK 2' + '    Stars: ' + str(progress['Block 2'])
        block2_button = Button(text=block2_text, pos=(790 - block1_surface.get_width() // 2, 400))
        block3_text = 'BLOCK 3' + '    Stars: ' + str(progress['Block 3'])
        block3_button = Button(text=block3_text, pos=(790 - block1_surface.get_width() // 2, 450))
        block4_text = 'BLOCK 4' + '    Stars: ' + str(progress['Block 4'])
        block4_button = Button(text=block4_text, pos=(790 - block1_surface.get_width() // 2, 500))
        block5_text = 'BLOCK 5' + '    Stars: ' + str(progress['Block 5'])
        block5_button = Button(text=block5_text, pos=(790 - block1_surface.get_width() // 2, 550))
        quit_text = 'QUIT'
        quit_button = Button(text=quit_text, pos=(790 - block1_surface.get_width() // 2, 650))

        # Checking Game Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.check_for_input(mouse_pos):
                    running = False
                    return
                if block1_button.check_for_input(mouse_pos):
                    block_x('Block 1', progress)
                if block2_button.check_for_input(mouse_pos):
                    block_x('Block 2', progress)
                if block3_button.check_for_input(mouse_pos):
                    block_x('Block 3', progress)
                if block4_button.check_for_input(mouse_pos):
                    block_x('Block 4', progress)
                if block5_button.check_for_input(mouse_pos):
                    block_x('Block 5', progress)

        # Writing Buttons to Screen
        for button in [block1_button, block2_button, block3_button, block4_button, block5_button, quit_button]:
            button.change_color(mouse_pos)
            button.update(screen)

        # Writing Title, Stars, and Description to Screen
        screen.blit(title_surface, (635 - title_surface.get_width() // 2, 50 - title_surface.get_height() // 2))
        screen.blit(star_surface, (635 - star_surface.get_width() // 2, 150 - title_surface.get_height() // 2))
        screen.blit(description_surface1, (350 - star_surface.get_width() // 2, 225 - title_surface.get_height() // 2))
        screen.blit(description_surface2, (300 - star_surface.get_width() // 2, 260 - title_surface.get_height() // 2))

        # Update Screen and Limit Frame Rate
        pygame.display.update()
        clock.tick(60)


def main():
    # Load Player Data or Create Save File
    progress = player_progress()

    # Display Main Menu
    menu(progress)

    # Exit Game
    pygame.quit()


if __name__ == "__main__":
    # Pygame Initialization
    pygame.init()
    screen = pygame.display.set_mode((1270, 720))
    clock = pygame.time.Clock()
    running = True
    main()
