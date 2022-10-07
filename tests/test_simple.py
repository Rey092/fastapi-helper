import unittest

from src.fastapi_fancy_exceptions import FancyHTTPException


class TestSimple(unittest.TestCase):

    def test_add_one(self):
        print(FancyHTTPException)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
