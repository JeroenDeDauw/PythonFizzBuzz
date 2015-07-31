import unittest


def fizz_buzz(a):
    if a % 5 == 0 and a % 3 == 0:
        return 'FizzBuzz'

    if a % 3 == 0:
        return 'Fizz'

    if a % 5 == 0:
        return 'Buzz'

    return a


class TestFizzBuzz(unittest.TestCase):
    def test_given_non_divisible_number__number_is_returned(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)

    def test_var_mod_3_to_return_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")

    def test_var_mod_5_to_return_buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")

    def test_var_mod_3_and_5_to_return_fizz_buzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
