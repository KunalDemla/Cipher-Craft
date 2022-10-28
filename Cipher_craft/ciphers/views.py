from django.shortcuts import render
from .forms import CipherTextForm
# Create your views here.
forms = {
    'caesar': CipherTextForm
}
def ciphers(request,cipher_choice):
    context = {
        'form': forms[cipher_choice](),
        'output_text': ''
    }
    if request.method == 'POST':
        form = forms[cipher_choice](request.POST)
        if form.is_valid():
            context['form'] = form
            output = caesarEncrypt(form)
            context['output_text'] = output
    return render(request,'ciphers/caesar.html',context)

def caesarEncrypt(form):
    text = form.cleaned_data['text']
    s = form.cleaned_data['key']
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