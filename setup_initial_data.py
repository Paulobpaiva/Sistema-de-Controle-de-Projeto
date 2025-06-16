#!/usr/bin/env python
import os
import sys
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from activities.models import Worker, Action, Activity

def setup_initial_data():
    print("Configurando dados iniciais...")
    
    # Criar Worker para o admin
    admin_user = User.objects.get(username='admin')
    worker, created = Worker.objects.get_or_create(
        user=admin_user,
        defaults={
            'level': 'admin',
            'department': 'TI',
            'phone': '(11) 99999-9999'
        }
    )
    
    if created:
        print(f"Worker criado para {admin_user.get_full_name()}")
    else:
        print(f"Worker já existe para {admin_user.get_full_name()}")
    
    # Criar algumas ações de exemplo
    actions_data = [
        {
            'name': 'Desenvolvimento do Sistema Web',
            'description': 'Criação de um sistema web completo para gestão de projetos',
            'start_date': date.today() - timedelta(days=30),
            'end_date': date.today() + timedelta(days=60),
            'budget': 50000.00,
            'status': 'in_progress'
        },
        {
            'name': 'Implementação de API REST',
            'description': 'Desenvolvimento de API REST para integração com outros sistemas',
            'start_date': date.today() - timedelta(days=15),
            'end_date': date.today() + timedelta(days=45),
            'budget': 25000.00,
            'status': 'planning'
        },
        {
            'name': 'Testes e Qualidade',
            'description': 'Execução de testes automatizados e garantia de qualidade',
            'start_date': date.today(),
            'end_date': date.today() + timedelta(days=30),
            'budget': 15000.00,
            'status': 'planning'
        }
    ]
    
    for action_data in actions_data:
        action, created = Action.objects.get_or_create(
            name=action_data['name'],
            defaults={
                'owner': worker,
                **action_data
            }
        )
        
        if created:
            print(f"Ação criada: {action.name}")
        else:
            print(f"Ação já existe: {action.name}")
    
    # Criar algumas atividades de exemplo
    activities_data = [
        {
            'name': 'Análise de Requisitos',
            'description': 'Levantamento e documentação dos requisitos do sistema',
            'action': Action.objects.get(name='Desenvolvimento do Sistema Web'),
            'status': 'completed',
            'priority': 'high',
            'deadline': date.today() - timedelta(days=10),
            'estimated_hours': 16.0
        },
        {
            'name': 'Design da Interface',
            'description': 'Criação dos wireframes e protótipos da interface',
            'action': Action.objects.get(name='Desenvolvimento do Sistema Web'),
            'status': 'in_progress',
            'priority': 'medium',
            'deadline': date.today() + timedelta(days=5),
            'estimated_hours': 24.0
        },
        {
            'name': 'Desenvolvimento Backend',
            'description': 'Implementação da lógica de negócio e banco de dados',
            'action': Action.objects.get(name='Desenvolvimento do Sistema Web'),
            'status': 'not_started',
            'priority': 'high',
            'deadline': date.today() + timedelta(days=20),
            'estimated_hours': 80.0
        },
        {
            'name': 'Configuração do Ambiente',
            'description': 'Preparação do ambiente de desenvolvimento',
            'action': Action.objects.get(name='Implementação de API REST'),
            'status': 'not_started',
            'priority': 'medium',
            'deadline': date.today() + timedelta(days=3),
            'estimated_hours': 8.0
        },
        {
            'name': 'Criação de Testes Unitários',
            'description': 'Desenvolvimento de testes automatizados',
            'action': Action.objects.get(name='Testes e Qualidade'),
            'status': 'not_started',
            'priority': 'low',
            'deadline': date.today() + timedelta(days=15),
            'estimated_hours': 20.0
        }
    ]
    
    for activity_data in activities_data:
        activity, created = Activity.objects.get_or_create(
            name=activity_data['name'],
            action=activity_data['action'],
            defaults={
                'assigned_to': worker,
                **activity_data
            }
        )
        
        if created:
            print(f"Atividade criada: {activity.name}")
        else:
            print(f"Atividade já existe: {activity.name}")
    
    print("\nDados iniciais configurados com sucesso!")
    print(f"Usuário: admin")
    print(f"Senha: 1234")
    print(f"Worker criado com nível: {worker.get_level_display()}")

if __name__ == '__main__':
    setup_initial_data() 