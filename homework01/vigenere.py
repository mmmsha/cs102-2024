def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    for i in range(len(plaintext)):
           if plaintext[i].isalpha():
                if key[i].islower():
                     shift = ord(key[i]) - 97
                elif key[i].isupper():
                     shift = ord(key[i]) - 65
                nbuk = ord(plaintext[i]) + shift
                if plaintext[i].islower() and nbuk > ord("z"):
                     nbuk = nbuk - 26
                elif plaintext[i].isupper() and nbuk > ord("Z"):
                     nbuk = nbuk - 26
                otv = chr(nbuk)
                ciphertext += otv
           else:
                ciphertext+=plaintext[i]

    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    for i in range(len(ciphertext)):
           if ciphertext[i].isalpha():
                if key[i].islower():
                     shift = ord(key[i]) - 97
                elif key[i].isupper():
                     shift = ord(key[i]) - 65
                nbuk = ord(ciphertext[i]) - shift
                if ciphertext[i].islower() and nbuk < ord("a"):
                     nbuk = nbuk + 26
                elif ciphertext[i].isupper() and nbuk < ord("A"):
                     nbuk = nbuk + 26
                otv = chr(nbuk)
                plaintext += otv
           else:
                plaintext+=ciphertext[i]
    return plaintext
