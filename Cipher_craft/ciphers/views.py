from django.shortcuts import render
from .forms import CipherTextForm
# Create your views here.
def caesar(request):
    context = {
        'form': CipherTextForm(),
        'output_text': ''
    }
    if request.method == 'POST':
        form = CipherTextForm(request.POST)
        if form.is_valid():
            context['form'] = form
            text = form.cleaned_data['text']
            key = form.cleaned_data['key']
            output = caesarEncrypt(text,key)
            context['output_text'] = output
    return render(request,'ciphers/caesar.html',context)

def caesarEncrypt(text,s):
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