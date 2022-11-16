import string


class VigenereCipher:
    """
    def encrypt(self, plain_text, key):
    def decrypt(self, cipher_text, key):
    def viggenerateKey(self,string, key):
    """
    def viggenerateKey(self,string, key): 
        key = list(key) 
        if len(string) == len(key): 
            return(key) 
        else: 
            for i in range(len(string) - len(key)): 
                key.append(key[i % len(key)]) 
        return("" . join(key)) 

    def encrypt(self, plain_text, key):
        try:
            key = self.viggenerateKey(plain_text,key)
            encrypt_text = [] 
            for i in range(len(plain_text)): 
                x = (ord(plain_text[i]) +ord(key[i])) % 26
                x += ord('A') 
                encrypt_text.append(chr(x)) 
            return("" . join(encrypt_text)) 
        except:
            return "#"

    def decrypt(self, cipher_text, key):
        try:
            key = self.viggenerateKey(cipher_text,key)
            orig_text = [] 
            for i in range(len(cipher_text)): 
                x = (ord(cipher_text[i]) -ord(key[i]) + 26) % 26
                x += ord('A') 
                orig_text.append(chr(x)) 
            return("" . join(orig_text))
        except:
            return "#"