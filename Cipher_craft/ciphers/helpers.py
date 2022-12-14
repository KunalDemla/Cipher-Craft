from cgi import test
from .logic.ceasar import CeasarCipher
# caesar cipher
def caesarEncrypt(form):
    text = form.cleaned_data['text']
    key = form.cleaned_data['key']%26
    obj=CeasarCipher()
    return obj.encrypt(text,key)

def caesarDecrypt(form):
    text = form.cleaned_data['text']
    key = -form.cleaned_data['key']%26
    obj=CeasarCipher()
    return obj.decrypt(text,key)

# vigenere cipher
from .logic.vigenere import VigenereCipher 
def vigenereEncrypt(form):
    text = (form.cleaned_data['text']).upper()
    key = (form.cleaned_data['key']).upper()
    obj=VigenereCipher()
    return obj.encrypt(text,key)
    
def vigenereDecrypt(form): 
    encrypt_text = (form.cleaned_data['text']).upper()
    keyword = (form.cleaned_data['key']).upper()
    obj=VigenereCipher()
    return obj.decrypt(encrypt_text,keyword)

#PLAYFAIR
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


#MORSE
from .logic.morse import Morse
def morseEncrypt(form):
    text = form.cleaned_data['text']
    obj = Morse()
    return obj.encrypt(text)
def morseDecrypt(form):
    encrypt_text = form.cleaned_data['text']
    obj = Morse()
    return obj.decrypt(encrypt_text)

#Verman
from .logic.vernam import VernamCipher
def vernamEncrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = VernamCipher()
    return obj.encrypt(text,s)

def vernamDecrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = VernamCipher()
    return obj.decrypt(text,s)

#railfence
from .logic.railFence import RailFence
def railfenceEncrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = RailFence()
    return obj.encrypt(text,s)

def railfenceDecrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
    obj = RailFence()
    return obj.decrypt(text,s)

#Tower of hanoi
from .logic.TowerOfHanoi import TowerOfHanoi
def TowerOfHanoiSolver(form):
    disks = form.cleaned_data['disks']
    obj = TowerOfHanoi()
    return obj.solver(disks)

#XOR
from .logic.xor import encryptDecrypt
def xorEncrypt(form):
    text=form.cleaned_data['text']
    key=form.cleaned_data['key']
    return encryptDecrypt(key,text)
def xorDecrypt(form):
    text=form.cleaned_data['text']
    key=form.cleaned_data['key']
    return encryptDecrypt(key,text)
#columnarTransposition

from .logic.columnarTransposition import encryptMessage,decryptMessage
def columTranspositionEncrypt(form):
    text = form.cleaned_data['text']
    key = form.cleaned_data['key']
    return encryptMessage(key,text)

def columTranspositionDecrypt(form):
    text = form.cleaned_data['text']
    key = form.cleaned_data['key']
    return decryptMessage(key,text)


#ATBASH
from .logic.atbash import atbash
def atbashEncrypt(form):
    text = form.cleaned_data['text']
    return atbash(text)
def atbashDecrypt(form):
    text = form.cleaned_data['text']
    return atbash(text)