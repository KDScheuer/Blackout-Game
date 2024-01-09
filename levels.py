import pygame

levels = {
    'Block 1': {
        'Buildings': {
            'building_1': pygame.Rect(1100, 220, 100, 500),
            'building_2': pygame.Rect(950, 320, 100, 400),
            'building_3': pygame.Rect(700, 370, 100, 350),
            'building_4': pygame.Rect(550, 345, 100, 375),
        },
        'Stars': {
            '3 Star': 4,
            '2 Star': 6,
            '1 Star': 7
        },
        'Wind': -.5
    },

    'Block 2': {
        'Buildings': {
            'building_1': pygame.Rect(1100, 220, 100, 500),
            'building_2': pygame.Rect(990, 270, 100, 450),
            'building_3': pygame.Rect(800, 245, 100, 475),
            'building_4': pygame.Rect(600, 270, 100, 450),
        },
        'Stars': {
            '3 Star': 4,
            '2 Star': 5,
            '1 Star': 6
        },
        'Wind': .3
    },

    'Block 3': {
        'Buildings': {
            'building_1': pygame.Rect(1100, 320, 100, 400),
            'building_2': pygame.Rect(990, 320, 100, 400),
            'building_3': pygame.Rect(880, 320, 100, 400),
            'building_4': pygame.Rect(650, 420, 100, 300),
            'building_5': pygame.Rect(540, 420, 100, 300),
        },
        'Stars': {
            '3 Star': 5,
            '2 Star': 7,
            '1 Star': 8
        },
        'Wind': 1
    },

    'Block 4': {
        'Buildings': {
            'building_1': pygame.Rect(1100, 320, 100, 400),
            'building_2': pygame.Rect(900, 370, 100, 350),
            'building_3': pygame.Rect(790, 345, 100, 375),
            'building_4': pygame.Rect(575, 270, 100, 450)
        },
        'Stars': {
            '3 Star': 4,
            '2 Star': 5,
            '1 Star': 6
        },
        'Wind': -.7
    },

    'Block 5': {
        'Buildings': {
            'building_1': pygame.Rect(1110, 220, 100, 500),
            'building_2': pygame.Rect(985, 320, 100, 400),
            'building_3': pygame.Rect(860, 370, 100, 350),
            'building_4': pygame.Rect(735, 320, 100, 400),
            'building_5': pygame.Rect(610, 570, 100, 150),
            'building_6': pygame.Rect(485, 620, 100, 200),
            'building_7': pygame.Rect(360, 570, 100, 150),
        },
        'Stars': {
            '3 Star': 7,
            '2 Star': 8,
            '1 Star': 9
        },
        'Wind': -.3
    },
}
