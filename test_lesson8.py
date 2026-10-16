import unittest
from lesson8 import LessonDate, DivisionByZero, NotANumber, divide, numeric_inputs, Warehouse, Printer, ComplexNumber

class LessonEightTests(unittest.TestCase):
    def test_date(self):
        self.assertEqual(LessonDate.parse("29-02-2024"), LessonDate(29, 2, 2024))
        with self.assertRaises(ValueError):
            LessonDate.parse("29-02-2023")

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(DivisionByZero):
            divide(1, 0)

    def test_numbers(self):
        self.assertEqual(numeric_inputs(["2", "3.5", "stop", "4"]), [2.0, 3.5])
        with self.assertRaises(NotANumber):
            numeric_inputs(["bad"])

    def test_warehouse(self):
        w = Warehouse()
        w.receive(Printer("HP", 100, 4))
        w.dispatch("HP", 3)
        self.assertEqual(w.stock["HP"], 1)
        with self.assertRaises(ValueError):
            w.dispatch("HP", 2)

    def test_complex(self):
        a, b = ComplexNumber(1, -2), ComplexNumber(3, 4)
        self.assertEqual(a + b, ComplexNumber(4, 2))
        self.assertEqual(a * b, ComplexNumber(11, -2))

if __name__ == "__main__":
    unittest.main()
