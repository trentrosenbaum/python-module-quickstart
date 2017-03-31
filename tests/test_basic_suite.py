# -*- coding: utf-8 -*-

from .context import sample


class TestBasicSuite:
    """Basic test cases."""

    def test_absolute_message(self):
        assert sample.get_message() == 'hello world!!!'

    def test_absolute_truth(self):
        assert True
