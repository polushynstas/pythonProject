class Calculator:
    def add(self, x, y):
        try:
            result = x + y
            return result
        except Exception as e:
            print(f"Error during addition: {e}")

    def subtract(self, x, y):
        try:
            result = x - y
            return result
        except Exception as e:
            print(f"Error during subtraction: {e}")

    def multiply(self, x, y):
        try:
            result = x * y
            return result
        except Exception as e:
            print(f"Error during multiplication: {e}")

    def divide(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error during division: {e}")

    def power(self, x, y):
        try:
            if y < 0:
                raise NegativePowerError()
            result = x ** y
            return result
        except NegativePowerError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error during exponentiation: {e}")

    def square_root(self, x):
        try:
            if x < 0:
                raise ValueError("Cannot calculate square root of a negative number.")
            result = x ** 0.5
            return result
        except Exception as e:
            print(f"Error during square root calculation: {e}")


class NegativePowerError(Exception):
    def __init__(self, message="Cannot raise a number to a negative power."):
        self.message = message
        super().__init__(self.message)


calculator = Calculator()

print(calculator.add(5, 3))
print(calculator.subtract(5, 3))
print(calculator.multiply(5, 3))
print(calculator.divide(5, 0))
print(calculator.power(2, -3))
print(calculator.square_root(-9))
