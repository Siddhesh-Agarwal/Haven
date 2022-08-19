CHARS = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
LENGTH = len(CHARS)


def encrypt(text: str, shift: int):
    """Caesar cipher"""
    encrypted = ""
    for char in text:
        encrypted += CHARS[(CHARS.find(char) + shift) % LENGTH]
    return encrypted


def decrypt(text: str, shift: int):
    decrypted = ""
    for char in text:
        decrypted += CHARS[(CHARS.find(char) - shift) % LENGTH]
    return decrypted
