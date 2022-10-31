from . import forms as cforms
from . import helpers as chelpers

forms = {
    'caesar': cforms.CipherTextForm,
    'vigenere': cforms.VigenereForm,
    'playfair': cforms.VigenereForm,
    'vernam':cforms.VigenereForm,
    'morse': cforms.MorseForm,
    'railfence': cforms.CipherTextForm,
}

encrypt_func = {
    'caesar': chelpers.caesarEncrypt,
    'vigenere': chelpers.vigenereEncrypt,
    'playfair': chelpers.plyencrypt,
    'vernam': chelpers.vernamEncrypt,
    'morse': chelpers.morseEncrypt,
    'railfence': chelpers.railfenceDecrypt,
}

decrypt_func = {
    'caesar': chelpers.caesarDecrypt,
    'vigenere': chelpers.vigenereDecrypt,
    'playfair': chelpers.plydecrypt,
    'vernam': chelpers.vernamDecrypt,
    'morse': chelpers.morseDecrypt,
    'railfence': chelpers.railfenceEncrypt,
}

cipher_title = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenere Cipher',
    'playfair': 'Playfair Cipher',
    'vernam':'Vernam Cipher',
    'morse': 'Morse Code',
    'railfence': 'Rail Fence Cipher',
}
