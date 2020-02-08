import unittest
from general import main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "hello world")


if __name__ == '__main__':
    unittest.main()
