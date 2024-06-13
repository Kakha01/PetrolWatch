import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_sluggify_socar_euro_regular(self):
        fuel = "Nano Euro Regular"
        expected = "euro_regular"
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)

    def test_sluggify_rompetrol_euro_diesel(self):
        fuel = "efix Euro Diesel"
        expected = "euro_diesel"
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)

    def test_sluggify_georgian_euro_regular(self):
        fuel = "Evro Regulari"
        expected = "euro_regular"
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)

    def test_sluggify_3(self):
        fuel = "Hello World"
        expected = None
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)
    
    def test_sluggify_euro_premium(self):
        fuel = "Nano Evro Premiumi"
        expected = "euro_premium"
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)
    
    def test_sluggify_gulf_super(self):
        fuel = "G-Force Super"
        expected = "super"
        result = Utils.sluggify_fuel(fuel)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()