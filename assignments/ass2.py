def caesar_cipher(string, offset):
    string = string.lower()
    cipher = ""
    for letters in string:
        x = ord(letters) - offset
        if x < 97:
           x = 123-(97-x)
        cipher = cipher + chr(x)
    return cipher