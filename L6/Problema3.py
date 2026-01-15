def is_palindrome(text):
    # transformam in litere mici si eliminam spatiile
    clean = text.lower().replace(" ", "")
    # verificam daca este palindrom
    return clean == clean[::-1]


# test
print(is_palindrome("A man a plan a canal Panama"))
