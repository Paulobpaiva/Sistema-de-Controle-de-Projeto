from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum, Case, When, IntegerField
from django.utils import timezone
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.offline as opy
import json
from activities.models import Action, Activity, Worker, TimeEntry


@login_required
def index(request):
    """Dashboard principal com KPIs e gráficos"""
    
    # Dados para KPIs
    total_actions = Action.objects.count()
    total_activities = Activity.objects.count()
    completed_activities = Activity.objects.filter(status='completed').count()
    
    # Atividades atrasadas (apenas se há atividades com deadline)
    overdue_activities = Activity.objects.filter(
        deadline__lt=timezone.now().date(),
        status__in=['not_started', 'in_progress']
    ).count()
    
    # Progresso geral
    progress_percentage = round((completed_activities / total_activities * 100) if total_activities > 0 else 0, 1)
    
    # Atividades por status
    status_data = Activity.objects.values('status').annotate(count=Count('id'))
    status_labels = [item['status'] for item in status_data]
    status_values = [item['count'] for item in status_data]
    
    # Criar gráfico de pizza para status (apenas se há dados)
    status_pie_div = ""
    if status_data:
        status_pie = go.Figure(data=[go.Pie(
            labels=status_labels,
            values=status_values,
            hole=0.3,
            marker_colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        )])
        status_pie.update_layout(
            title="Atividades por Status",
            height=400,
            showlegend=True
        )
        status_pie_div = opy.plot(status_pie, auto_open=False, output_type='div')
    
    # Atividades por prioridade
    priority_data = Activity.objects.values('priority').annotate(count=Count('id'))
    priority_labels = [item['priority'] for item in priority_data]
    priority_values = [item['count'] for item in priority_data]
    
    priority_bar_div = ""
    if priority_data:
        priority_bar = go.Figure(data=[go.Bar(
            x=priority_labels,
            y=priority_values,
            marker_color=['#FF6B6B', '#FFE66D', '#4ECDC4', '#45B7D1']
        )])
        priority_bar.update_layout(
            title="Atividades por Prioridade",
            xaxis_title="Prioridade",
            yaxis_title="Quantidade",
            height=400
        )
        priority_bar_div = opy.plot(priority_bar, auto_open=False, output_type='div')
    
    # Progresso das ações (calculado baseado nas atividades)
    actions_progress = []
    for action in Action.objects.all():
        total_activities_in_action = Activity.objects.filter(action=action).count()
        completed_activities_in_action = Activity.objects.filter(action=action, status='completed').count()
        
        if total_activities_in_action > 0:
            progress = round((completed_activities_in_action / total_activities_in_action) * 100, 1)
        else:
            progress = 0
            
        actions_progress.append({
            'name': action.name,
            'progress': progress
        })
    
    progress_bar_div = ""
    if actions_progress:
        action_names = [item['name'] for item in actions_progress]
        action_progress = [item['progress'] for item in actions_progress]
        
        progress_bar = go.Figure(data=[go.Bar(
            x=action_names,
            y=action_progress,
            marker_color='#4ECDC4'
        )])
        progress_bar.update_layout(
            title="Progresso das Ações",
            xaxis_title="Ações",
            yaxis_title="Progresso (%)",
            height=400
        )
        progress_bar_div = opy.plot(progress_bar, auto_open=False, output_type='div')
    
    # Atividades recentes
    recent_activities = Activity.objects.select_related('action', 'assigned_to__user').order_by('-created_at')[:10]
    
    # Atividades atrasadas
    overdue_activities_list = Activity.objects.filter(
        deadline__lt=timezone.now().date(),
        status__in=['not_started', 'in_progress']
    ).select_related('action', 'assigned_to__user')[:5]
    
    context = {
        'total_actions': total_actions,
        'total_activities': total_activities,
        'completed_activities': completed_activities,
        'overdue_activities': overdue_activities,
        'progress_percentage': progress_percentage,
        'status_pie_div': status_pie_div,
        'priority_bar_div': priority_bar_div,
        'progress_bar_div': progress_bar_div,
        'recent_activities': recent_activities,
        'overdue_activities_list': overdue_activities_list,
    }
    
    return render(request, 'dashboard/index.html', context)


@login_required
def activities_report(request):
    """Relatório detalhado de atividades"""
    
    # Filtros
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    action_filter = request.GET.get('action', '')
    
    activities = Activity.objects.select_related('action', 'assigned_to__user')
    
    if status_filter:
        activities = activities.filter(status=status_filter)
    if priority_filter:
        activities = activities.filter(priority=priority_filter)
    if action_filter:
        activities = activities.filter(action_id=action_filter)
    
    # Estatísticas
    total_time_spent = sum(activity.total_time_spent for activity in activities)
    avg_time_per_activity = total_time_spent / activities.count() if activities.count() > 0 else 0
    
    context = {
        'activities': activities,
        'total_time_spent': total_time_spent,
        'avg_time_per_activity': avg_time_per_activity,
        'status_choices': Activity.STATUS_CHOICES,
        'priority_choices': Activity.PRIORITY_CHOICES,
        'actions': Action.objects.all(),
        'current_filters': {
            'status': status_filter,
            'priority': priority_filter,
            'action': action_filter,
        }
    }
    
    return render(request, 'dashboard/activities_report.html', context)


@login_required
def time_report(request):
    """Relatório de tempo gasto"""
    
    # Filtros de data
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    time_entries = TimeEntry.objects.select_related('activity', 'worker__user')
    
    if start_date:
        time_entries = time_entries.filter(start_time__date__gte=start_date)
    if end_date:
        time_entries = time_entries.filter(start_time__date__lte=end_date)
    
    # Agrupar por trabalhador
    worker_time = {}
    for entry in time_entries:
        worker_name = entry.worker.full_name
        if worker_name not in worker_time:
            worker_time[worker_name] = 0
        worker_time[worker_name] += entry.duration_hours
    
    # Criar gráfico de tempo por trabalhador
    worker_names = list(worker_time.keys())
    worker_hours = list(worker_time.values())
    
    worker_time_chart = go.Figure(data=[go.Bar(
        x=worker_names,
        y=worker_hours,
        marker_color='#45B7D1'
    )])
    worker_time_chart.update_layout(
        title="Tempo Gasto por Trabalhador",
        xaxis_title="Trabalhador",
        yaxis_title="Horas",
        height=400
    )
    worker_time_chart_div = opy.plot(worker_time_chart, auto_open=False, output_type='div')
    
    context = {
        'time_entries': time_entries,
        'worker_time_chart_div': worker_time_chart_div,
        'total_hours': sum(worker_hours),
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'dashboard/time_report.html', context)
