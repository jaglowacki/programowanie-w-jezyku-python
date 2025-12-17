import zad_5_flatten_list.flatten_list as fl


class TestsIsPalindrome:

    def test_answer_1(self):
        assert fl.flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_answer_2(self):
        assert fl.flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]

    def test_answer_3(self):
        assert fl.flatten_list([]) == []

    def test_answer_4(self):
        assert fl.flatten_list([[[1]]]) == [1]

    def test_answer_5(self):
        assert fl.flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
