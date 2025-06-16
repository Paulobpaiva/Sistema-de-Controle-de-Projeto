from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
from .models import Action, Activity, TimeEntry, Comment, Worker
from .forms import ActivityForm, TimeEntryForm, CommentForm


@login_required
def activity_list(request):
    """Lista de atividades do usuário logado"""
    try:
        worker = request.user.worker
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    # Filtrar atividades do usuário
    activities = Activity.objects.filter(assigned_to=worker).select_related('action')
    
    # Filtros
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    
    if status_filter:
        activities = activities.filter(status=status_filter)
    if priority_filter:
        activities = activities.filter(priority=priority_filter)
    
    context = {
        'activities': activities,
        'status_choices': Activity.STATUS_CHOICES,
        'priority_choices': Activity.PRIORITY_CHOICES,
        'current_filters': {
            'status': status_filter,
            'priority': priority_filter,
        }
    }
    
    return render(request, 'activities/activity_list.html', context)


@login_required
def activity_detail(request, pk):
    """Detalhes de uma atividade específica"""
    activity = get_object_or_404(Activity, pk=pk)
    
    # Verificar se o usuário tem permissão
    try:
        worker = request.user.worker
        if activity.assigned_to != worker and worker.level not in ['admin', 'manager']:
            messages.error(request, 'Você não tem permissão para visualizar esta atividade.')
            return redirect('activities:activity_list')
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    # Formulário para registro de tempo
    if request.method == 'POST':
        time_form = TimeEntryForm(request.POST)
        comment_form = CommentForm(request.POST)
        
        if time_form.is_valid():
            time_entry = time_form.save(commit=False)
            time_entry.activity = activity
            time_entry.worker = worker
            time_entry.save()
            messages.success(request, 'Tempo registrado com sucesso!')
            return redirect('activities:activity_detail', pk=pk)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.activity = activity
            comment.worker = worker
            comment.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('activities:activity_detail', pk=pk)
    else:
        time_form = TimeEntryForm()
        comment_form = CommentForm()
    
    context = {
        'activity': activity,
        'time_form': time_form,
        'comment_form': comment_form,
        'time_entries': activity.time_entries.all().order_by('-start_time'),
        'comments': activity.comments.all().order_by('-created_at'),
    }
    
    return render(request, 'activities/activity_detail.html', context)


@login_required
def activity_create(request):
    """Criar nova atividade"""
    try:
        worker = request.user.worker
        if worker.level not in ['admin', 'manager']:
            messages.error(request, 'Você não tem permissão para criar atividades.')
            return redirect('activities:activity_list')
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            messages.success(request, 'Atividade criada com sucesso!')
            return redirect('activities:activity_detail', pk=activity.pk)
    else:
        form = ActivityForm()
    
    context = {
        'form': form,
        'title': 'Nova Atividade'
    }
    
    return render(request, 'activities/activity_form.html', context)


@login_required
def activity_update(request, pk):
    """Atualizar atividade existente"""
    activity = get_object_or_404(Activity, pk=pk)
    
    try:
        worker = request.user.worker
        if activity.assigned_to != worker and worker.level not in ['admin', 'manager']:
            messages.error(request, 'Você não tem permissão para editar esta atividade.')
            return redirect('activities:activity_list')
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atividade atualizada com sucesso!')
            return redirect('activities:activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)
    
    context = {
        'form': form,
        'activity': activity,
        'title': 'Editar Atividade'
    }
    
    return render(request, 'activities/activity_form.html', context)


@login_required
def activity_delete(request, pk):
    """Excluir atividade"""
    activity = get_object_or_404(Activity, pk=pk)
    
    try:
        worker = request.user.worker
        if worker.level not in ['admin', 'manager']:
            messages.error(request, 'Você não tem permissão para excluir atividades.')
            return redirect('activities:activity_list')
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Atividade excluída com sucesso!')
        return redirect('activities:activity_list')
    
    context = {
        'activity': activity
    }
    
    return render(request, 'activities/activity_confirm_delete.html', context)


@login_required
def update_activity_status(request, pk):
    """Atualizar status da atividade via AJAX"""
    if request.method == 'POST' and request.is_ajax():
        activity = get_object_or_404(Activity, pk=pk)
        new_status = request.POST.get('status')
        
        try:
            worker = request.user.worker
            if activity.assigned_to != worker and worker.level not in ['admin', 'manager']:
                return JsonResponse({'success': False, 'message': 'Permissão negada'})
        except Worker.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Perfil incompleto'})
        
        if new_status in dict(Activity.STATUS_CHOICES):
            activity.status = new_status
            activity.save()
            return JsonResponse({'success': True, 'message': 'Status atualizado'})
        
        return JsonResponse({'success': False, 'message': 'Status inválido'})
    
    return JsonResponse({'success': False, 'message': 'Método não permitido'})


@login_required
def action_list(request):
    """Lista de ações"""
    try:
        worker = request.user.worker
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    # Filtrar ações baseado no nível do usuário
    if worker.level in ['admin', 'manager']:
        actions = Action.objects.all()
    else:
        actions = Action.objects.filter(activities__assigned_to=worker).distinct()
    
    context = {
        'actions': actions
    }
    
    return render(request, 'activities/action_list.html', context)


@login_required
def action_detail(request, pk):
    """Detalhes de uma ação"""
    action = get_object_or_404(Action, pk=pk)
    
    try:
        worker = request.user.worker
        if worker.level not in ['admin', 'manager'] and not action.activities.filter(assigned_to=worker).exists():
            messages.error(request, 'Você não tem permissão para visualizar esta ação.')
            return redirect('activities:action_list')
    except Worker.DoesNotExist:
        messages.warning(request, 'Complete seu perfil primeiro.')
        return redirect('accounts:complete_profile')
    
    context = {
        'action': action,
        'activities': action.activities.all().order_by('deadline')
    }
    
    return render(request, 'activities/action_detail.html', context)
