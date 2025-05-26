import pygame
from upgradeItem import UpgradeItem

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
    'right_top': 100,
    'store_size': 73,
    'header_font': "georgia",
    'sub_font': 'arial',
    'index': 1,
    'scroll_y': 0,
    'scroll_y_center': 0,
    'scroll_cookies': 0,
    'scrollable': False,
    'scrollable_display': False,

    # Colors
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'grey': (65,65,65),
    'green': (0, 200, 0),
    'red': (174, 0, 0),

    # Values and Cost

    'tab': "DEFAULT",
    'count': 0,
    'bg_cookies': 100,
    'multiplier': 1.15,
    'auto_click_persec': 0,  # auto click
    'manual_click_current': 1,  # manual click
    'global_bought': 0,
    'cursor_prices': [15, 0.1, 0],
    'grandma_prices': [100, 1, 0],
    'farm_prices': [1100, 8, 0],
    'mine_prices': [12000, 47, 0],
    'factory_prices': [130000, 260, 0],
    'bank_prices': [1400000, 1400, 0],
    'temple_prices': [20000000, 7800, 0],
    'wizard_prices': [330000000, 44000, 0],
    'shipment_prices': [5100000000, 260000, 0],
    'alchemy_prices': [75000000000, 1600000, 0],

    # Images
    'cookie_img': pygame.image.load("images/Cookie!!!.png"),
    'wallpaper_img': pygame.image.load("images/Wallpaper.jpg"),
    'wallpaper_top_img': pygame.image.load("images/wallpaper_top.png"),
    'wallpaper_left_img': pygame.image.load("images/wallpaper_left.png"),
    'divider': pygame.image.load("images/divider.png"),
    'divider_h': pygame.image.load("images/horizontal.png"),
    'stats_greyed': pygame.image.load("images/stats.png"),
    'stats_hover': pygame.image.load("images/stats_hover.png"),
    'default_img': pygame.image.load("images/default.png"),
    #########upgrades#########
    'upgrade_b': pygame.image.load("images/upgrades/upgrade_b.png"),
    'upgrade_h': pygame.image.load("images/upgrades/upgrade_h.png"),
    'upgrade_u': pygame.image.load("images/upgrades/upgrade_u.png"),
    'finger0': pygame.image.load("images/upgrades/finger0.png"),
    'finger1': pygame.image.load("images/upgrades/finger1.png"),
    'finger2': pygame.image.load("images/upgrades/finger2.png"),
    'finger3': pygame.image.load("images/upgrades/finger3.png"),
    'finger4': pygame.image.load("images/upgrades/finger4.png"),
    'finger5': pygame.image.load("images/upgrades/finger5.png"),
    'rolling0': pygame.image.load("images/upgrades/rolling_0.png"),
    'rolling1': pygame.image.load("images/upgrades/rolling_1.png"),
    'rolling2': pygame.image.load("images/upgrades/rolling_2.png"),
    'rolling3': pygame.image.load("images/upgrades/rolling_3.png"),
    'rolling4': pygame.image.load("images/upgrades/rolling_4.png"),
    'spout0': pygame.image.load("images/upgrades/spout0.png"),
    'spout1': pygame.image.load("images/upgrades/spout1.png"),
    'spout2': pygame.image.load("images/upgrades/spout2.png"),
    'spout3': pygame.image.load("images/upgrades/spout3.png"),
    'spout4': pygame.image.load("images/upgrades/spout4.png"),
    'axe0': pygame.image.load("images/upgrades/axe0.png"),
    'axe1': pygame.image.load("images/upgrades/axe1.png"),
    'axe2': pygame.image.load("images/upgrades/axe2.png"),
    'axe3': pygame.image.load("images/upgrades/axe3.png"),
    'axe4': pygame.image.load("images/upgrades/axe4.png"),
    'grandma_types': pygame.image.load("images/upgrades/grandma_types.png"),
    'finger_index': 0,
    'rolling_index': 0,
    'spout_index': 0,
    'axe_index': 0,
    'upgrade_unlock': [1,10,25,50,100],
    'flavored_unlocked': [50000, 250000, 500000, 2500000, 5000000,
                          5000000, 5000000, 5000000, 5000000, 5000000],
    "finger0_effects": ["cursor", "efficient"], # efficient is always x2
    "finger1_effects": ["cursor", "efficient"], # efficient is always x2
    "finger2_effects": ["cursor", "efficient"], # efficient is always x2
    "finger3_effects": ["cursor", "plus_non_cursor"], # +.1 for all non-cursor owned
    "finger4_effects": ["cursor", "thousand", 5], # efficient is always x2
    "finger5_effects": ["cursor", "thousand", 10], # efficient is always x2
    'rolling_effects': ["grandma", "efficient"],
    'spout_effects': ["farm", "efficient"],
    'axe_effects': ["mine", "efficient"],
    "grandma_farm_effects": ["grandma", "cps", "farm", 1],
    "grandma_mine_effects": ["grandma", "cps", "mine", 2],
    "grandma_factory_effects": ["grandma", "cps", "factory", 3],
    "grandma_bank_effects": ["grandma", "cps", "bank", 4],
    "grandma_temple_effects": ["grandma", "cps", "temple", 5],
    "grandma_wizard_effects": ["grandma", "cps", "wizard", 6],
    "grandma_shipment_effects": ["grandma", "cps", "shipment", 7],
    "grandma_alchemy_effects": ["grandma", "cps", "alchemy", 8],
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
    'alchemy_display': pygame.image.load("images/display/alchemy_display.png")
}

