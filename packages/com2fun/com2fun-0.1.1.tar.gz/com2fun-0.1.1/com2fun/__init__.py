#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .func_def import *
from .simulated_function import *


def com2fun(func):
    func_def = to_func_def(func)
    return PythonInterpreterSF(func_def)
