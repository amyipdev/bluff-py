#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0

import pygame as p

import consts as c
import runtime


def render_img_sq(img, rs: runtime.Runtime):
    for x in range(c.WIDTH_DIM):
        for y in range (c.HEIGHT_DIM):
            rs.screen.blit(img, p.Rect(c.SQ_SIZE * x, c.SQ_SIZE * y, c.SQ_SIZE, c.SQ_SIZE))
