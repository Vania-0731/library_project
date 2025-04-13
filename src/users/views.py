# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirige al login luego de cerrar sesión

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Lo loguea automáticamente
            return redirect('home')  # Redirige a la página principal
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
