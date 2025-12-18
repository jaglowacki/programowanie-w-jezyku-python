def word_frequencies(text: str) -> dict:
    import string
    text_without_pm = ''
    dictionary = {}
    punctuation_marks = string.punctuation
    for char in text:
        if char in punctuation_marks:
            text_without_pm += ' '
        else:
            text_without_pm += char
    word_list = text_without_pm.lower().split()
    while len(word_list) > 0:
        word = word_list.pop(0)
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary
