# pylint: disable=missing-module-docstring,missing-class-docstring,no-self-use,missing-function-docstring
import unittest

from {{cookiecutter.name}}.app import some_func


class AppTest(unittest.TestCase):
    def test_some_func(self):
        self.assertEqual(some_func(), "Woohoo!")
