# graphics and tileset addresses for main hub tileset
MAIN_HUB_GFX_ADDR = 0x42011C
MAIN_HUB_TILEMAP_ADDR = 0x45DCD0

# room and door IDs
MAIN_HUB_CENTER_ROOM = 0x18
MAIN_HUB_ELE_ROOMS = [0x1C, 0x19, 0x1D, 0x1A, 0x1E, 0x1B] # 1-6
MAIN_HUB_ELE_DOORS = [0x43, 0x44, 0x45, 0x46, 0x47, 0x48] # 1-6

# BG2 block numbers for area numbers
MAIN_HUB_SMALL_NUM_BLOCK = 0x1B5
MAIN_HUB_LARGE_NUM_BLOCKS = [0x118, 0x113, 0x114, 0x115, 0x133, 0x134, 0x135] # 0-6

# block coordinates of area numbers
MAIN_HUB_CENTER_SMALL_NUM_COORDS_1 = [
    (0x12, 0x0F), # 1
    (0x1D, 0x0F), # 2
    (0x12, 0x10), # 3
    (0x1D, 0x10), # 4
    (0x12, 0x11), # 5
    (0x1D, 0x11), # 6
]
MAIN_HUB_CENTER_SMALL_NUM_COORDS_2 = [
    (0x0A, 0x10), # 1
    (0x25, 0x10), # 2
    (0x08, 0x10), # 3
    (0x27, 0x10), # 4
    (0x06, 0x10), # 5
    (0x29, 0x10), # 6
]
MAIN_HUB_ELE_ROOM_SMALL_NUM_COORDS = [
    [
        None,         # 1
        (0x0D, 0x05), # 2
        (0x04, 0x06), # 3
        (0x0D, 0x06), # 4
        (0x04, 0x07), # 5
        (0x0D, 0x07)  # 6
    ],
    [
        (0x04, 0x05), # 1
        None,         # 2
        (0x04, 0x06), # 3
        (0x0D, 0x06), # 4
        (0x04, 0x07), # 5
        (0x0D, 0x07)  # 6
    ],
    [
        (0x0D, 0x04), # 1
        (0x0D, 0x05), # 2
        None,         # 3
        (0x0D, 0x06), # 4
        (0x04, 0x06), # 5
        (0x0D, 0x07)  # 6
    ],
    [
        (0x04, 0x05), # 1
        (0x04, 0x04), # 2
        (0x04, 0x06), # 3
        None,         # 4
        (0x04, 0x07), # 5
        (0x0D, 0x06)  # 6
    ],
    [
        (0x0D, 0x05), # 1
        (0x0D, 0x06), # 2
        (0x0D, 0x04), # 3
        (0x0D, 0x07), # 4
        None,         # 5
        (0x0D, 0x08)  # 6
    ],
    [
        (0x04, 0x06), # 1
        (0x04, 0x05), # 2
        (0x04, 0x07), # 3
        (0x04, 0x04), # 4
        (0x04, 0x08), # 5
        None          # 6
    ]
]
MAIN_HUB_ELE_ROOM_LARGE_NUM_COORD = (0x09, 0x06)
