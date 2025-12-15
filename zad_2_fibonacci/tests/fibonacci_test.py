import pytest
import zad_2_fibonacci.fibonacci as fb


class TestsFibonacci:

    def test_answer_1(self):
        assert fb.fibonacci(0) == 0

    def test_answer_2(self):
        assert fb.fibonacci(1) == 1

    def test_answer_3(self):
        assert fb.fibonacci(5) == 5

    def test_answer_4(self):
        assert fb.fibonacci(10) == 55

    def test_answer_5(self):
        with pytest.raises(ValueError, match='Argument nie może być ujemny!'):
            fb.fibonacci(-1)
