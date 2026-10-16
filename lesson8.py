"""Corrected Lesson 8: dates, exceptions, inventory and complex numbers."""
from dataclasses import dataclass
from datetime import date

class DivisionByZero(ZeroDivisionError):
    pass

class NotANumber(ValueError):
    pass

@dataclass(frozen=True)
class LessonDate:
    day: int
    month: int
    year: int

    @classmethod
    def parse(cls, value: str):
        try:
            day, month, year = map(int, value.replace(" ", "").split("-"))
            cls.validate(day, month, year)
        except (TypeError, ValueError) as exc:
            raise ValueError("Expected a real date in DD-MM-YYYY format") from exc
        return cls(day, month, year)

    @staticmethod
    def validate(day: int, month: int, year: int):
        date(year, month, day)
        return True

def divide(a: float, b: float):
    if b == 0:
        raise DivisionByZero("Cannot divide by zero")
    return a / b

def numeric_inputs(values):
    numbers = []
    for value in values:
        if value.strip().lower() == "stop":
            break
        try:
            numbers.append(float(value))
        except ValueError as exc:
            raise NotANumber(f"Not a number: {value}") from exc
    return numbers

@dataclass(frozen=True)
class Equipment:
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        if not self.name or self.price < 0 or not isinstance(self.quantity, int) or isinstance(self.quantity, bool) or self.quantity < 0:
            raise ValueError("Invalid equipment information")

class Printer(Equipment):
    pass

class Scanner(Equipment):
    pass

class Copier(Equipment):
    pass

class Warehouse:
    def __init__(self):
        self.stock = {}

    def receive(self, equipment: Equipment):
        if not isinstance(equipment, Equipment):
            raise TypeError("Expected Equipment")
        self.stock[equipment.name] = self.stock.get(equipment.name, 0) + equipment.quantity

    def dispatch(self, name: str, quantity: int):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0 or quantity > self.stock.get(name, 0):
            raise ValueError("Invalid quantity or insufficient stock")
        self.stock[name] -= quantity

@dataclass(frozen=True)
class ComplexNumber:
    real: float
    imag: float

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)
