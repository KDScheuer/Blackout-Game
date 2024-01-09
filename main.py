import pygame
import os
import time
import random
from button import Button
from levels import levels
from player import Player
from shots import Shot
from overlay import Overlay
from wind_effect import WindEffect


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


def power_animation(building_hit, buildings, powered_buildings, overlay, player, image1, image2, clock, shot):
    # Plays Sounds Effect When Building is Hit
    pygame.mixer.music.load('./Assets/shockwave.wav')
    pygame.mixer.music.play()

    # Controls How Many Times the Building Hit Will Flash
    for i in range(4):

        # Draws UnPowered Buildings to Screen
        for building in buildings:
            building_image = pygame.transform.scale(image1, (building.width, building.height))
            screen.blit(building_image, building.topleft)

        # Draws Powered Buildings to Screen
        for building in powered_buildings:
            building_image = pygame.transform.scale(image2, (building.width, building.height))
            screen.blit(building_image, building.topleft)

        # If Even Building Hit is On else it is Off (This is What Makes the Hit Building Flash)
        if i % 2 == 0:
            building_image2 = pygame.transform.scale(image2, (building_hit.width, building_hit.height))
            screen.blit(building_image2, building_hit.topleft)
        else:
            building_image = pygame.transform.scale(image1, (building_hit.width, building_hit.height))
            screen.blit(building_image, building_hit.topleft)

        # Draws the other elements onto the screen, so they don't disappear to the player
        shot.update()
        player.update()
        overlay.update()
        pygame.display.update()
        clock.tick(30)


