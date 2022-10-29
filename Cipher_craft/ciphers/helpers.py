
# caesar cipher
def caesarEncrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']%26
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def caesarDecrypt(form):
    text = form.cleaned_data['text']
    s = -form.cleaned_data['key']%26
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# vigenere cipher
from .logic.vigenere import VigenereCipher 
def viggenerateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def vigenereEncrypt(form):
    text = (form.cleaned_data['text']).upper()
    keyword = (form.cleaned_data['key']).upper()
    # obj=VigenereCipher()
    key = viggenerateKey(text,keyword)
    encrypt_text = [] 
    for i in range(len(text)): 
        x = (ord(text[i]) +ord(key[i])) % 26
        x += ord('A') 
        encrypt_text.append(chr(x)) 
    return("" . join(encrypt_text)) 
    

def vigenereDecrypt(form): 
    encrypt_text = (form.cleaned_data['text']).upper()
    keyword = (form.cleaned_data['key']).upper()
    # obj=VigenereCipher()
    key = viggenerateKey(encrypt_text,keyword)
    orig_text = [] 
    for i in range(len(encrypt_text)): 
        x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))
    # return obj.decrypt(encrypt_text,keyword)


from .logic.playfair import PlayfairCipher
def plyencrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = PlayfairCipher()
    return obj.encrypt(text,s)
def plydecrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = PlayfairCipher()
    return obj.decrypt(text,s)