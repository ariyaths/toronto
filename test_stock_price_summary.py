import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_smallest_interesting_case(self):
        """blank is the smallest valid input"""
        self.assertEqual(a1.stock_price_summary([]), (0, 0))

    def test_list_with_single_negative_value(self):
        """smallest list which should result in a negative total"""
        price_changes = [-0.01]
        self.assertEqual(a1.stock_price_summary(price_changes), (0, -0.01))

    def test_list_with_single_positive_value(self):
        """smallest list which should result in a positive total"""
        price_changes = [0.01]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.01, 0))

    def test_even_length_of_mixed_list(self):
        """mixed positive and negative list with length of list as even"""
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.14, -0.17))

    def test_odd_length_of_mixed_list(self):
        """mixed positive and negative list with length of list as even"""
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.14, -0.16))

    def test_order_with_all_initial_negative_values(self):
        """the first four values are negative, followed by two zeros"""
        price_changes = [-0.01, -0.03, -0.02, -0.14, 0, 0, 0.10]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.10, -0.2))

    def test_order_with_all_initial_positive_values(self):
        """the first four values are positives, followed by two zeros"""
        price_changes = [0.01, 0.03, 0.02, 0.14, 0, 0, -0.10]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.2, -0.1))


if __name__ == '__main__':
    unittest.main(exit=False)
