# test_main.py
import unittest
from main import hello_world

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, CI/CD World!")

if __name__ == "__main__":
    unittest.main()

