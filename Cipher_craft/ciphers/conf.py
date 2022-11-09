from . import forms as cforms
from . import helpers as chelpers

forms = {
    'caesar': cforms.CipherTextForm,
    'vigenere': cforms.VigenereForm,
    'playfair': cforms.VigenereForm,
    'vernam':cforms.VigenereForm,
    'morse': cforms.MorseForm,
    'railfence': cforms.CipherTextForm,
    'TowerOfHanoi': cforms.TowerOfHanoiForm,
    'XOR':cforms.XOR,
    'columnTransposition':cforms.XOR,  #using the same form
    'atbash': cforms.atbash
}

encrypt_func = {
    'caesar': chelpers.caesarEncrypt,
    'vigenere': chelpers.vigenereEncrypt,
    'playfair': chelpers.plyencrypt,
    'vernam': chelpers.vernamEncrypt,
    'morse': chelpers.morseEncrypt,
    'railfence': chelpers.railfenceEncrypt,
    'TowerOfHanoi': chelpers.TowerOfHanoiSolver,
    'XOR':chelpers.xorEncrypt,
    'columnTransposition':chelpers.columTranspositionEncrypt,
    'atbash': chelpers.atbashEncrypt
}

decrypt_func = {
    'caesar': chelpers.caesarDecrypt,
    'vigenere': chelpers.vigenereDecrypt,
    'playfair': chelpers.plydecrypt,
    'vernam': chelpers.vernamDecrypt,
    'morse': chelpers.morseDecrypt,
    'railfence': chelpers.railfenceDecrypt,
    'TowerOfHanoi':chelpers.TowerOfHanoiSolver,
    'XOR':chelpers.xorDecrypt,
    'columnTransposition':chelpers.columTranspositionDecrypt,
    'atbash':chelpers.atbashDecrypt
}

cipher_title = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenere Cipher',
    'playfair': 'Playfair Cipher',
    'vernam':'Vernam Cipher',
    'morse': 'Morse Code',
    'railfence': 'Rail Fence Cipher',
    'TowerOfHanoi':'Tower Of Hanoi',
    'XOR':'XOR',
    'columnTransposition':'Column Transposition Cipher',
    'atbash':'Atbashs'
}
