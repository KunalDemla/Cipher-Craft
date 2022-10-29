from django.shortcuts import render
from .conf import forms,encrypt_func,decrypt_func,cipher_title

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
        'about': 'ciphers/'+cipher_choice+'_about.html'
    }
    if request.method == 'POST':
        form = forms[cipher_choice](request.POST)
        if form.is_valid():
            context['form'] = form
            operation = form.cleaned_data['operation']
            if operation == 'encrypt':
                output = encrypt_func[cipher_choice](form)
            else:
                output = decrypt_func[cipher_choice](form)
            context['output_text'] = output

    return render(request,'ciphers/ciphers.html',context)