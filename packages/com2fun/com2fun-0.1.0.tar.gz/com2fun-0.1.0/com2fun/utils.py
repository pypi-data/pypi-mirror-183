#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_empty_function(ef):
    import dis

    instructions = list(dis.get_instructions(ef))
    if not all(
        [
            len(instructions) == 2,
            instructions[0].opcode == 100,  # LOAD_CONST
            instructions[0].argrepr == "None",
            instructions[1].opcode == 83,  # RETURN_VALUE
        ]
    ):
        return False
    return True


def input_with_prefill_linux(prompt, prefill):
    import readline

    # TODO: this remove any pre-existing startup hook the
    #       caller may have already installed. Need fix.
    readline.set_startup_hook(lambda: readline.insert_text(prefill))
    try:
        return input(prompt)
    finally:
        readline.set_startup_hook()


def input_with_prefill_jupyter(prompt, prefill):
    # fallback to ordinary input
    return input(prompt + prefill + "\n")


def is_jupyter():
    try:
        from IPython import get_ipython

        if get_ipython().__class__.__name__ in ["ZMQInteractiveShell"]:
            return True
        elif get_ipython().__class__.__name__ in [
            "NoneType",
            "TerminalInteractiveShell",
        ]:
            return False
        else:
            raise Warning("Unknown IPython shell type")
            return False
    except ImportError:
        return False


def input_with_prefill(prompt, prefill):
    # check if client is jupyter or shell(linux) or shell(macos)
    if is_jupyter():
        return input_with_prefill_jupyter(prompt, prefill)
    else:
        import sys

        if sys.platform.startswith("linux"):
            return input_with_prefill_linux(prompt, prefill)
        else:
            # fallback to ordinary input
            return input(prompt + prefill + "\n")
