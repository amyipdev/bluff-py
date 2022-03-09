#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0

import pygame as p

import consts as c

class Runtime:
    def __init__(self):
        self.setup()

    def setup(self, menu = 0):
        self.screen = p.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.clock = p.time.Clock()
        self.menu = menu
        # Can preload fonts or load at runtime!
        self.fonts = {}
