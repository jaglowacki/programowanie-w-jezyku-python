import Sample.sample as sample


def test_answer_1():
    assert sample.func(3) == 3
    assert sample.func(3) == 4


def test_answer_2():
    assert sample.func(3) == 12
