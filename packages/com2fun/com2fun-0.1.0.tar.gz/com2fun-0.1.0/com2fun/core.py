#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect
import functools
import openai
import json

from . import utils
from . import gen_prompts


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


class SimulatedFunction:
    default_param = {
        #  "stop": [gen_prompts.INPUT_PREFIX, "\n"],
        "stop": [gen_prompts.INPUT_PREFIX.rstrip()],
    }

    def __init__(self, func):
        assert utils.is_empty_function(
            func
        ), "{func.__name__} should have empty function body, i.e. do nothing except returning None."
        self.func = func
        functools.update_wrapper(self, wrapped=func)

        self.param = {}
        self.examples = {}

    def resource_id(self):
        return (self.func.__module__, gen_prompts.func_definition(self.func, ""))

    def arg_id(self, *args, **kwargs):
        return repr((args, kwargs))

    def check_arg(self, *args, **kwargs):
        self.func(*args, **kwargs)  # should do nothing except check parameter format

    def __call__(self, *args, **kwargs):
        self.check_arg(*args, **kwargs)
        return self.invoke(*args, **kwargs)["result"]

    def invoke_read_out_method(self):
        # get return type
        sig = inspect.signature(self.func)
        return_type = sig.return_annotation
        if return_type == str:
            return gen_prompts.read_out_str
        if return_type == bool:
            return gen_prompts.read_out_bool
        return gen_prompts.read_out_struct_json

    def invoke_prompt(self, *args, **kwargs):
        prompts = []
        #  prompts += gen_prompts.intepreter_header()
        prompts += gen_prompts.func_query_format()
        prompts += gen_prompts.func_definition(self.func)
        for i in self.examples:
            prompts += gen_prompts.example(
                self.func, read_out=self.invoke_read_out_method(), **self.examples[i]
            )
        prompts += gen_prompts.query(
            self.func, args, kwargs, read_out=self.invoke_read_out_method()
        )
        prompt = "".join(prompts)
        return prompt

    def invoke(self, *args, **kwargs):
        prompt = self.invoke_prompt(*args, **kwargs)
        param = DEFAULT_PARAM
        param = {**param, **SimulatedFunction.default_param}
        if self.param is not None:
            param = {**param, **self.param}
        response = openai.Completion.create(prompt=prompt, **param)
        result_json = response["choices"][0]["text"]
        try:
            result = self.invoke_read_out_method()[2](result_json)
        except (json.JSONDecodeError, ValueError) as e:
            raise InvalidCompletionResult(
                "The completion result is not JSON serializable.",
                {
                    "prompt": prompt,
                    "param": param,
                    "response": response,
                    "result_json": result_json,
                    "error": e,
                },
            )
        return {
            "prompt": prompt,
            "param": param,
            "response": response,
            "result_json": result_json,
            "result": result,
        }

    def add_example(self, *args, **kwargs):
        self.check_arg(*args, **kwargs)

        def _add_example(result, explanation=None):
            example = {
                "args": args,
                "kwargs": kwargs,
                "result": result,
                "explanation": explanation,
            }
            i = self.arg_id(*args, **kwargs)
            if i in self.examples:
                if not self.examples[i]["result"] == result:
                    raise ValueError(
                        "The result of the example is different from the previous one. Arguments: {}, {}. Old result: {}, new result: {}.".format(
                            args, kwargs, self.examples[i]["result"], result
                        )
                    )
            else:
                self.examples[i] = example

        return _add_example

    def trial(self, *args, **kwargs):
        result_detail = self.invoke(*args, **kwargs)
        while True:
            true_result_json = utils.input_with_prefill(
                result_detail["prompt"], json.dumps(result_detail["result"], indent=2)
            )
            try:
                result = self.invoke_read_out_method()[2](true_result_json)
            except (json.JSONDecodeError, ValueError) as e:
                print("Groundtruth in bad format. {0}".format(e))
                continue
            return result

    def train(self, *args, **kwargs):
        result = self.trial(*args, **kwargs)
        self.add_example(*args, **kwargs)(result)
