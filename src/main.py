#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0

import pygame as p

import consts as c
import utils as u
import runtime
import render_utils as ru
import title


# TODO: move to rendering file
def render_img_sq(img, rs: runtime.Runtime):
    for x in range(c.WIDTH_DIM):
        for y in range (c.HEIGHT_DIM):
            rs.screen.blit(img, p.Rect(c.SQ_SIZE * x, c.SQ_SIZE * y, c.SQ_SIZE, c.SQ_SIZE))


def main():
    # TODO: move to runtime.py
    p.init()
    p.font.init()
    rs = runtime.Runtime()
    p.display.set_caption(f"Bluff v{c.VERS_MAJ}.{c.VERS_MIN}.{c.VERS_PAT}{c.VERS_SUF}")
    title.title(rs)
    while rs.menu == 1:
        render_img_sq(bg, rs)
        for e in p.event.get():
            if e.type == p.QUIT: rs.menu = -1
        rs.clock.tick(c.FPS)
        p.display.flip()


if __name__ == "__main__":
    main()
