# -*- coding: utf-8 -*-

from . import helper


def get_message():
    """Get a thought."""

    return 'hello world!!!'


def say_hello():
    """Contemplation..."""

    if helper.should_speak():
        print(get_message())
