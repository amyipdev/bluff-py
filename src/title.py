#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0

import pygame as p

import consts as c
import utils as u
import runtime
import render_utils as ru

TITLE_SETUP = False
TOP_BUTTON_SET = False
LARGEST_SURFACE_WIDTH = 0
LARGEST_SURFACE_HEIGHT = 0

bg_img = p.image.load(f"{u.find_assets()}/pat.jpg")
bg = None


class TitleButton:
    def __init__(self, name: str, offset: float, rs):
        global TOP_BUTTON_SET
        global LARGEST_SURFACE_WIDTH
        global LARGEST_SURFACE_HEIGHT
        self.text = rs.fonts["title_button"].render(name, True, (0x33,0x33,0x33))
        self.textbox = self.text.get_rect()
        self.textbox.center = (c.WINDOW_WIDTH >> 1, c.WINDOW_HEIGHT // 9 * offset)
        if TOP_BUTTON_SET:
            self.surface = p.Surface((LARGEST_SURFACE_WIDTH, LARGEST_SURFACE_HEIGHT))
        else:
            self.surface = p.Surface((LARGEST_SURFACE_WIDTH := int(self.text.get_width() * 1.2),
                                      LARGEST_SURFACE_HEIGHT := int(self.text.get_height() * 1.2)))
            TOP_BUTTON_SET = True
        self.surface.fill((0xaa,0xaa,0xaa))
        self.surfbox = self.surface.get_rect()
        p.draw.rect(self.surface, (0x0,0x0,0x0), self.surfbox, 5)
        self.surfbox.center = self.textbox.center
        self.hover = False


    def reset_color(self, color: tuple[int, int, int]):
        self.surface.fill(color)
        self.surfbox = self.surface.get_rect()
        p.draw.rect(self.surface, (0x0,0x0,0x0), self.surfbox, 5)
        self.surfbox.center = self.textbox.center


def setup_title(rs: runtime.Runtime):
    rs.fonts["title_main"] = p.font.Font(f"{u.find_assets()}/LEMONMILK-Medium.otf",
                                         c.SMALLER_DIM // 5)
    rs.fonts["title_button"] = p.font.Font(f"{u.find_assets()}/coolvetica rg.otf",
                                           c.SMALLER_DIM // 12)


def title(rs: runtime.Runtime):
    global TITLE_SETUP
    if not TITLE_SETUP:
        TITLE_SETUP = True
        setup_title(rs)
    title_r = rs.fonts["title_main"].render("BLUFF", True, (0x0,0x0,0x0))
    title_b = title_r.get_rect()
    title_b.center = (c.WINDOW_WIDTH >> 1, c.WINDOW_HEIGHT // 6)
    bg = p.transform.scale(bg_img, (c.SQ_SIZE, c.SQ_SIZE))
    buttons = (TitleButton("Join Game", 4, rs),
               TitleButton("Options", 5.5, rs),
               TitleButton("Credits", 7, rs))
    while rs.menu == 0:
        ru.render_img_sq(bg, rs)
        rs.screen.blit(title_r, title_b)
        for b in buttons:
            if b.hover:
                b.reset_color((0x8a,0xad,0xba))
            else:
                b.reset_color((0xaa,0xaa,0xaa))
            rs.screen.blit(b.surface, b.surfbox)
            rs.screen.blit(b.text, b.textbox)
        for e in p.event.get():
            if e.type == p.QUIT:
                rs.menu = -1
            # TODO: turn into a general button engine
            elif e.type == p.MOUSEMOTION:
                for b in buttons:
                    tl = b.surfbox.topleft
                    br = b.surfbox.bottomright
                    if u.bounds_check(tl[0], tl[1],
                                      br[0], br[1],
                                      e.pos[0], e.pos[1]):
                        b.hover = True
                    else:
                        b.hover = False
        rs.clock.tick(c.FPS)
        p.display.flip()
