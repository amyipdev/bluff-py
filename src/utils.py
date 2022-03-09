#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0

import os


# Really wish there was some form of constexpr for Python.
# Obviously can not evaluate at compile time, *but* what
# if we only had to evaluate once? Would be much faster,
# saves stringops. Would be even better if paths were just
# relative to file location and not cwd...
def find_assets() -> str:
    return os.path.dirname(os.path.dirname(__file__)) + "/assets"


def bounds_check(tlx: int, tly: int, brx: int,
                 bry: int, px: int, py: int):
    return (
        px > tlx
        and py > tly
        and px < brx
        and py < bry)
