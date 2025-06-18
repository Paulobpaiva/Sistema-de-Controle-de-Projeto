from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
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
        user = form.save(commit=False)
        user.is_active = False  # Usuário fica inativo até aprovação
        user.save()
        form.save_m2m()
        messages.success(self.request, 'Conta criada com sucesso! Aguarde aprovação do administrador.')
        return redirect('accounts:login')


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


@user_passes_test(lambda u: u.is_superuser)
def pending_approval(request):
    pendentes = User.objects.filter(is_active=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        user = User.objects.get(id=user_id)
        if action == 'aprovar':
            user.is_active = True
            user.save()
            messages.success(request, f'Usuário {user.username} aprovado!')
        elif action == 'rejeitar':
            user.delete()
            messages.warning(request, f'Usuário {user.username} rejeitado e removido!')
        return redirect('accounts:pending_approval')
    return render(request, 'accounts/pending_approval.html', {'pendentes': pendentes})