def block_x(level, progress):
    # Get Global Variables to Establish Block 1 Game Loop
    global screen, clock, running

    # Load Background Image
    image = pygame.image.load('./Assets/city_skyline.png')
    background = pygame.transform.scale(image, (1270, 720))

    # Load Building Image
    building_image = pygame.image.load('./Assets/building.png')
    building_image2 = pygame.image.load('./Assets/building2.png')

    # Load Star Image
    star_image_raw = pygame.image.load('./Assets/star.png')
    star_image = pygame.transform.scale(star_image_raw, (95, 105))

    # Initialize Player and Shots
    player = Player(screen)
    shot = Shot(screen)

    # Import Buildings for Level
    buildings = [rect for building, rect in levels[level]['Buildings'].items()]
    powered_buildings = []

    # Set Menu Caption on Window
    pygame.display.set_caption('BLACKOUT / Block 1')

    # Sets Wind Effect for the Level
    shot.wind = levels[level]['Wind']

    # Creates Object to Display Wind Speed Moving Across Screen
    clouds_start = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7']
    clouds = []
    for cloud in clouds_start:
        cloud = WindEffect(screen)
        cloud.speed = levels[level]['Wind']
        cloud.x_pos = random.randint(0, 1270)
        cloud.y_pos = random.randint(a=0, b=250)
        clouds.append(cloud)

    # Block 1 Game Loop
    while running:
        # Display Background Color
        screen.fill('black')
        screen.blit(background, (0, 0))

        # Moves Wind
        for cloud in clouds:
            cloud.update()

        # Initialize Overlay
        overlay = Overlay(screen, player.shots_fired, level, levels[level], shot.shot_angle,
                          shot.shot_power, star_image)
        overlay.update()

        # Draw Buildings to Screen
        for building in buildings:
            pygame.draw.rect(screen, 'gray', building)
            building_image = pygame.transform.scale(building_image, (building.width, building.height))
            screen.blit(building_image, building.topleft)
            if pygame.Rect.contains(building, shot.sprite):
                # Keeps Track of What Buildings are Powered
                buildings.remove(building)
                power_animation(building, buildings, powered_buildings, overlay ,player, building_image,
                                building_image2, clock, shot)
                powered_buildings.append(building)
                shot.reset()

        for powered_building in powered_buildings:
            if pygame.Rect.contains(powered_building, shot.sprite):
                shot.reset()
            pygame.draw.rect(screen, 'yellow', powered_building)
            building_image2 = pygame.transform.scale(building_image2,
                                                    (powered_building.width, powered_building.height))
            screen.blit(building_image2, powered_building.topleft)

        # Gets Keys Press on Keyboard
        keys_pressed = pygame.key.get_pressed()

        # If the shot is not fired this will continue to update the shot
        if not shot.fired:
            if keys_pressed[pygame.K_UP] and shot.shot_power < 100:
                shot.shot_power += 1
            if keys_pressed[pygame.K_DOWN] and shot.shot_power > 0:
                shot.shot_power -= 1
            if keys_pressed[pygame.K_LEFT] and shot.shot_angle < 90:
                shot.shot_angle += 1
            if keys_pressed[pygame.K_RIGHT] and shot.shot_angle > 0:
                shot.shot_angle -= 1

            # If the Space Bar is Pressed it will Calculate the Tajactory and Pause User Input until the shot is over
            if keys_pressed[pygame.K_SPACE]:
                shot.calculate_shot()
                pygame.mixer.music.load('./Assets/laser-shot.wav')
                pygame.mixer.music.play()
                shot.fired = True
                player.shots_fired += 1

        if shot.fired:
            shot.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw Player and shot to Screen
        shot.update()
        player.update()

        # Update Screen and Limit Frame Rate
        pygame.display.update()
        clock.tick(30)

        # Checks if all buildings have been powered, If so Displays a victory message and returns to menu
        if not buildings:
            screen.blit(overlay.level_beat_surface, (635 - overlay.level_beat_surface.get_width() // 2,
                                                     360 - overlay.level_beat_surface.get_height() // 2))
            pygame.display.update()
            if player.shots_fired <= levels[level]['Stars']['3 Star']:
                progress[level] = 3
            elif player.shots_fired <= levels[level]['Stars']['2 Star']:
                progress[level] = 2
            else:
                progress[level] = 1
            with open('Blackout_Save_Data.txt', 'w') as f:
                for key, value in progress.items():
                    f.write(str(key) + ',' + str(value) + '\n')
            time.sleep(2)
            menu(progress)


def menu(progress):
    # Get Global Variables to Establish Menu Game Loop
    global screen, clock, running

    # Load Background Image
    image = pygame.image.load('./Assets/city_skyline_menu.png')
    background = pygame.transform.scale(image, (1270, 720))
    control_image = pygame.image.load('./Assets/controls.PNG')
    controls = pygame.transform.scale(control_image, (315, 165))

    # Set Menu Caption on Window
    pygame.display.set_caption('BLACKOUT / Menu')

    # Initializing Menu Text and Variables
    title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    title = "BLACKOUT"
    title_color = (255, 255, 0)
    star_desc_color = (200, 200, 25)
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
    description1 = '''Following a City Wide Black-Out,'''
    description_font1 = pygame.font.Font(None, 40)
    description_surface1 = description_font1.render(description1, True, star_desc_color)
    description2 = ''' We Need you to reconnect the Buildings and Restore Power'''
    description_surface2 = description_font1.render(description2, True, star_desc_color)

    # Menu Game Loop
    while running:
        # Display Background Color
        screen.fill('black')
        screen.blit(background, (0, 0))
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
                pygame.mixer.music.load('./Assets/click.wav')
                if quit_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    running = False
                    return
                if block1_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    block_x('Block 1', progress)
                if block2_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    block_x('Block 2', progress)
                if block3_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    block_x('Block 3', progress)
                if block4_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    block_x('Block 4', progress)
                if block5_button.check_for_input(mouse_pos):
                    pygame.mixer.music.play()
                    block_x('Block 5', progress)

        # Writing Buttons to Screen
        for button in [block1_button, block2_button, block3_button, block4_button, block5_button, quit_button]:
            button.change_color(mouse_pos)
            button.update(screen)

        # Writing Title, Stars, and Description to Screen
        screen.blit(title_surface, (635 - title_surface.get_width() // 2, 50 - title_surface.get_height() // 2))
        screen.blit(star_surface, (635 - star_surface.get_width() // 2, 150 - title_surface.get_height() // 2))
        screen.blit(description_surface1, (550 - star_surface.get_width() // 2, 225 - title_surface.get_height() // 2))
        screen.blit(description_surface2, (350 - star_surface.get_width() // 2, 260 - title_surface.get_height() // 2))

        # Display Controls
        screen.blit(controls, (950, 550))

        # Update Screen and Limit Frame Rate
        pygame.display.update()
        clock.tick(30)


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
