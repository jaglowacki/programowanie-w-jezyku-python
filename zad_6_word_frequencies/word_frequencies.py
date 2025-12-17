def word_frequencies(text: str) -> dict:
    import string
    text_without_pm=''
    slownik={}
    punctuation_marks= string.punctuation
    for char in text:
        if char in punctuation_marks:
            text_without_pm += ' '
        else:
            text_without_pm += char
    text_without_pm = text_without_pm.lower()
    word_list = text_without_pm.split()
    while len(word_list)>0:
        slowo=word_list.pop(0)
        if slowo not in slownik:
            slownik[slowo]=1
        else:
            slownik[slowo]+=1
    return slownik

print(word_frequencies("To be or not to be"))