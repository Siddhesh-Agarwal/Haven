CHARS = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
LENGTH = len(CHARS)


def encryptor(message: str, public_key: str, private_key: str) -> None:
    """Encrypt message with public and private key"""
    pub_len, priv_len = len(public_key), len(private_key)
    encrypted = ""
    for i in range(len(message)):
        encrypted += CHARS[
            CHARS.find(message[i])
            ^ CHARS.find(private_key[i % priv_len])
            ^ public_key[i % pub_len]
        ]
    return encrypted


def decryptor(message: str, public_key: str, private_key: str) -> None:
    """Decrypt message with public and private key"""
    pub_len, priv_len = len(public_key), len(private_key)
    decrypted = ""
    for i in range(len(message)):
        decrypted += CHARS[
            CHARS.find(message[i])
            ^ CHARS.find(private_key[i % priv_len])
            ^ public_key[i % pub_len]
        ]
    return decrypted
