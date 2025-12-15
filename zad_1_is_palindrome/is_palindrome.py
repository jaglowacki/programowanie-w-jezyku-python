def is_palindrome(text: str) -> bool:
    text_normal = text.lower().replace(' ', '')
    text_reversed = text_normal[::-1]
    return text_reversed == text_normal
