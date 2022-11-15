class RailFence:
    def __init__(self):
        self._key = ''
        self._ciphertext = ''
        self._plaintext = ''

    @staticmethod
    def _sequence(key):
        arr = []
        i = 0
        while i < key - 1:
            arr.append(i)
            i += 1
        while i > 0:
            arr.append(i)
            i -= 1
        return arr

    def encrypt(self, plaintext, key):
        try:
            self._plaintext = plaintext.replace(' ', '')
            self._ciphertext = ""
            self._key = key
            L = self._sequence(self._key)
            temp = L
            while len(self._plaintext) > len(L):
                L = L + temp
            for _ in range(len(L) - len(self._plaintext)):
                L.pop()
            num = 0
            while num < self._key:
                for i in range(L.count(num)):
                    self._ciphertext = self._ciphertext + self._plaintext[L.index(num)]
                    L[L.index(num)] = self._key
                num += 1
            return self._ciphertext
        except:
            return "#"

    def decrypt(self, ciphertext, key):
        try:
            self._ciphertext = ciphertext
            self._plaintext = ""
            self._key = key
            L = self._sequence(self._key)
            temp = L
            while len(self._ciphertext) > len(L):
                L = L + temp
            for i in range(len(L) - len(self._ciphertext)):
                L.pop()
            temp = sorted(L)
            for i in L:
                k = temp.index(i)
                temp[k] = self._key
                self._plaintext += self._ciphertext[k]
            return self._plaintext
        except:
            return "#"