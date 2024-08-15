import string

import pygame
import random

from image import Image
from solid import Solid
from text import Text
from tab import Tab
from store import Store, number_exchange
from particles import Particle
from display import Display
from settings import settings, img_org
from cursor import Cursor

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
scroll_rect = scrollscreen.get_rect()
x1 = scroll_rect[0]
x2 = x1 + scroll_rect[2]
a, b = (255, 0, 0), (60, 255, 120)
y1 = scroll_rect[1]
y2 = y1 + scroll_rect[3]
h = y2-y1
rate = (float((b[0]-a[0])/h),
         (float(b[1]-a[1])/h),
         (float(b[2]-a[2])/h)
         )




cookie_particle_group = pygame.sprite.Group()
cookie_rain_group = pygame.sprite.Group()
cursor_group = pygame.sprite.Group()

'''OBJECTS'''
'''Cookie Clicker Screen'''
cookie = Image(settings['left_width'] / 2, screen_height - 300, 0.15, settings['cookie_img'], topscreen)
left_column_text_box = Solid(topscreen, settings['black'], 100, settings['left_width'], settings['center_top'], 0, 30)
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
               settings['left_width'] + settings['center_width'], settings['center_top'])


grandma = Store(scrollscreen, img_org['grandma_img'], settings['grandma_prices'], settings['multiplier'], True, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + settings['storeOptionHeight'])
grandma_bg = Display(scrollscreen_display, img_org['grandma_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'], 1, True)


farm = Store(scrollscreen, img_org['farm_img'], settings['farm_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
             settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 2))
farm_bg = Display(scrollscreen_display, img_org['farm_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'] + settings['store_display_height'], 2, False)


mine = Store(scrollscreen, img_org['mine_img'], settings['mine_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
             settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 3))
mine_bg = Display(scrollscreen_display, img_org['mine_display_images'], img_org['divider_h_scale'], .5, settings['left_width'], settings['center_top'] + (settings['store_display_height'] * 2), 3, False)


