from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lms-home')  # Замените 'home' на имя вашего URL-адреса для домашней страницы
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
