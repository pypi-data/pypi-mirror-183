#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openai

from . import InvalidCompletionResult, SimulatedFunction, DEFAULT_PARAM
from . import python_interpreter_gen_prompts as gen_prompts


class PythonInterpreterSF(SimulatedFunction):
    default_param = {
        #  "stop": [gen_prompts.INPUT_PREFIX, "\n"],
        "stop": [gen_prompts.INPUT_PREFIX.rstrip()],
    }

    def __init__(self, *args, **kwargs):
        self.param = {}
        super().__init__(*args, **kwargs)

    def invoke_read_out_method(self):
        # get return type
        sig = self.func_def.intension.signature
        return_type = sig.return_annotation
        if return_type == str:
            return gen_prompts.read_out_str
        if return_type == bool:
            return gen_prompts.read_out_bool
        return gen_prompts.read_out_struct_eval

    def invoke_prompt(self, *args, **kwargs) -> str:
        prompts = []
        #  prompts += gen_prompts.intepreter_header()
        prompts += gen_prompts.func_query_format()
        prompts += gen_prompts.func_definition(self.func_def)
        for i in self.func_def.extension.examples:
            prompts += gen_prompts.example(
                self.func_def,
                read_out=self.invoke_read_out_method(),
                **self.func_def.extension.examples[i].__dict__,
            )
        prompts += gen_prompts.query(
            self.func_def, args, kwargs, read_out=self.invoke_read_out_method()
        )
        prompt = "".join(prompts)
        return prompt

    def invoke(self, *args, **kwargs):
        prompt = self.invoke_prompt(*args, **kwargs)
        param = DEFAULT_PARAM
        param = {**param, **type(self).default_param}
        if self.param is not None:
            param = {**param, **self.param}
        response = openai.Completion.create(prompt=prompt, **param)
        result_str = response["choices"][0]["text"]
        r = {
            "prompt": prompt,
            "param": param,
            "response": response,
            "result_str": result_str,
        }
        try:
            result = self.invoke_read_out_method()[2](result_str)
        except Exception as e:
            raise InvalidCompletionResult(
                "The completion result is not serializable.",
                {
                    **r,
                    "error": e,
                },
            )
        return {
            **r,
            "result": result,
        }