factory = Store(scrollscreen, img_org['factory_img'], settings['factory_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 4))
factory_bg = Display(scrollscreen_display, img_org['factory_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 3), 4, False)

bank = Store(scrollscreen, img_org['bank_img'], settings['bank_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 5))
bank_bg = Display(scrollscreen_display, img_org['bank_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 4), 5, False)

temple = Store(scrollscreen, img_org['temple_img'], settings['temple_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 6))
temple_bg = Display(scrollscreen_display, img_org['temple_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 5), 6, False)

wizard = Store(scrollscreen, img_org['wizard_img'], settings['wizard_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 7))
wizard_bg = Display(scrollscreen_display, img_org['wizard_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 6), 7, False)

shipment = Store(scrollscreen, img_org['shipment_img'], settings['shipment_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 8))
shipment_bg = Display(scrollscreen_display, img_org['shipment_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 7), 8, False)

alchemy = Store(scrollscreen, img_org['alchemy_img'], settings['alchemy_prices'], settings['multiplier'], False, settings['storeScale'], settings['header_font'],
                settings['left_width'] + settings['center_width'], settings['center_top'] + (settings['storeOptionHeight'] * 9))
alchemy_bg = Display(scrollscreen_display, img_org['alchemy_display_images'], img_org['divider_h_scale'], .5, settings['left_width'],
                     settings['center_top'] + (settings['store_display_height'] * 8), 9, False)


def draw_stats():
    stats_display.draw()
    stats_text.draw_stats(settings['count'], img_org['total_cookies'], settings['auto_click_persec'])


def draw_default():
    screen.blit(img_org['wall_center_scale'], (13, -10))
    grandma_bg.draw(settings['grandma_prices'][2], 3)
    farm_bg.draw(settings['farm_prices'][2], 2)
    mine_bg.draw(settings['mine_prices'][2], 2)
    factory_bg.draw(settings['factory_prices'][2], 1)
    bank_bg.draw(settings['bank_prices'][2], 1)
    temple_bg.draw(settings['temple_prices'][2], 1)
    wizard_bg.draw(settings['wizard_prices'][2], 1)
    shipment_bg.draw(settings['shipment_prices'][2], 1)
    alchemy_bg.draw(settings['alchemy_prices'][2], 1)
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

    drawDividers()


def drawDividers():
    topscreen.blit(img_org['divider_h_scale'], (settings['left_width'], settings['center_top'] - 5))
    topscreen.blit(img_org['divider_h_scale'], (settings['left_width'] + settings['center_width'], settings['center_top'] - 5))
    topscreen.blit(img_org['divider_scale'], (settings['left_width'] - 5, 0))
    topscreen.blit(img_org['divider_scale'], (settings['left_width'] + settings['center_width'] - 5, 0))


def drawCookieClickerSection():
    topscreen.blit(img_org['wall_top_scale'], (0, 0))
    topscreen.blit(img_org['wall_left_scale'], (0, 0))
    left_column_text_box.draw()
    cookie_rain_group.draw(screen)
    cookie.draw()
    cookie_particle_group.draw(screen)
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
            if event.button == 4 and pos[0] >= (settings['right_width'] + settings["center_width"]):
                settings["scroll_y"] = min(settings["scroll_y"] + 15, 0)
            elif event.button == 5 and pos[0] >= (settings['right_width'] + settings["center_width"]):
                settings["scroll_y"] = max(settings["scroll_y"] - 15, -300)
            if event.button == 4 and pos[0] >= settings['right_width'] and pos[0] <= screen_width - settings["right_width"]:
                settings["scroll_y_center"] = min(settings["scroll_y_center"] + 15, 0)
            elif event.button == 5 and pos[0] >= settings['right_width'] and pos[0] <= screen_width - settings["right_width"]:
                settings["scroll_y_center"] = max(settings["scroll_y_center"] - 15, -300)
            elif event.button == 1 and cookie.rect.collidepoint(pos):
                settings['count'] += settings['manual_click_current']
                img_org['total_cookies'] += settings['manual_click_current']
                direction = pygame.math.Vector2(random.uniform(-.5, .5), random.uniform(-.5, -.1))
                direction.normalize()
                speed = random.randint(50, 400)
                Particle(cookie_particle_group, pos, settings['cookie_img'], .03, settings['white'], direction, speed)
                direction = pygame.math.Vector2(0, 1)
                direction.normalize()
                Particle(cookie_rain_group, (random.randint(0, settings['left_width']-5), -10), settings['cookie_img'], .03, settings['white'], direction, .5)
            elif event.button == 1 and stats_tab.rect.collidepoint(pos):
                if settings['tab'].upper() == "STATS":
                    settings['tab'] = "DEFAULT"
                else:
                    settings['tab'] = "STATS"
            elif event.button == 1 and default_tab.rect.collidepoint(pos):
                tab = "DEFAULT"
            elif event.button == 1 and cursor.rect.collidepoint(pos) and settings['count'] >= settings['cursor_prices'][0]:
                settings['cursor_prices'][2] += 1
                settings['count'] -= settings['cursor_prices'][0]
                settings['cursor_prices'][0] = round((settings['cursor_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['cursor_prices'][1]
            elif event.button == 1 and grandma.rect.collidepoint(pos) and settings['count'] >= settings['grandma_prices'][0]:
                settings['grandma_prices'][2] += 1
                temp = grandma_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['grandma_prices'][0]
                settings['grandma_prices'][0] = round((settings['grandma_prices'][0] * settings['multiplier']),3)
                settings['auto_click_persec'] += settings['grandma_prices'][1]
                grandma_bg.addToGrannie(settings['index'])
            elif event.button == 1 and farm.rect.collidepoint(pos) and settings['count'] >= settings['farm_prices'][0]:
                settings['farm_prices'][2] += 1
                temp = farm_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['farm_prices'][0]
                settings['farm_prices'][0] = round((settings['farm_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['farm_prices'][1]
            elif event.button == 1 and mine.rect.collidepoint(pos) and settings['count'] >= settings['mine_prices'][0]:
                settings['mine_prices'][2] += 1
                temp = mine_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['mine_prices'][0]
                settings['mine_prices'][0] = round((settings['mine_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['mine_prices'][1]
            elif event.button == 1 and factory.rect.collidepoint(pos) and settings['count'] >= settings['factory_prices'][0]:
                settings['factory_prices'][2] += 1
                temp = factory_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['factory_prices'][0]
                settings['factory_prices'][0] = round((settings['factory_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['factory_prices'][1]
            elif event.button == 1 and bank.rect.collidepoint(pos) and settings['count'] >= settings['bank_prices'][0]:
                settings['bank_prices'][2] += 1
                temp = bank_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['bank_prices'][0]
                settings['bank_prices'][0] = round((settings['bank_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['bank_prices'][1]
            elif event.button == 1 and temple.rect.collidepoint(pos) and settings['count'] >= settings['temple_prices'][0]:
                settings['temple_prices'][2] += 1
                temp = temple_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['temple_prices'][0]
                settings['temple_prices'][0] = round((settings['temple_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['temple_prices'][1]
            elif event.button == 1 and wizard.rect.collidepoint(pos) and settings['count'] >= settings['wizard_prices'][0]:
                settings['wizard_prices'][2] += 1
                temp = wizard_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['wizard_prices'][0]
                settings['wizard_prices'][0] = round((settings['wizard_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['wizard_prices'][1]
            elif event.button == 1 and shipment.rect.collidepoint(pos) and settings['count'] >= settings['shipment_prices'][0]:
                settings['shipment_prices'][2] += 1
                temp = shipment_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['shipment_prices'][0]
                settings['shipment_prices'][0] = round((settings['shipment_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['shipment_prices'][1]
            elif event.button == 1 and alchemy.rect.collidepoint(pos) and settings['count'] >= settings['alchemy_prices'][0]:
                settings['alchemy_prices'][2] += 1
                temp = alchemy_bg.unlock()
                settings['index'] = max(temp, settings['index'])
                settings['count'] -= settings['alchemy_prices'][0]
                settings['alchemy_prices'][0] = round((settings['alchemy_prices'][0] * settings['multiplier']))
                settings['auto_click_persec'] += settings['alchemy_prices'][1]

    dt = clock.tick() / 1000
    drawBg()
    cookie_rain_group.update(dt, settings['left_width'], screen_height, True)
    cookie_particle_group.update(dt, settings['left_width'], screen_height, False)
    cookie.cookieUpdate()

    screen.blit(topscreen,
                (0, 0))
    # cursor_click.update(dt)
    pygame.display.update()
