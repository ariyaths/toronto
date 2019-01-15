import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_smallest_interesting_case(self):
        """zero is the smallest valid input"""
        self.assertEqual(a1.num_buses(0), 0)

    def test_smallest_case_for_one_bus(self):
        """one is the smallest valid input for which we should get a bus"""
        self.assertEqual(a1.num_buses(1), 1)

    def test_odd_lower_boundary_for_50(self):
        """forty nine is just one less than 50, it is at the boundary """
        self.assertEqual(a1.num_buses(49), 1)

    def test_threshold_of_50(self):
        """50, it is at the threshold"""
        self.assertEqual(a1.num_buses(50), 1)

    def test_odd_upper_boundary_for_50(self):
        """fifty one is just one more than 50, it is at the boundary """
        self.assertEqual(a1.num_buses(51), 2)

    def test_even_high_value(self):
        """fifty one is just one more than 50, it is at the boundary """
        self.assertEqual(a1.num_buses(4444444444), 88888889)


if __name__ == '__main__':
    unittest.main(exit=False)
