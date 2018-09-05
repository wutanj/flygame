#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : ship.py
# @Date  : 2018/9/4

__author__ = 'wutanj'

import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """
        初始化飞船并三个设置其初始位置
        :param screen:
        """
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.y = float(self.rect.y)

    def update(self):
        """
        根据移动标志调整飞船位置
        :return:
        """
        # 更新飞船的center值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
