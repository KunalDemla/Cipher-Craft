from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from ciphers.models import Ciphers

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form' : form})

@login_required
def show_favourites(request):
    favourite_ciphers = Ciphers.objects.all().filter(favourites=request.user)
    return render(request,'users/favourite_ciphers_list.html',{'favourite_ciphers':favourite_ciphers})

@login_required
def favourite_add(request,cipher_choice):
    cipher = get_object_or_404(Ciphers,name=cipher_choice)
    if cipher.favourites.filter(id=request.user.id).exists():
        cipher.favourites.remove(request.user)
    else:
        cipher.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@login_required
def Profile(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if(u_form.is_valid() and p_form.is_valid() ) :
            u_form.save()
            p_form.save()
            messages.success(request,f'Account has been updated!')
            return redirect('user_profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile) 
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)


