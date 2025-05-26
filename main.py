import string
from typing import Final
import pygame
import random

from image import Image
from solid import Solid
from text import Text
from tab import Tab
from store import Store, number_exchange
from particles import Particle
from display import Display
from settings import settings, img_org, upgrade
from cursor import Cursor
from upgrades import Upgrades

pygame.init()
clock = pygame.time.Clock()  # The clock tracks how fast the game is running.
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

topscreen = pygame.surface.Surface((screen_width, screen_height), pygame.SRCALPHA, 32)
topscreen = topscreen.convert_alpha()

scrollscreen = pygame.surface.Surface((screen_width, screen_height+200), pygame.SRCALPHA, 32)
scrollscreen = scrollscreen.convert_alpha()
scrollscreen_display = pygame.surface.Surface((screen_width, screen_height+200), pygame.SRCALPHA, 32)
scrollscreen_display = scrollscreen_display.convert_alpha()


cookie_particle_group = pygame.sprite.Group()
cookie_rain_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()
cookie_bg_group = pygame.sprite.Group()


'''OBJECTS'''
'''Cookie Clicker Screen'''
cookie = Image(settings['left_width'] / 2, screen_height - 300, 0.15, settings['cookie_img'], topscreen)
left_column_text_box = Solid(topscreen, settings['black'], 100, settings['left_width'], settings['center_top'], 0, 30)
right_column_upgrades = Solid(topscreen, settings['grey'],0, settings['right_width'], settings['right_top'], settings['left_width'] + settings['center_width'], 0)
cookie_count_text = Text(topscreen, settings['header_font'], 18, settings['white'], settings['left_width'] / 2, 35)
auto_text = Text(topscreen, settings['header_font'], 12, settings['white'], settings['left_width'] / 2, 60)

# cursor_click = Cursor(Vector2(left_width, screen_height-100)//2, 270, cursor_buy, .3)

'''Cookie Display Screen'''
stats_display = Solid(scrollscreen, settings['black'], 200, settings['center_width'], screen_height - 50, settings['left_width'], settings['center_top'])
stats_text = Text(scrollscreen, settings['header_font'], 14, settings['white'], settings['left_width'], settings['center_top'])
stats_tab = Tab(topscreen, img_org['stats_images'], .25, settings['left_width'], settings['center_top'] - 3)
default_tab = Tab(topscreen, img_org['default_images'], 1, settings['left_width'], 0)

'''Cookie Store Screen'''
cursor = Store(scrollscreen, img_org['cursor_img'], settings['cursor_prices'], settings['multiplier'], True, settings['storeScale'], settings['header_font'],
               settings['left_width'] + settings['center_width'], settings['right_top'])


grandma = Store(scrollscreen, img_org['grandma_img'], settings['grandma_prices'], settings['multiplier'], True, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + settings['storeOptionHeight'])
grandma_bg = Display(scrollscreen_display, img_org['grandma_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'], 1, True)


farm = Store(scrollscreen, img_org['farm_img'], settings['farm_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
             settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 2))
farm_bg = Display(scrollscreen_display, img_org['farm_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'] + settings['store_display_height'], 2, False)


mine = Store(scrollscreen, img_org['mine_img'], settings['mine_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
             settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 3))
mine_bg = Display(scrollscreen_display, img_org['mine_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'] + (settings['store_display_height'] * 2), 3, False)


