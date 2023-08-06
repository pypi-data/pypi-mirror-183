#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import gen_prompts
from .core import *


def com2fun(func):
    return SimulatedFunction(func)
