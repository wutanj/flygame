#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : alien_invasion.py
# @Date  : 2018/9/4

__author__ = 'wutanj'

# import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景配置
    ai_settings = Setting()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        gf.check_events(ai_settings, screen, ship, bullets)
        # 每次循环时都重绘屏幕
        # screen.fill(ai_setting.bg_color)
        # ship.blitme()
        ship.update()

        gf.update_bullet(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        # 让最近绘制屏幕可见
        # pygame.display.flip()


run_game()
