BASE = 256


def hash_code(string):
    code = 0
    for i in range(len(string)):
        code += ord(string[i]) * BASE ** (len(string) - i - 1)
    return code


def rabin_karp(string, text):
    substring = text[:len(string)]
    string_hash = hash_code(string)
    text_hash = hash_code(substring)
    if string_hash == text_hash:
        return string == substring
    for i in range(len(string), len(text)):
        prev = ord(text[i - len(string)]) * BASE ** (len(string) - 1)
        text_hash = BASE * (text_hash - prev) + ord(text[i])
        if string_hash == text_hash:
            substring = text[(i - len(string) + 1):(i + 1)]
            return string == substring
    return False
