import zad_1_is_palindrome.is_palindrome as ip


class TestsIsPalindrome:

    def test_answer_1(self):
        assert ip.is_palindrome('kajak')

    def test_answer_2(self):
        assert ip.is_palindrome('Kobyła ma mały bok')

    def test_answer_3(self):
        assert not ip.is_palindrome('python')

    def test_answer_4(self):
        assert ip.is_palindrome('')

    def test_answer_5(self):
        assert ip.is_palindrome('A')
