import zad_7_is_prime.is_prime as ip


class TestsIsPrime:

    def test_answer_1(self):
        assert ip.is_prime(2)

    def test_answer_2(self):
        assert ip.is_prime(3)

    def test_answer_3(self):
        assert not ip.is_prime(4)

    def test_answer_4(self):
        assert not ip.is_prime(0)

    def test_answer_5(self):
        assert not ip.is_prime(1)

    def test_answer_6(self):
        assert ip.is_prime(5)

    def test_answer_7(self):
        assert ip.is_prime(97)
