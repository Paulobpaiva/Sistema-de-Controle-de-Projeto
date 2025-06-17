#!/usr/bin/env python
"""
Script para configurar dados iniciais no Railway
Execute este script após o primeiro deploy
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
django.setup()

from django.contrib.auth.models import User
from django.core.management import call_command
from core.models import Worker
from activities.models import Activity, Action
from datetime import datetime, timedelta

def create_superuser():
    """Criar superusuário se não existir"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@controleprojetos.com',
            password='1234'
        )
        print("✅ Superusuário 'admin' criado com sucesso!")
    else:
        print("ℹ️ Superusuário 'admin' já existe")

def create_worker_profile():
    """Criar perfil de worker para o admin"""
    try:
        admin_user = User.objects.get(username='admin')
        worker, created = Worker.objects.get_or_create(
            user=admin_user,
            defaults={
                'name': 'Administrador',
                'email': 'admin@controleprojetos.com',
                'phone': '(11) 99999-9999',
                'role': 'Gerente',
                'department': 'TI',
                'is_active': True
            }
        )
        if created:
            print("✅ Perfil de worker criado para o admin")
        else:
            print("ℹ️ Perfil de worker já existe para o admin")
    except Exception as e:
        print(f"❌ Erro ao criar perfil de worker: {e}")

def create_sample_data():
    """Criar dados de exemplo"""
    try:
        # Criar algumas atividades de exemplo
        if Activity.objects.count() == 0:
            activities = [
                {
                    'title': 'Desenvolvimento do Sistema',
                    'description': 'Desenvolvimento do sistema de controle de projetos',
                    'status': 'em_andamento',
                    'priority': 'alta',
                    'start_date': datetime.now().date(),
                    'end_date': (datetime.now() + timedelta(days=30)).date(),
                },
                {
                    'title': 'Testes de Qualidade',
                    'description': 'Realizar testes de qualidade do sistema',
                    'status': 'pendente',
                    'priority': 'media',
                    'start_date': datetime.now().date(),
                    'end_date': (datetime.now() + timedelta(days=15)).date(),
                }
            ]
            
            for activity_data in activities:
                Activity.objects.create(**activity_data)
            
            print("✅ Dados de exemplo criados")
        else:
            print("ℹ️ Dados de exemplo já existem")
    except Exception as e:
        print(f"❌ Erro ao criar dados de exemplo: {e}")

def main():
    """Função principal"""
    print("🚀 Configurando dados iniciais no Railway...")
    
    # Executar migrações
    try:
        call_command('migrate')
        print("✅ Migrações executadas com sucesso")
    except Exception as e:
        print(f"❌ Erro nas migrações: {e}")
        return
    
    # Coletar arquivos estáticos
    try:
        call_command('collectstatic', '--noinput')
        print("✅ Arquivos estáticos coletados")
    except Exception as e:
        print(f"❌ Erro ao coletar arquivos estáticos: {e}")
    
    # Criar superusuário
    create_superuser()
    
    # Criar perfil de worker
    create_worker_profile()
    
    # Criar dados de exemplo
    create_sample_data()
    
    print("🎉 Configuração concluída com sucesso!")
    print("📧 Login: admin")
    print("🔑 Senha: 1234")

if __name__ == '__main__':
    main() 