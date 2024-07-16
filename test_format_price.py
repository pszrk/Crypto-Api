import unittest
import format_price as fp

class TestFormatPrice(unittest.TestCase):
    def test_price_above_1000(self):
        self.assertEqual(fp.format(1234.5678), "1235")

    def test_price_between_1_and_1000(self):
        self.assertEqual(fp.format(56.789), "56.79")

    def test_price_below_1(self):
        self.assertEqual(fp.format(0.123456), "0.1235")

    def test_invalid_price(self):
        self.assertEqual(fp.format("not a number"), "not a number")

if __name__ == "__main__":
    unittest.main()