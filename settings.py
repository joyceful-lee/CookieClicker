import pygame

# Setting
settings = {
    'left_width': 200,
    'center_width': 400,
    'right_width': 200,
    'center_height': 450,
    'right_height': 450,
    'store_display_height': 60,
    'storeOptionHeight': 42,
    'storeScale': 0.37,
    'center_top': 50,
    'store_size': 73,
    'header_font': "georgia",
    'sub_font': 'arial',
    'index': 1,

    # Colors
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 200, 0),
    'red': (174, 0, 0),

    # Values and Cost

    'tab': "DEFAULT",
    'count': 0,
    'multiplier': 1.15,
    'auto_click_persec': 0,  # auto click
    'manual_click_current': 1,  # manual click
    'cursor_prices': [15, 0.1, 0],
    'grandma_prices': [100, 1, 0],
    'farm_prices': [1100, 8, 0],
    'mine_prices': [12000, 47, 0],
    'factory_prices': [130000, 260, 0],

    # Images
    'cookie_img': pygame.image.load("images/Cookie!!!.png"),
    'wallpaper_img': pygame.image.load("images/Wallpaper.jpg"),
    'divider': pygame.image.load("images/divider.png"),
    'divider_h': pygame.image.load("images/horizontal.png"),
    'stats_greyed': pygame.image.load("images/stats.png"),
    'stats_hover': pygame.image.load("images/stats_hover.png"),
    'default_img': pygame.image.load("images/default.png"),
    #########cursors#########
    'cursor_b': pygame.image.load("images/store/cursor_blocked.png"),
    'cursor_u': pygame.image.load("images/store/cursor_unblocked.png"),
    'cursor_g': pygame.image.load("images/store/cursor_greyed.png"),
    'cursor_buy': pygame.image.load("images/display/cursor_click.png"),
    #########grandma#########
    'grandma_b': pygame.image.load("images/store/grandma_blocked.png"),
    'grandma_u': pygame.image.load("images/store/grandma_unblocked.png"),
    'grandma_g': pygame.image.load("images/store/grandma_greyed.png"),
    'grandma_buy1': pygame.image.load("images/display/grannie/grandma_buy1.png"),
    'grandma_buy2': pygame.image.load("images/display/grannie/grandma_buy2.png"),
    'grandma_buy3': pygame.image.load("images/display/grannie/grandma_buy3.png"),
    'grandma_buy4': pygame.image.load("images/display/grannie/grandma_buy4.png"),
    'grandma_display': pygame.image.load("images/display/grandma_display.png"),
    #########farm############
    'farm_b': pygame.image.load("images/store/farm_blocked.png"),
    'farm_u': pygame.image.load("images/store/farm_unblocked.png"),
    'farm_g': pygame.image.load("images/store/farm_greyed.png"),
    'farm_buy': pygame.image.load("images/display/farm_buy.png"),
    'farm_display': pygame.image.load("images/display/farm_display.png"),
    #########mine############
    'mine_b': pygame.image.load("images/store/mine_blocked.png"),
    'mine_u': pygame.image.load("images/store/mine_unblocked.png"),
    'mine_g': pygame.image.load("images/store/mine_greyed.png"),
    'mine_buy': pygame.image.load("images/display/mine_buy.png"),
    'mine_display': pygame.image.load("images/display/mine_display.png"),
    #########factory############
    'factory_b': pygame.image.load("images/store/factory_blocked.png"),
    'factory_u': pygame.image.load("images/store/factory_unblocked.png"),
    'factory_g': pygame.image.load("images/store/factory_greyed.png"),
    'factory_buy': pygame.image.load("images/display/factory_buy.png"),
    'factory_display': pygame.image.load("images/display/factory_display.png")}

img_org = {
    'total_cookies': settings['count'],
    'wall_scale': pygame.transform.scale(settings['wallpaper_img'], (
        int(settings['wallpaper_img'].get_width() * 0.5), int(settings['wallpaper_img'].get_height() * 0.6))),
    'divider_scale': pygame.transform.scale(settings['divider'], (
        int(settings['divider'].get_width() * 0.5), int(settings['divider'].get_height() * 0.6))),
    'divider_h_scale' : pygame.transform.scale(settings['divider_h'],
    (int(settings['divider_h'].get_width() * 0.8), int(settings['divider_h'].get_height() * 0.8))),
    'stats_images': [settings['stats_greyed'], settings['stats_hover']],
    'default_images': [settings['default_img'], settings['default_img']],
    'cursor_img': [settings['cursor_b'], settings['cursor_u'], settings['cursor_g']],
    'grandma_img': [settings['grandma_b'], settings['grandma_u'], settings['grandma_g']],
    'farm_img': [settings['farm_b'], settings['farm_u'], settings['farm_g']],
    'mine_img': [settings['mine_b'], settings['mine_u'], settings['mine_g']],
    'factory_img': [settings['factory_b'], settings['factory_u'], settings['factory_g']],
    'grandma_display_images': [settings['grandma_display'], settings['grandma_buy1'], settings['grandma_buy2'],
                               settings['grandma_buy3'], settings['grandma_buy4']],
    'farm_display_images': [settings['farm_display'], settings['farm_buy']],
    'mine_display_images': [settings['mine_display'], settings['mine_buy']],
    'factory_display_images': [settings['factory_display'], settings['factory_buy']]


}
