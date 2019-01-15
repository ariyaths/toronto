import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_smallest_interesting_case(self):
        """blank is the smallest valid input"""
        """for a zero length list k = 0"""
        self.assertEqual(a1.swap_k([], 0), [])

    def test_list_with_single_negative_value(self):
        """smallest list with negative value which should result in a replica"""
        """for a one length list k = 0"""
        self.assertEqual(a1.swap_k([-0.01], 0), [-0.01])

    def test_list_with_single_character_value(self):
        """smallest list with one character which should result in a replica"""
        """for a one length list k = 0"""
        self.assertEqual(a1.swap_k(['a'], 0), ['a'])

    def test_even_length_of_mixed_list_with_max_k(self):
        """mixed numbers and character list with length of list as even"""
        """for a eight length list max k = 4"""
        list_to_swap = [0.01, 'a', -0.02, 'b', 0, 'c', 0.10, 'd']
        k = len(list_to_swap)//2
        swapped_list = [0, 'c', 0.10, 'd', 0.01, 'a', -0.02, 'b']
        self.assertEqual(a1.swap_k(list_to_swap, k), swapped_list)

    def test_odd_length_of_mixed_list_with_max_k(self):
        """mixed numbers and character list with length of list as odd"""
        """for a nine length list max k = 4"""
        list_to_swap = [0.1, 'a', -0.2, 'b', 'middle-earth', 0, 'c', 0.1, 'd']
        k = len(list_to_swap)//2
        swapped_list = [0, 'c', 0.1, 'd', 'middle-earth', 0.1, 'a', -0.2, 'b']
        self.assertEqual(a1.swap_k(list_to_swap, k), swapped_list)

    def test_mixed_list_with_minimum_k_as_0(self):
        """mixed numbers and character list with length of list as even"""
        """for a nine length list we use k = 0"""
        list_to_swap = [0.1, 'a', -0.2, 'b', 'middle-earth', 0, 'c', 0.1, 'd']
        k = 0
        swapped_list = [0.1, 'a', -0.2, 'b', 'middle-earth', 0, 'c', 0.1, 'd']
        self.assertEqual(a1.swap_k(list_to_swap, k), swapped_list)

    def test_mixed_odd_list_with_medium_k_as_2(self):
        """mixed numbers and character list with length of list as even"""
        """for a nine length list we use k = 2"""
        list_to_swap = [0.1, 'a', -0.2, 'b', 'middle-earth', 0, 'c', 0.1, 'd']
        k = 2
        swapped_list = [0.1, 'd', -0.2, 'b', 'middle-earth', 0, 'c', 0.1, 'a']
        self.assertEqual(a1.swap_k(list_to_swap, k), swapped_list)

    def test_mixed_even_list_with_medium_k_as_3(self):
        """mixed numbers and character list with length of list as even"""
        """for a eight length list we use k = 3"""
        list_to_swap = [0.1, 'a', -0.2, 'b', 0, 'c', 0.1, 'd']
        k = 3
        swapped_list = ['c', 0.1, 'd', 'b', 0, 0.1, 'a', -0.2]
        self.assertEqual(a1.swap_k(list_to_swap, k), swapped_list)


if __name__ == '__main__':
    unittest.main(exit=False)
