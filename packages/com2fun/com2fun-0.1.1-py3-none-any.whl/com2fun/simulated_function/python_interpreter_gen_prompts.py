#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import namedtuple
import ast

INPUT_PREFIX = ">>> "
INDENT_REGEX = re.compile(r"^\s*")


def intepreter_header():
    return [
        "Python 3.10.8 (main, Nov 24 2022, 14:13:03) [GCC 11.2.0] on linux\n"
        'Type "help", "copyright", "credits" or "license" for more information.\n'
    ]


def func_query_format():
    return [INPUT_PREFIX + "1\n", "1\n"]
    #  return [INPUT_PREFIX + "print(json.dumps(['1']))\n", '["1"]\n']


def func_definition(func_def, input_prefix=INPUT_PREFIX):
    prompts = []

    if func_def.intension.comments is not None:
        prompts += [
            input_prefix + l
            for l in func_def.intension.comments.splitlines(keepends=True)
        ]
    prompts += [
        input_prefix + l
        for l in func_def.intension.full_source.splitlines(keepends=True)
        if l not in ["@com2fun.com2fun\n", "@com2fun\n", "@SimulatedFunction"]
    ]
    prompts.append(
        input_prefix
        + INDENT_REGEX.match(prompts[-1][len(input_prefix) :]).group()
        #  + "[...Implementation Omitted...]\n"
        + f"_{func_def.intension.name}(*locals())\n"  # TODO
    )
    prompts.append(input_prefix + "\n")
    return prompts


def invoke(func_def, args, kwargs):
    return (
        func_def.intension.name
        + "("
        + ", ".join(
            [repr(arg) for arg in args]
            + [repr(k) + "=" + repr(v) for k, v in kwargs.items()]
        )
        + ")"
    )


ReadOut = namedtuple("ReadOut", ["cmd", "serialize", "deserialize"])
read_out_str = ReadOut(
    lambda invoke_str: [
        INPUT_PREFIX + "print(" + invoke_str + ")\n",
    ],
    lambda x: x,
    lambda x: x,
)


def _bool_parse(x):
    x = x.strip()
    if x in ["True", "False"]:
        return x == "True"
    else:
        raise ValueError("Invalid boolean value: {}".format(x))


read_out_bool = ReadOut(
    lambda invoke_str: [
        INPUT_PREFIX + "print(" + invoke_str + ")\n",
    ],
    lambda x: str(x),
    _bool_parse,
)
#  read_out_struct_json = ReadOut(
#      lambda invoke_str: [
#          INPUT_PREFIX + "print(json.dumps(" + invoke_str + ", ensure_ascii=False))\n",
#      ],
#      lambda x: json.dumps(x, ensure_ascii=False),
#      lambda x: json.loads(x),
#  )
read_out_struct_eval = ReadOut(
    lambda invoke_str: [
        INPUT_PREFIX + invoke_str + "\n",
    ],
    lambda x: repr(x),
    lambda x: ast.literal_eval(x),
)


def query(func_def, args, kwargs, read_out=read_out_struct_eval):
    return read_out[0](invoke(func_def, args, kwargs))


def example(
    func_def, args, kwargs, result, comments=None, read_out=read_out_struct_eval
):
    prompts = []
    if comments is not None:
        prompts += [INPUT_PREFIX + "# " + l for l in comments.splitlines(keepends=True)]
        if prompts[-1][-1] != "\n":
            prompts[-1] += "\n"
    prompts += read_out[0](invoke(func_def, args, kwargs))
    prompts.append(
        read_out[1](result) + "\n",
    )
    return prompts
