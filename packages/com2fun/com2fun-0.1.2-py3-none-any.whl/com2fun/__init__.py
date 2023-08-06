#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .func_def import *
from .simulated_function import *


def com2fun(func, SF=PythonInterpreterSF):
    func_def = to_func_def(func)
    return SF(func_def)
