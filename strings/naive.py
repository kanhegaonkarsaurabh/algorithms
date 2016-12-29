def naive(string, text):
    for i in range(len(text) - len(string)):
        if string == text[i:(i + len(string))]:
            return True
    return False