factory = Store(scrollscreen, img_org['factory_img'], settings['factory_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 4))
factory_bg = Display(scrollscreen_display, img_org['factory_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 3), 4, False)

bank = Store(scrollscreen, img_org['bank_img'], settings['bank_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 5))
bank_bg = Display(scrollscreen_display, img_org['bank_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 4), 5, False)

temple = Store(scrollscreen, img_org['temple_img'], settings['temple_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 6))
temple_bg = Display(scrollscreen_display, img_org['temple_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 5), 6, False)

wizard = Store(scrollscreen, img_org['wizard_img'], settings['wizard_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 7))
wizard_bg = Display(scrollscreen_display, img_org['wizard_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 6), 7, False)

shipment = Store(scrollscreen, img_org['shipment_img'], settings['shipment_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 8))
shipment_bg = Display(scrollscreen_display, img_org['shipment_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 7), 8, False)

alchemy = Store(scrollscreen, img_org['alchemy_img'], settings['alchemy_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['right_top'] + (settings['storeOptionHeight'] * 9))
alchemy_bg = Display(scrollscreen_display, img_org['alchemy_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 8), 9, False)

cursor_y: Final = cursor.rect.y
grandma_y: Final = grandma.rect.y
farm_y: Final = farm.rect.y
mine_y: Final = mine.rect.y
factory_y: Final = factory.rect.y
bank_y: Final = bank.rect.y
temple_y: Final = temple.rect.y
wizard_y: Final = wizard.rect.y
shipment_y: Final = shipment.rect.y
alchemy_y: Final = alchemy.rect.y

def appendList(obj):
    img_org['upgrades_list'].append(
        Upgrades(topscreen, upgrade[obj], 1, screen_width - settings["right_width"], settings["center_top"]))

def upgrade_effect(effects):
    match effects[0]:
        case "cursor":
            if effects[1] == "efficient":
                settings['manual_click_current'] *= 2
            elif effects[1] == "plus_non_cursor":
                total = settings['global_bought'] - settings["cursor_prices"][2]
                settings['manual_click_current'] += (0.1 * total)
                settings['cursor_prices'][1] += (0.1 * total)
            elif effects[1] == "thousand":
                add = (settings['cursor_prices'][1]/1000) * int(effects[2])
                settings['manual_click_current'] += add
                settings['cursor_prices'][1] += add
        case "grandma":
            if effects[1] == "cps":
                settings['grandma_prices'][1] *= 2
                settings[str(effects[2]) + '_prices'][1] += (settings['auto_click_persec'] / (100/effects[3])) * settings['grandma_prices'][2]
    if effects[1] == "efficient":
        settings[effects[0]+'_prices'][1] *= 2

def updateY():
    cursor.rect.y = (cursor_y + settings["scroll_y"])
    grandma.rect.y = (grandma_y + settings["scroll_y"])
    farm.rect.y = (farm_y + settings["scroll_y"])
    mine.rect.y = (mine_y + settings["scroll_y"])
    factory.rect.y = (factory_y + settings["scroll_y"])
    bank.rect.y = (bank_y + settings["scroll_y"])
    temple.rect.y = (temple_y + settings["scroll_y"])
    wizard.rect.y = (wizard_y + settings["scroll_y"])
    shipment.rect.y = (shipment_y + settings["scroll_y"])
    alchemy.rect.y = (alchemy_y + settings["scroll_y"])

def draw_stats():
    stats_display.draw()
    stats_text.draw_stats(settings['count'], img_org['total_cookies'], settings['auto_click_persec'])

def draw_default():
    grandma_bg.draw(settings['grandma_prices'][2], 3)
    farm_bg.draw(settings['farm_prices'][2], 2)
    mine_bg.draw(settings['mine_prices'][2], 2)
    factory_bg.draw(settings['factory_prices'][2], 1)
    bank_bg.draw(settings['bank_prices'][2], 1)
    temple_bg.draw(settings['temple_prices'][2], 2)
    wizard_bg.draw(settings['wizard_prices'][2], 2)
    shipment_bg.draw(settings['shipment_prices'][2], 1)
    alchemy_bg.draw(settings['alchemy_prices'][2], 2)
    screen.blit(scrollscreen_display,
                (0, settings["scroll_y_center"]))

def drawBg():
    screen.blit(img_org['wall_scale'], (0, 0))

    drawCookieClickerSection()
    drawStore()

    stats_tab.draw()
    default_tab.draw()
    if settings['tab'].upper() == "STATS":
        draw_stats()
    elif settings['tab'].upper() == "DEFAULT":
        draw_default()
    topscreen.fill((0,0,0), (screen_width - settings["right_width"], settings["center_top"], 200, 50))
    drawUpgrades()

    drawDividers()

def drawDividers():
    topscreen.blit(img_org['divider_h_scale'], (settings['left_width'], settings['center_top'] - 5))
    topscreen.blit(img_org['divider_h_scale'], (settings['left_width'] + settings['center_width'], settings['center_top'] - 5))
    topscreen.blit(img_org['divider_h_scale'], (settings['left_width'] + settings['center_width'], settings['right_top']-2))
    topscreen.blit(img_org['divider_scale'], (settings['left_width'] - 5, 0))
    topscreen.blit(img_org['divider_scale'], (settings['left_width'] + settings['center_width'] - 5, 0))

def drawCookieClickerSection():
    topscreen.blit(img_org['wall_top_scale'], (0, 0))
    topscreen.blit(img_org['wall_left_scale'], (0, 0))
    cookie_bg_group.draw(topscreen)
    cookie_bg_group.update(dt)
    left_column_text_box.draw()
    cookie_rain_group.draw(topscreen)
    cookie.draw()
    cookie_particle_group.draw(topscreen)
    if settings['auto_click_persec'] > 100:
        auto_text.draw_text("per second: " + number_exchange(settings['auto_click_persec'], 3))
        cookie_count_text.draw_text(number_exchange(settings['count'], 3) + " cookies")
    else:
        auto_text.draw_text("per second: " + str(round(settings['auto_click_persec'],3)))
        cookie_count_text.draw_text(str(round(settings['count'], 3)) + " cookies")
    # cursor_click.draw(screen, cursor_prices[2])

def drawStore():
    screen.blit(scrollscreen,(0, settings["scroll_y"]))
    cursor.draw(settings['cursor_prices'][0], settings['count'], 0, img_org['total_cookies'])
    grandma.draw(settings['grandma_prices'][0], settings['count'], 0, img_org['total_cookies'])
    farm.draw(settings['farm_prices'][0], settings['count'], 15, img_org['total_cookies'])
    mine.draw(settings['mine_prices'][0], settings['count'], 100, img_org['total_cookies'])
    factory.draw(settings['factory_prices'][0], settings['count'], 1000, img_org['total_cookies'])
    bank.draw(settings['bank_prices'][0], settings['count'], 10000, img_org['total_cookies'])
    temple.draw(settings['temple_prices'][0], settings['count'], 100000, img_org['total_cookies'])
    wizard.draw(settings['wizard_prices'][0], settings['count'], 1000000, img_org['total_cookies'])
    shipment.draw(settings['shipment_prices'][0], settings['count'], 10000000, img_org['total_cookies'])
    alchemy.draw(settings['alchemy_prices'][0], settings['count'], 100000000, img_org['total_cookies'])

def drawUpgrades():
    right_column_upgrades.draw()
    mini = min(4, len(img_org['upgrades_list']))
    x_inc = 0
    for i in range(mini):
        img_org['upgrades_list'][i].draw(settings['count'], x_inc)
        x_inc += 50


# to increase per second
AUTO_EVENT = pygame.USEREVENT
pygame.time.set_timer(AUTO_EVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == AUTO_EVENT:
            settings['count'] += settings['auto_click_persec']
            img_org['total_cookies'] += settings['auto_click_persec']
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mini = min(4, len(img_org['upgrades_list']))
            ind = -1
            x_inc = 0
            for i in range(mini):
                if event.button == 1 and img_org['upgrades_list'][i].rect.collidepoint(pos) and settings['count'] >= img_org["upgrades_list"][i].getCost():
                    ind = i
                    settings['count'] -= img_org["upgrades_list"][ind].getCost()
                    upgrade_effect(img_org["upgrades_list"][ind].effect())
            if ind != -1:
                del img_org["upgrades_list"][ind]
            if settings['scrollable']:
                if event.button == 4 and pos[0] >= (settings['left_width'] + settings["center_width"]):
                    settings["scroll_y"] = min(settings["scroll_y"] + 15, 0)
                    updateY()
                elif event.button == 5 and pos[0] >= (settings['left_width'] + settings["center_width"]):
                    settings["scroll_y"] = max(settings["scroll_y"] - 15, -300)
                    updateY()
            if settings['scrollable_display']:
                if event.button == 4 and settings['left_width'] <= pos[0] <= screen_width - settings["right_width"]:
                    settings["scroll_y_center"] = min(settings["scroll_y_center"] + 15, 0)
                elif event.button == 5 and settings['left_width'] <= pos[0] <= screen_width - settings["right_width"]:
                    settings["scroll_y_center"] = max(settings["scroll_y_center"] - 15, -300)
            if event.button == 1 and cookie.rect.collidepoint(pos):
                settings['count'] += settings['manual_click_current']
                img_org['total_cookies'] += settings['manual_click_current']
                direction = pygame.math.Vector2(random.uniform(-.5, .5), random.uniform(-.5, -.1))
                direction.normalize()
                speed = random.randint(50, 400)
                Particle(cookie_particle_group, pos, settings['cookie_img'], .03, direction, speed)
                direction = pygame.math.Vector2(0, 1)
                direction.normalize()
                Particle(cookie_rain_group, (random.randint(0, settings['left_width']-5), -10), settings['cookie_img'], .03, direction, 1)
            elif event.button == 1 and stats_tab.rect.collidepoint(pos):
                if settings['tab'].upper() == "STATS":
                    settings['tab'] = "DEFAULT"
                else:
                    settings['tab'] = "STATS"
            elif event.button == 1 and default_tab.rect.collidepoint(pos):
                tab = "DEFAULT"
            elif event.button == 1 and cursor.rect.collidepoint(pos) and settings['count'] >= settings['cursor_prices'][0]:
                settings['global_bought']+=1
                settings['cursor_prices'][2] += 1
                settings['count'] -= settings['cursor_prices'][0]
                settings['cursor_prices'][0] = round((settings['cursor_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['cursor_prices'][1]
                if settings['finger_index'] < 5 and settings['cursor_prices'][2] == settings['upgrade_unlock'][settings['finger_index']]:
                    if settings['upgrade_unlock'][settings['finger_index']] == 1:
                        appendList("finger" + str(settings['finger_index']))
                    appendList("finger"+str(settings['finger_index']+1))
                    settings['finger_index'] += 1
            elif event.button == 1 and grandma.rect.collidepoint(pos) and settings['count'] >= settings['grandma_prices'][0]:
                settings['global_bought'] += 1
                settings['grandma_prices'][2] += 1
                temp = grandma_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['grandma_prices'][0]
                settings['grandma_prices'][0] = round((settings['grandma_prices'][0] * settings['multiplier']),3)
                settings['auto_click_persec'] += settings['grandma_prices'][1]
                grandma_bg.addToGrannie(settings['index'])
                if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                    appendList("rolling"+str(settings['rolling_index']))
                    settings['rolling_index'] += 1
            elif event.button == 1 and farm.rect.collidepoint(pos) and settings['count'] >= settings['farm_prices'][0]:
                settings['global_bought'] += 1
                settings['farm_prices'][2] += 1
                temp = farm_bg.unlock()
                settings['count'] -= settings['farm_prices'][0]
                settings['farm_prices'][0] = round((settings['farm_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['farm_prices'][1]
                if settings['spout_index'] < 5 and settings['farm_prices'][2] == settings['upgrade_unlock'][settings['spout_index']]:
                    appendList("spout"+str(settings['spout_index']))
                    settings['spout_index'] += 1
                if settings['farm_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_farm")
            elif event.button == 1 and mine.rect.collidepoint(pos) and settings['count'] >= settings['mine_prices'][0]:
                settings['global_bought'] += 1
                settings['mine_prices'][2] += 1
                temp = mine_bg.unlock()
                settings['count'] -= settings['mine_prices'][0]
                settings['mine_prices'][0] = round((settings['mine_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['mine_prices'][1]
                if settings['axe_index'] < 5 and settings['mine_prices'][2] == settings['upgrade_unlock'][settings['axe_index']]:
                    appendList("axe"+str(settings['axe_index']))
                    settings['axe_index'] += 1
                if settings['mine_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_mine")
            elif event.button == 1 and factory.rect.collidepoint(pos) and settings['count'] >= settings['factory_prices'][0]:
                settings['global_bought'] += 1
                settings['factory_prices'][2] += 1
                temp = factory_bg.unlock()
                settings['count'] -= settings['factory_prices'][0]
                settings['factory_prices'][0] = round((settings['factory_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['factory_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['factory_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_factory")
            elif event.button == 1 and bank.rect.collidepoint(pos) and settings['count'] >= settings['bank_prices'][0]:
                settings['global_bought'] += 1
                settings['bank_prices'][2] += 1
                temp = bank_bg.unlock()
                settings['count'] -= settings['bank_prices'][0]
                settings['bank_prices'][0] = round((settings['bank_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['bank_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['bank_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_bank")
            elif event.button == 1 and temple.rect.collidepoint(pos) and settings['count'] >= settings['temple_prices'][0]:
                settings['global_bought'] += 1
                settings['scrollable'] = True
                settings['temple_prices'][2] += 1
                temp = temple_bg.unlock()
                settings['count'] -= settings['temple_prices'][0]
                settings['temple_prices'][0] = round((settings['temple_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['temple_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['temple_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_temple")
            elif event.button == 1 and wizard.rect.collidepoint(pos) and settings['count'] >= settings['wizard_prices'][0]:
                settings['global_bought'] += 1
                settings['wizard_prices'][2] += 1
                settings['scrollable'] = True
                temp = wizard_bg.unlock()
                settings['count'] -= settings['wizard_prices'][0]
                settings['wizard_prices'][0] = round((settings['wizard_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['wizard_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['wizard_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    appendList("grandma_wizard")
                    settings['index'] = max(temp, settings['index'])
            elif event.button == 1 and shipment.rect.collidepoint(pos) and settings['count'] >= settings['shipment_prices'][0]:
                settings['global_bought'] += 1
                settings['shipment_prices'][2] += 1
                settings['scrollable'] = True
                settings['scrollable_display'] = True
                temp = shipment_bg.unlock()
                settings['count'] -= settings['shipment_prices'][0]
                settings['shipment_prices'][0] = round((settings['shipment_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['shipment_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['shipment_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_shipment")
            elif event.button == 1 and alchemy.rect.collidepoint(pos) and settings['count'] >= settings['alchemy_prices'][0]:
                settings['global_bought'] += 1
                settings['alchemy_prices'][2] += 1
                settings['scrollable_display'] = True
                settings['scrollable'] = True
                temp = alchemy_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['alchemy_prices'][0]
                settings['alchemy_prices'][0] = round((settings['alchemy_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['alchemy_prices'][1]
                # if settings['rolling_index'] < 5 and settings['grandma_prices'][2] == settings['upgrade_unlock'][settings['rolling_index']]:
                #     appendList("rolling"+str(settings['rolling_index']))
                #     settings['rolling_index'] += 1
                if settings['alchemy_prices'][2] == 15 and settings['grandma_prices'][2] >= 1:
                    settings['index'] = max(temp, settings['index'])
                    appendList("grandma_alchemy")
    dt = clock.tick() / 1000
    drawBg()
    cookie_rain_group.update(dt, screen_height, True)
    cookie_particle_group.update(dt, screen_height, False)
    cookie.cookieUpdate()
    screen.blit(topscreen,(0, 0))
    # if img_org['total_cookies'] >= settings['bg_cookies'] and settings['scroll_cookies'] < 50:
    #     cookie_bg_group.add(Image(random.randint(0,settings['left_width']-15), 0, random.randint(3, 7)/100, settings['cookie_img'], topscreen))
    #     settings['bg_cookies'] *= 2
    #     settings['scroll_cookies'] += 1
    # cursor_click.update(dt)
    pygame.display.update()