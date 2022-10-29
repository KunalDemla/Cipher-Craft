import string


class CeasarCipher:
    """
    def encrypt(self, plain_text, key):
    def decrypt(self, cipher_text, key):
    """
    def encrypt(self, plain_text, key):
        result = ""
        for i in range(len(plain_text)):
            char = plain_text[i]
            if (char.isupper()):
                result += chr((ord(char) + key-65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result

    def decrypt(self, cipher_text, key):
        result = ""
        for i in range(len(cipher_text)):
            char = cipher_text[i]
            if (char.isupper()):
                result += chr((ord(char) + key-65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)
        return result