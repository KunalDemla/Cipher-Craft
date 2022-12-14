class VernamCipher:
    def __init__(self):
        self._key = ''
        self._ciphertext = ''
        self._plaintext = ''

    def encrypt(self, plain_text, key):
        try:
            self._plaintext = plain_text.replace(" ", "").lower()
            self._key = key.replace(" ", "").lower()
            self._ciphertext = ""
            if len(self._plaintext) != len(self._key):
                raise Exception("Length of plain text and key must be same")
            else:
                for i in range(len(self._plaintext)):
                    k1 = ord(self._plaintext[i]) - 97
                    k2 = ord(self._key[i]) - 97
                    s = chr((k1 + k2) % 26 + 97)
                    self._ciphertext += s
                return self._ciphertext.upper()
        except:
            return "#"

    def decrypt(self, cipher_text, key):
        try:
            self._ciphertext = cipher_text.replace(" ", "").lower()
            self._key = key.replace(" ", "").lower()
            self._plaintext = ""
            if len(self._ciphertext) != len(self._key):
                raise Exception("Length of cipher text and key must be same")
            else:
                for i in range(len(self._ciphertext)):
                    k1 = ord(self._ciphertext[i]) - 97
                    k2 = ord(self._key[i]) - 97
                    s = chr((((k1 - k2) + 26) % 26) + 97)
                    self._plaintext += s
                return self._plaintext.upper()
        except:
            return "#"