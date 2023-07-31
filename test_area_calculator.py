import unittest
from circle import calculate_circle_area
from rectangle import calculate_rectangle_area

class TestAreaCalculator(unittest.TestCase):
    def test_calculate_circle_area(self):
        # Test case 1: Radius of 5
        radius_1 = 5
        expected_area_1 = 78.54
        self.assertAlmostEqual(calculate_circle_area(radius_1), expected_area_1, places=2)

        # Test case 2: Radius of 10.5
        radius_2 = 10.5
        expected_area_2 = 346.36
        self.assertAlmostEqual(calculate_circle_area(radius_2), expected_area_2, places=2)

    def test_calculate_rectangle_area(self):
        # Test case 1: Length 5 and Width 3
        length_1 = 5
        width_1 = 3
        expected_area_1 = 15
        self.assertEqual(calculate_rectangle_area(length_1, width_1), expected_area_1)

        # Test case 2: Length 8.25 and Width 4.5
        length_2 = 8.25
        width_2 = 4.5
        expected_area_2 = 37.125
        self.assertAlmostEqual(calculate_rectangle_area(length_2, width_2), expected_area_2, places=3)

if __name__ == "__main__":
    unittest.main()

