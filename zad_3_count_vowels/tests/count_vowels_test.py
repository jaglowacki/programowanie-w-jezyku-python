import pytest
import zad_3_count_vowels.count_vowels as cv


class TestsCountVowels:

    def test_answer_1(self):
        assert cv.count_vowels('Python') == 2

    def test_answer_2(self):
        assert cv.count_vowels('AEIOUY') == 6

    def test_answer_3(self):
        assert cv.count_vowels('bcd') == 0

    def test_answer_4(self):
        assert cv.count_vowels('') == 0

    def test_answer_5(self):
        assert cv.count_vowels('Próba żółwia') == 4