img_org = {
    'total_cookies': settings['count'],
    'wall_scale': pygame.transform.scale(settings['wallpaper_img'], (
        int(settings['wallpaper_img'].get_width() * 0.5), int(settings['wallpaper_img'].get_height() * 0.6))),
    'wall_top_scale': pygame.transform.scale(settings['wallpaper_top_img'], (
        int(settings['wallpaper_top_img'].get_width()*1.2), int(settings['wallpaper_top_img'].get_height())*1.2)),
    'wall_left_scale': pygame.transform.scale(settings['wallpaper_left_img'], (
        int(settings['wallpaper_left_img'].get_width()*0.52), int(settings['wallpaper_left_img'].get_height())*0.6)),
    'divider_scale': pygame.transform.scale(settings['divider'], (
        int(settings['divider'].get_width() * 0.5), int(settings['divider'].get_height() * 0.6))),
    'divider_h_scale' : pygame.transform.scale(settings['divider_h'],
    (int(settings['divider_h'].get_width() * 0.8), int(settings['divider_h'].get_height() * 0.8))),
    'stats_images': [settings['stats_greyed'], settings['stats_hover']],
    'default_images': [settings['default_img'], settings['default_img']],
    'upgrade_bg_images': [settings['upgrade_b'], settings['upgrade_u'], settings['upgrade_h']],
    'upgrades_list': [],



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
                               settings['grandma_buy3'], settings['grandma_buy4'], settings['grandma_buy5'], settings['grandma_buy6'],
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

finger0 = UpgradeItem(settings['finger0'], 1, "cursor",
                           100, settings["finger0_effects"], .75)
finger1 = UpgradeItem(settings['finger1'], 1, "cursor",
                           500, settings["finger1_effects"], 1.20)
finger2 = UpgradeItem(settings['finger2'], 10, "cursor",
                           10000, settings["finger2_effects"], 1.20)
finger3 = UpgradeItem(settings['finger3'], 25, "cursor",
                           100000, settings["finger3_effects"], 1.20)
finger4 = UpgradeItem(settings['finger4'], 50, "cursor",
                           10000000, settings["finger4_effects"], 1.20)
finger5 = UpgradeItem(settings['finger5'], 100, "cursor",
                           100000000, settings["finger5_effects"], 1.20)

rolling0 = UpgradeItem(settings['rolling0'], 1, "grandma",
                           1000, settings["rolling_effects"], 1.20)
rolling1 = UpgradeItem(settings['rolling1'], 10, "grandma",
                           5000, settings["rolling_effects"], 1.20)
rolling2 = UpgradeItem(settings['rolling2'], 25, "grandma",
                           50000, settings["rolling_effects"], 1.20)
rolling3 = UpgradeItem(settings['rolling3'], 50, "grandma",
                           5000000, settings["rolling_effects"], 1.20)
rolling4 = UpgradeItem(settings['rolling4'], 100, "grandma",
                           500000000, settings["rolling_effects"], 1.20)

spout0 = UpgradeItem(settings['spout0'], 1, "farm",
                           11000, settings["spout_effects"], 1.20)
spout1 = UpgradeItem(settings['spout1'], 10, "farm",
                           55000, settings["spout_effects"], 1.20)
spout2 = UpgradeItem(settings['spout2'], 25, "farm",
                           550000, settings["spout_effects"], 1.20)
spout3 = UpgradeItem(settings['spout3'], 50, "farm",
                           55000000, settings["spout_effects"], 1.20)
spout4 = UpgradeItem(settings['spout4'], 100, "farm",
                           5500000000, settings["spout_effects"], 1.20)

axe0 = UpgradeItem(settings['axe0'], 1, "farm",
                           120000, settings["axe_effects"], 1.20)
axe1 = UpgradeItem(settings['axe1'], 10, "farm",
                           600000, settings["axe_effects"], 1.20)
axe2 = UpgradeItem(settings['axe2'], 25, "farm",
                           6000000, settings["axe_effects"], 1.20)
axe3 = UpgradeItem(settings['axe3'], 50, "farm",
                           60000000, settings["axe_effects"], 1.20)
axe4 = UpgradeItem(settings['axe4'], 100, "farm",
                           60000000000, settings["axe_effects"], 1.20)

grandma_farm = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           55000, settings["grandma_farm_effects"], 1.20)
grandma_mine = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           600000, settings["grandma_mine_effects"], 1.20)
grandma_factory = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           6500000, settings["grandma_factory_effects"], 1.20)
grandma_bank = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           70000000, settings["grandma_bank_effects"], 1.20)
grandma_temple = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           1000000000, settings["grandma_temple_effects"], 1.20)
grandma_wizard = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           16000000000, settings["grandma_wizard_effects"], 1.20)
grandma_shipment = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           255000000000, settings["grandma_shipment_effects"], 1.20)
grandma_alchemy = UpgradeItem(settings['grandma_types'], 15, "grandma",
                           3750000000000, settings["grandma_alchemy_effects"], 1.20)

upgrade = {
    'finger0': finger0,
    'finger1': finger1,
    'finger2': finger2,
    'finger3': finger3,
    'finger4': finger4,
    'finger5': finger5,
    'rolling0': rolling0,
    'rolling1': rolling1,
    'rolling2': rolling2,
    'rolling3': rolling3,
    'rolling4': rolling4,
    'spout0': spout0,
    'spout1': spout1,
    'spout2': spout2,
    'spout3': spout3,
    'spout4': spout4,
    'axe0': axe0,
    'axe1': axe1,
    'axe2': axe2,
    'axe3': axe3,
    'axe4': axe4,
    'grandma_farm': grandma_farm,
    'grandma_mine': grandma_mine,
    'grandma_factory': grandma_factory,
    'grandma_bank': grandma_bank,
    'grandma_temple': grandma_temple,
    'grandma_wizard': grandma_wizard,
    'grandma_shipment': grandma_shipment,
    'grandma_alchemy': grandma_alchemy
}

