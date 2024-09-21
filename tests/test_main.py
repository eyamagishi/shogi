import unittest
from shogi_module import main

class TestMain(unittest.TestCase):
    def test_main(self):
        main.main()

if __name__ == '__main__':
    unittest.main()
