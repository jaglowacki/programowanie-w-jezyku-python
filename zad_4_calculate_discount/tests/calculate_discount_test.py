import pytest
import zad_4_calculate_discount.calculate_discount as cd


class TestsDiscount:

    def test_answer_1(self):
        assert cd.calculate_discount(100, 0.2) == 80

    def test_answer_2(self):
        assert cd.calculate_discount(50, 0) == 50

    def test_answer_3(self):
        assert cd.calculate_discount(200, 1) == 0.0

    def test_answer_4(self):
        with pytest.raises(ValueError, match='Discount spoza zakresu 0-1!'):
            cd.calculate_discount(100, -0.1)

    def test_answer_5(self):
        with pytest.raises(ValueError, match='Discount spoza zakresu 0-1!'):
            cd.calculate_discount(100, 1.5)
