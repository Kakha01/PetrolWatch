import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_sluggify_socar_euro_regular(self):
        result = utils.sluggify_fuel("Nano Euro Regular")
        self.assertEqual(result, "euro_regular")

    def test_sluggify_rompetrol_euro_diesel(self):
        result = utils.sluggify_fuel("efix Euro Diesel")
        self.assertEqual(result, "euro_diesel")

    def test_sluggify_georgian_euro_regular(self):
        result = utils.sluggify_fuel("Evro Regulari")
        self.assertEqual(result, "euro_regular")

    def test_sluggify_3(self):
        result = utils.sluggify_fuel("Hello World")
        self.assertEqual(result, None)

    def test_sluggify_euro_premium(self):
        result = utils.sluggify_fuel("Nano Evro Premiumi")
        self.assertEqual(result, "euro_premium")

    def test_sluggify_gulf_super(self):
        result = utils.sluggify_fuel("G-Force Super")
        self.assertEqual(result, "super")

    def test_extract_fuel_type_regular(self):
        result = utils.extract_fuel_type("Nano Euro Regular")
        self.assertEqual(result, "regular")

    def test_extract_fuel_grade_euro(self):
        result = utils.extract_fuel_grade("g-force evro regulari")
        self.assertEqual(result, "euro")


if __name__ == "__main__":
    unittest.main()
