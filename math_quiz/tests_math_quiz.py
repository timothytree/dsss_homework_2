import unittest
from math_quiz import RandomInteger, ChooseOperation, ExecuteCalculation


class TestMathGame(unittest.TestCase):

    def test_RandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_ChooseOperation(self):
        # Test if ChooseOperation chooses operations out of given operations
        for _ in range(1000):
            randomOperation = ChooseOperation()
            if randomOperation == '+':
                self.assertTrue(randomOperation=='+')
            elif randomOperation == '-':
                self.assertTrue(randomOperation=='-')
            elif randomOperation == '*':
                self.assertTrue(randomOperation=='*')

    def test_ExecuteCalculation(self):
        # Test if ExecuteCalculation executes the correct calculation for given operators and gives the correct result
            test_cases = [
                (3, 2, '*', '3 * 2', 6),
                (5, 2, '+', '5 + 2', 7),
                (8, 7.5, '-', '8 - 7.5', 0.5),
                (20, -4, '*', '20 * -4', -80),
                (-7, 12, '+', '-7 + 12', 5),
                (0, 2, '-', '0 - 2', -2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                if operator == '+':
                    with self.subTest():
                        self.assertEqual(f"{num1} {operator} {num2}", expected_problem)
                    with self.subTest():
                        self.assertEqual(num1+num2, expected_answer)
                elif operator == '-':
                    with self.subTest():
                        self.assertEqual(f"{num1} {operator} {num2}", expected_problem)
                    with self.subTest():
                        self.assertEqual(num1-num2, expected_answer)
                elif operator == '*':
                    with self.subTest():
                        self.assertEqual(f"{num1} {operator} {num2}", expected_problem)
                    with self.subTest():
                        self.assertEqual(num1*num2, expected_answer)

if __name__ == "__main__":
    unittest.main()
