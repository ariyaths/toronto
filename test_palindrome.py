import unittest
import is_palindrome
import time

SLOW_TEST_THRESHOLD = 0.000001
# https://hackernoon.com/timing-tests-in-python-for-fun-and-profit-1663144571


class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        if elapsed > SLOW_TEST_THRESHOLD:
            print('MAX TIME TAKEN BY {} ({}s)'.format(self.id(), round(elapsed,
                                                                    5)))
        print('{} ({}s)'.format(self.id(), round(elapsed, 5)))

    def test_reverse(self):
        self.assertEqual(is_palindrome.reverse('kayak'), True)
        self.assertEqual(is_palindrome.reverse('rotator'), True)
        self.assertEqual(is_palindrome.reverse('noon'), True)
        self.assertEqual(is_palindrome.reverse('renter'), False)
        self.assertEqual(is_palindrome.reverse('redder'), True)
        self.assertEqual(is_palindrome.reverse('xerox'), False)
        self.assertEqual(is_palindrome.reverse('qwertytrewq'), True)
        self.assertEqual(is_palindrome.reverse('racecar '), True)
        self.assertEqual(is_palindrome.reverse('a'), True)
        self.assertEqual(is_palindrome.reverse(''), True)

        with self.assertRaises(TypeError):
            is_palindrome.reverse()
        with self.assertRaises(AttributeError):
            is_palindrome.reverse(20)

    def test_front_back(self):
        self.assertEqual(is_palindrome.front_back('kayak'), True)
        self.assertEqual(is_palindrome.front_back('rotator'), True)
        self.assertEqual(is_palindrome.front_back('noon'), True)
        self.assertEqual(is_palindrome.front_back('renter'), False)
        self.assertEqual(is_palindrome.front_back('redder'), True)
        self.assertEqual(is_palindrome.front_back('xerox'), False)
        self.assertEqual(is_palindrome.front_back('racecar'), True)
        self.assertEqual(is_palindrome.front_back('a'), True)
        self.assertEqual(is_palindrome.front_back(''), True)

        with self.assertRaises(TypeError):
            is_palindrome.front_back()
        with self.assertRaises(AttributeError):
            is_palindrome.front_back(20)

    def test_compare_loop(self):
        self.assertEqual(is_palindrome.compare_loop('kayak'), True)
        self.assertEqual(is_palindrome.compare_loop('rotator'), True)
        self.assertEqual(is_palindrome.compare_loop('noon'), True)
        self.assertEqual(is_palindrome.compare_loop('renter'), False)
        self.assertEqual(is_palindrome.compare_loop('redder'), True)
        self.assertEqual(is_palindrome.compare_loop('xerox'), False)
        self.assertEqual(is_palindrome.compare_loop('racecar'), True)
        self.assertEqual(is_palindrome.compare_loop('a'), True)
        self.assertEqual(is_palindrome.compare_loop(''), True)

        with self.assertRaises(TypeError):
            is_palindrome.compare_loop()
        with self.assertRaises(AttributeError):
            is_palindrome.compare_loop(20)


if __name__ == '__main__':
    unittest.main()
