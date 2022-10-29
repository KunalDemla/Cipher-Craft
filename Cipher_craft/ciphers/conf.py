from . import forms as cforms
from . import helpers as chelpers
# Create your views here.
forms = {
    'caesar': cforms.CipherTextForm,
    'vigenere': cforms.VigenereForm,
    'playfair': cforms.VigenereForm,
    'morse': cforms.MorseForm
}

encrypt_func = {
    'caesar': chelpers.caesarEncrypt,
    'vigenere': chelpers.vigenereEncrypt,
    'playfair': chelpers.plyencrypt,
    'morse': chelpers.morseEncrypt
}

decrypt_func = {
    'caesar': chelpers.caesarDecrypt,
    'vigenere': chelpers.vigenereDecrypt,
    'playfair': chelpers.plydecrypt,
    'morse': chelpers.morseDecrypt
}

cipher_title = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenere Cipher',
    'playfair': 'Playfair Cipher',
    'morse': 'Morse Code'
}
