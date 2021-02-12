from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 10, 4) == 6

    def test_adding_correctly(self):
        assert self.calc.adding(self, 7, 3) == 10