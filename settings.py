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
    'scroll_y': 0,
    'scroll_y_center': 0,

    # Colors
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 200, 0),
    'red': (174, 0, 0),

    # Values and Cost

    'tab': "DEFAULT",
    'count': 100000000,
    'multiplier': 1.15,
    'auto_click_persec': 0,  # auto click
    'manual_click_current': 1,  # manual click
    'cursor_prices': [15, 0.1, 0],
    'grandma_prices': [100, 1, 0],
    'farm_prices': [1100, 8, 0],
    'mine_prices': [12000, 47, 0],
    'factory_prices': [130000, 260, 0],
    'bank_prices': [130000, 260, 0],
    'temple_prices': [130000, 260, 0],
    'wizard_prices': [130000, 260, 0],
    'shipment_prices': [130000, 260, 0],
    'alchemy_prices': [130000, 260, 0],

    # Images
    'cookie_img': pygame.image.load("images/Cookie!!!.png"),
    'wallpaper_img': pygame.image.load("images/Wallpaper.jpg"),
    'wallpaper_top_img': pygame.image.load("images/wallpaper_top.png"),
    'wallpaper_left_img': pygame.image.load("images/wallpaper_left.png"),
    'wallpaper_center_img': pygame.image.load("images/wallpaper_center.png"),
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
    'grandma_buy5': pygame.image.load("images/display/grannie/grandma_buy5.png"),
    'grandma_buy6': pygame.image.load("images/display/grannie/grandma_buy6.png"),
    'grandma_buy7': pygame.image.load("images/display/grannie/grandma_buy7.png"),
    'grandma_buy8': pygame.image.load("images/display/grannie/grandma_buy8.png"),
    'grandma_buy9': pygame.image.load("images/display/grannie/grandma_buy9.png"),
    'grandma_buy10': pygame.image.load("images/display/grannie/grandma_buy10.png"),
    'grandma_buy11': pygame.image.load("images/display/grannie/grandma_buy11.png"),
    'grandma_buy12': pygame.image.load("images/display/grannie/grandma_buy12.png"),
    'grandma_buy13': pygame.image.load("images/display/grannie/grandma_buy13.png"),
    'grandma_buy14': pygame.image.load("images/display/grannie/grandma_buy14.png"),
    'grandma_buy15': pygame.image.load("images/display/grannie/grandma_buy15.png"),
    'grandma_buy16': pygame.image.load("images/display/grannie/grandma_buy16.png"),
    'grandma_buy17': pygame.image.load("images/display/grannie/grandma_buy17.png"),
    'grandma_buy18': pygame.image.load("images/display/grannie/grandma_buy18.png"),
    'grandma_buy19': pygame.image.load("images/display/grannie/grandma_buy19.png"),
    'grandma_buy20': pygame.image.load("images/display/grannie/grandma_buy20.png"),
    'grandma_buy21': pygame.image.load("images/display/grannie/grandma_buy21.png"),
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
    'factory_display': pygame.image.load("images/display/factory_display.png"),
    #########bank############
    'bank_b': pygame.image.load("images/store/bank_blocked.png"),
    'bank_u': pygame.image.load("images/store/bank_unblocked.png"),
    'bank_g': pygame.image.load("images/store/bank_greyed.png"),
    'bank_buy': pygame.image.load("images/display/bank_buy.png"),
    'bank_display': pygame.image.load("images/display/bank_display.png"),
    #########temple############
    'temple_b': pygame.image.load("images/store/temple_blocked.png"),
    'temple_u': pygame.image.load("images/store/temple_unblocked.png"),
    'temple_g': pygame.image.load("images/store/temple_greyed.png"),
    'temple_buy': pygame.image.load("images/display/temple_buy.png"),
    'temple_display': pygame.image.load("images/display/temple_display.png"),
    #########wizard############
    'wizard_b': pygame.image.load("images/store/wizard_blocked.png"),
    'wizard_u': pygame.image.load("images/store/wizard_unblocked.png"),
    'wizard_g': pygame.image.load("images/store/wizard_greyed.png"),
    'wizard_buy': pygame.image.load("images/display/wizard_buy.png"),
    'wizard_display': pygame.image.load("images/display/wizard_display.png"),
    #########shipment############
    'shipment_b': pygame.image.load("images/store/shipment_blocked.png"),
    'shipment_u': pygame.image.load("images/store/shipment_unblocked.png"),
    'shipment_g': pygame.image.load("images/store/shipment_greyed.png"),
    'shipment_buy': pygame.image.load("images/display/shipment_buy.png"),
    'shipment_display': pygame.image.load("images/display/shipment_display.png"),
    #########alchemy############
    'alchemy_b': pygame.image.load("images/store/alchemy_blocked.png"),
    'alchemy_u': pygame.image.load("images/store/alchemy_unblocked.png"),
    'alchemy_g': pygame.image.load("images/store/alchemy_greyed.png"),
    'alchemy_buy': pygame.image.load("images/display/alchemy_buy.png"),
    'alchemy_display': pygame.image.load("images/display/alchemy_display.png")}

