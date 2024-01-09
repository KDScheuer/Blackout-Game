import pygame

levels = {
    'Block 1': {
        'Buildings': {
            'building_1': pygame.Rect(1060, 220, 100, 500),
            'building_2': pygame.Rect(810, 470, 100, 250)
        },
        'Stars': {
            '3 Star': 2,
            '2 Star': 3,
            '1 Star': 4
        },
        'Wind': .5
    },

    'Block 2': {
        'Buildings': {
            'building_1': pygame.Rect(1060, 220, 100, 500),
            'building_2': pygame.Rect(810, 470, 100, 250),
            'building_3': pygame.Rect(610, 470, 100, 250)
        },
        'Stars': {
            '3 Star': 3,
            '2 Star': 4,
            '1 Star': 5
        },
        'Wind': .5
    },

    'Block 3': {
        'Buildings': {
            'building_1': pygame.Rect(1060, 470, 100, 250),
            'building_2': pygame.Rect(810, 220, 100, 500)
        },
        'Stars': {
            '3 Star': 2,
            '2 Star': 3,
            '1 Star': 4
        },
        'Wind': -.5
    },

    'Block 4': {
        'Buildings': {
            'building_1': pygame.Rect(600, 220, 150, 500),
            'building_2': pygame.Rect(820, 600, 100, 120),
            'building_3': pygame.Rect(940, 600, 100, 120),
            'building_4': pygame.Rect(1060, 320, 150, 400)
        },
        'Stars': {
            '3 Star': 4,
            '2 Star': 5,
            '1 Star': 6
        },
        'Wind': -.5
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
        'Wind': -.5
    },
}
