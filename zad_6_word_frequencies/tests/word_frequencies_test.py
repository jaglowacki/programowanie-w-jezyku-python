import zad_6_word_frequencies.word_frequencies as wf


class TestsWordFrequencies:

    def test_answer_1(self):
        assert wf.word_frequencies('To be or not to be') == {'to': 2, 'be': 2, 'or': 1, 'not': 1}

    def test_answer_2(self):
        assert wf.word_frequencies('Hello, hello!') == {'hello': 2}

    def test_answer_3(self):
        assert wf.word_frequencies('') == {}

    def test_answer_4(self):
        assert wf.word_frequencies('Python Python python') == {'python': 3}

    def test_answer_5(self):
        assert wf.word_frequencies('Ala ma kota, a kot ma Ale.') == {'ala': 1, 'ma': 2, 'kota': 1, 'a': 1, 'kot': 1, 'ale': 1}
