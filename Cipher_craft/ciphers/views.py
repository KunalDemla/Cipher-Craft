from django.shortcuts import render
from . import forms as cforms
from . import helpers as chelpers
# Create your views here.
forms = {
    'caesar': cforms.CipherTextForm,
    'vigenere': cforms.VigenereForm,
}

encrypt_func = {
    'caesar': chelpers.caesarEncrypt,
    'vigenere': chelpers.vigenereEncrypt
}

decrypt_func = {
    'caesar': chelpers.caesarDecrypt,
    'vigenere': chelpers.vigenereDecrypt
}

cipher_title = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenere Cipher'
}

def home(request):
    context={
        'ciphers' : cipher_title,
    }
    return render(request,'ciphers/cipher_list.html',context)



def ciphers(request,cipher_choice):
    context = {
        'form': forms[cipher_choice](),
        'output_text': '',
        'title': cipher_title[cipher_choice],
        'button':''
    }
    if request.method == 'POST':
        form = forms[cipher_choice](request.POST)
        if form.is_valid():
            context['form'] = form
            operation = form.cleaned_data['operation']
            context['button']=operation.upper()
            if operation == 'encrypt':
                output = encrypt_func[cipher_choice](form)
            else:
                output = decrypt_func[cipher_choice](form)
            context['output_text'] = output

    return render(request,'ciphers/ciphers.html',context)