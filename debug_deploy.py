#!/usr/bin/env python
"""
Script de diagnóstico para verificar a configuração do deploy
Execute este script para identificar problemas
"""

import os
import sys
import django

def check_environment():
    """Verificar variáveis de ambiente"""
    print("🔍 Verificando variáveis de ambiente...")
    
    required_vars = ['DATABASE_URL', 'SECRET_KEY', 'DJANGO_SETTINGS_MODULE']
    
    for var in required_vars:
        value = os.environ.get(var)
        if value:
            print(f"✅ {var}: {'*' * 10 if 'SECRET' in var else value[:50]}")
        else:
            print(f"❌ {var}: NÃO DEFINIDA")
    
    print()

def check_database():
    """Verificar conexão com banco de dados"""
    print("🔍 Verificando conexão com banco de dados...")
    
    try:
        # Configurar Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
        django.setup()
        
        from django.db import connection
        from django.core.management import execute_from_command_line
        
        # Testar conexão
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Conexão com banco: OK (resultado: {result})")
        
        # Verificar migrações
        print("🔍 Verificando migrações...")
        from django.core.management import call_command
        call_command('showmigrations')
        
    except Exception as e:
        print(f"❌ Erro no banco: {e}")
    
    print()

def check_static_files():
    """Verificar arquivos estáticos"""
    print("🔍 Verificando arquivos estáticos...")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
        django.setup()
        
        from django.conf import settings
        from django.core.management import call_command
        
        print(f"✅ STATIC_ROOT: {settings.STATIC_ROOT}")
        print(f"✅ STATIC_URL: {settings.STATIC_URL}")
        
        # Tentar coletar arquivos estáticos
        call_command('collectstatic', '--noinput', '--dry-run')
        print("✅ Coleta de arquivos estáticos: OK")
        
    except Exception as e:
        print(f"❌ Erro nos arquivos estáticos: {e}")
    
    print()

def check_imports():
    """Verificar imports importantes"""
    print("🔍 Verificando imports...")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
        django.setup()
        
        # Testar imports importantes
        from django.contrib.auth.models import User
        from activities.models import Activity, Action, Worker
        from accounts.models import UserProfile
        
        print("✅ Imports principais: OK")
        
        # Verificar se há dados
        user_count = User.objects.count()
        activity_count = Activity.objects.count()
        action_count = Action.objects.count()
        
        print(f"✅ Usuários: {user_count}")
        print(f"✅ Atividades: {activity_count}")
        print(f"✅ Ações: {action_count}")
        
    except Exception as e:
        print(f"❌ Erro nos imports: {e}")
    
    print()

def main():
    """Função principal"""
    print("🚀 Diagnóstico do Sistema de Controle de Projetos")
    print("=" * 50)
    
    check_environment()
    check_database()
    check_static_files()
    check_imports()
    
    print("🎯 Diagnóstico concluído!")

if __name__ == '__main__':
    main() 