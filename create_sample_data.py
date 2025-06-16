#!/usr/bin/env python
import os
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from activities.models import Worker, Action, Activity

def create_sample_data():
    print("🚀 Criando dados de exemplo...")
    
    # 1. Criar usuário admin se não existir
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'first_name': 'Administrador',
            'last_name': 'Sistema',
            'is_staff': True,
            'is_superuser': True,
            'is_active': True
        }
    )
    
    if created:
        admin_user.set_password('1234')
        admin_user.save()
        print("✅ Usuário admin criado!")
    else:
        admin_user.set_password('1234')
        admin_user.save()
        print("✅ Senha do usuário admin atualizada!")
    
    # 2. Criar Worker para admin
    admin_worker, worker_created = Worker.objects.get_or_create(
        user=admin_user,
        defaults={
            'level': 'admin',
            'department': 'TI',
            'phone': '(11) 99999-9999'
        }
    )
    
    if worker_created:
        print("✅ Worker criado para admin!")
    
    # 3. Criar ações de exemplo
    actions_data = [
        {
            'name': 'Desenvolvimento do Sistema Web',
            'description': 'Criar um sistema web completo para gestão de projetos',
            'start_date': date.today() - timedelta(days=30),
            'end_date': date.today() + timedelta(days=60),
            'budget': 50000.00,
            'status': 'in_progress'
        },
        {
            'name': 'Implementação de API',
            'description': 'Desenvolver API REST para integração com outros sistemas',
            'start_date': date.today() - timedelta(days=15),
            'end_date': date.today() + timedelta(days=45),
            'budget': 25000.00,
            'status': 'planning'
        },
        {
            'name': 'Testes e Qualidade',
            'description': 'Realizar testes unitários, integração e aceitação',
            'start_date': date.today() - timedelta(days=10),
            'end_date': date.today() + timedelta(days=30),
            'budget': 15000.00,
            'status': 'planning'
        }
    ]
    
    actions = []
    for action_data in actions_data:
        action, created = Action.objects.get_or_create(
            name=action_data['name'],
            defaults={
                'description': action_data['description'],
                'owner': admin_worker,
                'start_date': action_data['start_date'],
                'end_date': action_data['end_date'],
                'budget': action_data['budget'],
                'status': action_data['status']
            }
        )
        actions.append(action)
        if created:
            print(f"✅ Ação criada: {action.name}")
    
    # 4. Criar atividades de exemplo
    activities_data = [
        # Atividades para "Desenvolvimento do Sistema Web"
        {
            'name': 'Configurar ambiente de desenvolvimento',
            'description': 'Instalar e configurar todas as ferramentas necessárias',
            'action': actions[0],
            'status': 'completed',
            'priority': 'high',
            'deadline': date.today() - timedelta(days=25),
            'estimated_hours': 8.0
        },
        {
            'name': 'Criar estrutura do banco de dados',
            'description': 'Modelar e implementar o esquema do banco de dados',
            'action': actions[0],
            'status': 'completed',
            'priority': 'high',
            'deadline': date.today() - timedelta(days=20),
            'estimated_hours': 16.0
        },
        {
            'name': 'Desenvolver interface do usuário',
            'description': 'Criar as telas e componentes da interface',
            'action': actions[0],
            'status': 'in_progress',
            'priority': 'medium',
            'deadline': date.today() + timedelta(days=15),
            'estimated_hours': 40.0
        },
        {
            'name': 'Implementar autenticação',
            'description': 'Sistema de login e controle de acesso',
            'action': actions[0],
            'status': 'not_started',
            'priority': 'high',
            'deadline': date.today() + timedelta(days=10),
            'estimated_hours': 12.0
        },
        {
            'name': 'Testes de integração',
            'description': 'Realizar testes de integração entre módulos',
            'action': actions[0],
            'status': 'not_started',
            'priority': 'medium',
            'deadline': date.today() + timedelta(days=25),
            'estimated_hours': 20.0
        },
        
        # Atividades para "Implementação de API"
        {
            'name': 'Definir endpoints da API',
            'description': 'Documentar e definir todos os endpoints necessários',
            'action': actions[1],
            'status': 'in_progress',
            'priority': 'high',
            'deadline': date.today() + timedelta(days=5),
            'estimated_hours': 8.0
        },
        {
            'name': 'Implementar autenticação JWT',
            'description': 'Sistema de autenticação baseado em tokens',
            'action': actions[1],
            'status': 'not_started',
            'priority': 'high',
            'deadline': date.today() + timedelta(days=15),
            'estimated_hours': 16.0
        },
        
        # Atividades para "Testes e Qualidade"
        {
            'name': 'Configurar ambiente de testes',
            'description': 'Preparar ambiente para execução de testes automatizados',
            'action': actions[2],
            'status': 'not_started',
            'priority': 'medium',
            'deadline': date.today() + timedelta(days=5),
            'estimated_hours': 4.0
        },
        {
            'name': 'Escrever testes unitários',
            'description': 'Criar testes unitários para todas as funcionalidades',
            'action': actions[2],
            'status': 'not_started',
            'priority': 'high',
            'deadline': date.today() + timedelta(days=20),
            'estimated_hours': 32.0
        }
    ]
    
    for activity_data in activities_data:
        activity, created = Activity.objects.get_or_create(
            name=activity_data['name'],
            action=activity_data['action'],
            defaults={
                'description': activity_data['description'],
                'assigned_to': admin_worker,
                'status': activity_data['status'],
                'priority': activity_data['priority'],
                'deadline': activity_data['deadline'],
                'estimated_hours': activity_data['estimated_hours']
            }
        )
        if created:
            print(f"✅ Atividade criada: {activity.name}")
    
    print("\n🎉 Dados de exemplo criados com sucesso!")
    print("\n📊 Resumo:")
    print(f"   - {User.objects.count()} usuário(s)")
    print(f"   - {Worker.objects.count()} worker(s)")
    print(f"   - {Action.objects.count()} ação(ões)")
    print(f"   - {Activity.objects.count()} atividade(s)")
    
    print("\n🔑 Credenciais de acesso:")
    print("   Usuário: admin")
    print("   Senha: 1234")
    print("   URL: http://localhost:8000")

if __name__ == '__main__':
    create_sample_data() 