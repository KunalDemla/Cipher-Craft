from . import forms as cforms
from . import helpers as chelpers

forms = {
    'caesar': cforms.CipherTextForm,
    'vigenere': cforms.VigenereForm,
    'playfair': cforms.VigenereForm,
    'vernam':cforms.VigenereForm,
    'morse': cforms.MorseForm,

    'TowerOfHanoi': cforms.TowerOfHanoiForm
}

encrypt_func = {
    'caesar': chelpers.caesarEncrypt,
    'vigenere': chelpers.vigenereEncrypt,
    'playfair': chelpers.plyencrypt,
    'vernam': chelpers.vernamEncrypt,
    'morse': chelpers.morseEncrypt,

    'TowerOfHanoi':chelpers.TowerOfHanoiSolver
}

decrypt_func = {
    'caesar': chelpers.caesarDecrypt,
    'vigenere': chelpers.vigenereDecrypt,
    'playfair': chelpers.plydecrypt,
    'vernam': chelpers.vernamDecrypt,
    'morse': chelpers.morseDecrypt,

    'TowerOfHanoi':chelpers.TowerOfHanoiSolver
}

cipher_title = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenere Cipher',
    'playfair': 'Playfair Cipher',
    'vernam':'Vernam Cipher',
    'morse': 'Morse Code',
    
    'TowerOfHanoi':'Tower Of Hanoi'
}
