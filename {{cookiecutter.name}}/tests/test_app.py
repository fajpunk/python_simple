import unittest

from {{cookiecutter.name}}.app import App


class AppTest(unittest.TestCase):
    def test_some_func(self):
        app = App()
        self.assertEqual(app.some_func(), 'Woohoo!')
