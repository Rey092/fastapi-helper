# -*- coding: utf-8 -*-
import unittest

from src.fastapi_helper import BaseHTTPException


class TestSimple(unittest.TestCase):
    def test_add_one(self):
        print(BaseHTTPException)
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
