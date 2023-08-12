# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import multilogue.utilities.chatgpt as chatgpt
from dataclasses import dataclass


@dataclass
class Hypothesis:
    prompt: str = ""
    suffix: str = ""
    hypothesis: str = ""
