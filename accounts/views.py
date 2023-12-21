from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from .forms import UserForm




def user_registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            if User.objects.filter(email=email):
                messages.error(request, 'این ایمیل قبلا ثبت شده است')
                return redirect('accounts:register')
            user = User(email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request, 'اکانت شما با موفقیت ایجاد شد')
            return redirect('post:home')
    elif request.user.is_authenticated:
        return redirect('post:home')
    else:
        form = UserForm()
    
    return render(request, 'accounts/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            email = data['email']
            password = data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('post:home')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
                return render(request, 'accounts/login.html', {'form': form})
    elif request.user.is_authenticated:
        return redirect('post:home')
    else:
        form = UserForm()
    
    return render(request, 'accounts/login.html', {'form': form})


