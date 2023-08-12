# -*- coding: utf-8 -*-
# Python
"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import Any
import multilogue.utilities.chatgpt as chatgpt
from dataclasses import dataclass
from config import CONFIG


@dataclass
class Hypothesis:
    prompt: str = ""
    suffix: str = ""
    hypothesis: Any = None


hypothesis_yes = Hypothesis(
    prompt="Yes,",
    suffix="That is why the answer is: yes."
)

hypothesis_no = Hypothesis(
    prompt="No,",
    suffix="That is why the answer is: no."
)

hypothesis_unknown = Hypothesis(
    prompt="It is unknown,",
    suffix="That is why the answer is: unknown."
)

hypothesis_unknowable = Hypothesis(
    prompt="It is unknowable,",
    suffix="That is why the answer is: unknowable."
)

hypotheses_list = [hypothesis_yes,
                   hypothesis_no,
                   hypothesis_unknown,
                   hypothesis_unknowable]

question = "Can human nature be changed?"
connector = " for the following reason(s):"

for hypothesis in hypotheses_list:
    prompt = f'{question} {hypothesis.prompt} {connector}'
    suffix = hypothesis.suffix
    response = chatgpt.fill_in(prompt, suffix, **CONFIG)
    hypothesis.hypothesis = response[0]['text']
