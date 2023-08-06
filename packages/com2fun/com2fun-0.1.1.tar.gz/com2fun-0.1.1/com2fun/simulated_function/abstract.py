#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Any
import functools

from ..func_def import *

DEFAULT_PARAM = {
    "model": "text-davinci-003",
    #  "model": "code-davinci-002",
    "best_of": 1,
    "temperature": 0.0,
    "max_tokens": 2048,
    "stream": False,
}


class InvalidCompletionResult(Exception):
    def __init__(self, message, data):
        self.message = message
        self.data = data
        super().__init__(self.message)

    def __str__(self):
        return self.message + "\n" + str(self.data)


class SimulatedFunction(ABC):
    def __init__(self, func_def: FunctionDefinition):
        self.func_def = func_def
        super().__init__()

    @abstractmethod
    def invoke_prompt(self, *args, **kwargs) -> str:
        """Should return the prompt that is posted to OpenAI API"""

    @abstractmethod
    def invoke(self, *args, **kwargs) -> Dict[str, Any]:
        """Should return all details including prompt, param(eters for OpenAI API), (full) response, result"""

    def __call__(self, *args, **kwargs):
        self.check_arg(*args, **kwargs)
        return self.invoke(*args, **kwargs)["result"]

    def add_example(self, *args, **kwargs):
        self.check_arg(*args, **kwargs)
        examples = self.func_def.extension.examples

        def _add_example(examples, result, explanation=None):
            exam = InOutExample(args, kwargs, result, explanation)
            if exam.id() in examples:
                if not result == examples[exam.id()].result:
                    raise ValueError(
                        f"Example {exam.id()} already exists with different result. Old: {examples[exam.id()].result}. New: {result}"
                    )
            else:
                examples[exam.id()] = exam

        return functools.partial(_add_example, examples)

    def check_arg(self, *args, **kwargs):
        if self.func_def.intension.signature is None:
            return
        return self.func_def.intension.signature.bind(*args, **kwargs)
