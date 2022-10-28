
# caesar cipher
from ast import keyword


def caesarEncrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']%26
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
    # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
    # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def caesarDecrypt(form):
    text = form.cleaned_data['text']
    s = -form.cleaned_data['key']%26
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
    # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
    # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# vigenere cipher
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

def vigenereEncrypt(form):
    string = form.cleaned_data['text']
    keyword = form.cleaned_data['key']
    print(string,keyword)
    key = generateKey(string,keyword)
    encrypt_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) +ord(key[i])) % 26
        x += ord('A') 
        encrypt_text.append(chr(x)) 
    return("" . join(encrypt_text)) 

def vigenereDecrypt(form): 
    encrypt_text = form.cleaned_data['text']
    keyword = form.cleaned_data['key']
    key = generateKey(encrypt_text,keyword)
    orig_text = [] 
    for i in range(len(encrypt_text)): 
        x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))