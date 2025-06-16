from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, WorkerRegistrationForm, CustomAuthenticationForm
from activities.models import Worker


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('dashboard:index')
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


def custom_logout(request):
    """View personalizada para logout que aceita GET e POST"""
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso!')
    return redirect('accounts:login')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar.')
        return response


@login_required
def profile(request):
    try:
        worker = request.user.worker
    except Worker.DoesNotExist:
        worker = None
    
    context = {
        'worker': worker,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
            messages.success(request, 'Perfil completado com sucesso!')
            return redirect('dashboard:index')
    else:
        form = WorkerRegistrationForm()
    
    return render(request, 'accounts/complete_profile.html', {'form': form})