img_org = {
    'total_cookies': settings['count'],
    'wall_scale': pygame.transform.scale(settings['wallpaper_img'], (
        int(settings['wallpaper_img'].get_width() * 0.5), int(settings['wallpaper_img'].get_height() * 0.6))),
    'wall_top_scale': pygame.transform.scale(settings['wallpaper_top_img'], (
        int(settings['wallpaper_top_img'].get_width()*1.2), int(settings['wallpaper_top_img'].get_height())*1.2)),
    'wall_left_scale': pygame.transform.scale(settings['wallpaper_left_img'], (
        int(settings['wallpaper_left_img'].get_width()*0.52), int(settings['wallpaper_left_img'].get_height())*0.6)),
    'wall_center_scale': pygame.transform.scale(settings['wallpaper_center_img'], (
        int(settings['wallpaper_center_img'].get_width()*1.165), int(settings['wallpaper_center_img'].get_height())*1.5)),
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
    'bank_img': [settings['bank_b'], settings['bank_u'], settings['bank_g']],
    'temple_img': [settings['temple_b'], settings['temple_u'], settings['temple_g']],
    'wizard_img': [settings['wizard_b'], settings['wizard_u'], settings['wizard_g']],
    'shipment_img': [settings['shipment_b'], settings['shipment_u'], settings['shipment_g']],
    'alchemy_img': [settings['alchemy_b'], settings['alchemy_u'], settings['alchemy_g']],
    'grandma_display_images': [settings['grandma_display'], settings['grandma_buy1'], settings['grandma_buy2'],
                               settings['grandma_buy3'], settings['grandma_buy4'], settings['grandma_buy6'],
                               settings['grandma_buy7'], settings['grandma_buy8'], settings['grandma_buy9'],
                               settings['grandma_buy10'], settings['grandma_buy11'], settings['grandma_buy12'],
                               settings['grandma_buy13'], settings['grandma_buy14'], settings['grandma_buy15'],
                               settings['grandma_buy16'], settings['grandma_buy17'], settings['grandma_buy18'],
                               settings['grandma_buy19'], settings['grandma_buy20'], settings['grandma_buy21']],
    'farm_display_images': [settings['farm_display'], settings['farm_buy']],
    'mine_display_images': [settings['mine_display'], settings['mine_buy']],
    'factory_display_images': [settings['factory_display'], settings['factory_buy']],
    'bank_display_images': [settings['bank_display'], settings['bank_buy']],
    'temple_display_images': [settings['temple_display'], settings['temple_buy']],
    'wizard_display_images': [settings['wizard_display'], settings['wizard_buy']],
    'shipment_display_images': [settings['shipment_display'], settings['shipment_buy']],
    'alchemy_display_images': [settings['alchemy_display'], settings['alchemy_buy']]


}
