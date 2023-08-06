#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
``pysilsub.types``
==================

Some types.

"""

from typing import Sequence


PrimaryInput = int | float
PrimaryWeights = Sequence[float]
PrimarySettings = Sequence[int]
DeviceInput = PrimarySettings | PrimaryWeights
PrimaryBounds = list[tuple[float, float]]
PrimaryColors = Sequence[str] | Sequence[Sequence[int | float]]