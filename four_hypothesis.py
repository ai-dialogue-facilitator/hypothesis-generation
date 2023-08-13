# -*- coding: utf-8 -*-
# Python
"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List
import multilogue.utilities.chatgpt as chatgpt
from dataclasses import dataclass
from config import CONFIG


question = "Can human nature be changed?"
connector = " for the following reason(s):"


@dataclass
class Hypothesis:
    prompt: str = ""
    suffix: str = ""
    hypothesis: List[str] = None

    def __repr__(self):
        wording = '\n'.join(self.hypothesis)
        text = f"{question}\n{self.prompt}{connector}\n{wording}\n{self.suffix}"
        return text


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

for hypothesis in hypotheses_list:
    text_before = f'{question} {hypothesis.prompt} {connector}'
    response = chatgpt.fill_in(text_before=text_before, text_after=hypothesis.suffix, **CONFIG)
    hypothesis.hypothesis = [resp['text'].strip() for resp in response]
    print(hypothesis)

print("All done!")
