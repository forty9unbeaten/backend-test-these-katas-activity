import unittest
from katas import add, multiply, power, factorial, fibonacci


class TestKatas(unittest.TestCase):
    def test_add(self):
        TestKatas.assertEqual(self, add(3, 4), 7, msg='Addition function FAIL')
        TestKatas.assertEqual(self, add(20, 4), 24,
                              msg='Addition function FAIL')
        TestKatas.assertEqual(self, add(-7, 3), -4,
                              msg='Addition function FAIL')

    def test_multiply(self):
        TestKatas.assertEqual(self, multiply(6, 3), 18,
                              msg='Multiply function FAIL')
        TestKatas.assertEqual(self, multiply(-4, -9), 36,
                              msg='Multiply function FAIL')
        TestKatas.assertEqual(self, multiply(-6, 7), -42,
                              msg='Multiply function FAIL')

    def test_power(self):
        TestKatas.assertEqual(self, power(4, 6), 4096,
                              msg='Power function FAIL')
        TestKatas.assertEqual(self, power(-6, 3), -216,
                              msg='Power function FAIL')
        TestKatas.assertEqual(self, power(
            12, 12), 8916100448256, msg='Power function FAIL')

    def test_factorial(self):
        TestKatas.assertEqual(self, factorial(
            6), 720, msg='Factorial function FAIL')
        TestKatas.assertEqual(self, factorial(12), 479001600,
                              msg='Factorial function FAIL')
        TestKatas.assertEqual(self, factorial(
            1), 1, msg='Factorial function FAIL')

    def test_fibonacci(self):
        TestKatas.assertEqual(self, fibonacci(
            3), 1, msg='Fibonacci function FAIL')
        TestKatas.assertEqual(self, fibonacci(
            10), 34, msg='Fibonacci function FAIL')
        TestKatas.assertEqual(self, fibonacci(
            1), 0, msg='Fibonacci function FAIL')


if __name__ == '__main__':
    unittest.main()
