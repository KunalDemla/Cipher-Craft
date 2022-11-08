from django.shortcuts import render,get_object_or_404
from .models import Ciphers
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
        'about': 'ciphers/'+cipher_choice+'_about.html',
        'choice': cipher_choice,
        'fav': 'Add to Favourites'
    }
    cipher = get_object_or_404(Ciphers,name=cipher_choice)
    if cipher.favourites.filter(id=request.user.id).exists():
        context['fav'] = 'Remove from Favourites'
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