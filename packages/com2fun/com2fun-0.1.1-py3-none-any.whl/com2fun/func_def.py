#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass
import inspect
from typing import Optional, Any, Dict


@dataclass
class FunctionIntension:
    name: Optional[str]
    comments: Optional[str]
    doc: Optional[str]
    signature: Optional[inspect.Signature]
    full_source: Optional[str]


ExampleID = str


@dataclass
class InOutExample:
    args: Any
    kwargs: Any
    result: Any
    comments: Optional[str]

    def id(self) -> ExampleID:
        return repr((self.args, self.kwargs))


@dataclass
class FunctionExtension:
    examples: Dict[ExampleID, InOutExample]


@dataclass
class FunctionDefinition:
    intension: FunctionIntension
    extension: FunctionExtension


def to_func_def(func) -> FunctionDefinition:

    func_intension = FunctionIntension(
        name=func.__name__,
        comments=inspect.getcomments(func),
        doc=inspect.getdoc(func),
        signature=inspect.signature(func),
        full_source=inspect.getsource(func),
    )

    func_extension = FunctionExtension(examples={})

    return FunctionDefinition(
        intension=func_intension,
        extension=func_extension,
    )
