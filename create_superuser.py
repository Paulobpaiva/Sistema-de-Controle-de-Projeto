#!/usr/bin/env python
"""
Script para criar superusuário de forma segura
Execute este script localmente ou no servidor para criar um superusuário
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

def create_superuser():
    print("🔐 Criação de Superusuário")
    print("=" * 40)
    
    # Solicitar credenciais
    username = input("Digite o nome de usuário: ").strip()
    email = input("Digite o email: ").strip()
    password = input("Digite a senha: ").strip()
    
    if not username or not password:
        print("❌ Usuário e senha são obrigatórios!")
        return
    
    try:
        # Verificar se o usuário já existe
        if User.objects.filter(username=username).exists():
            print(f"⚠️  Usuário '{username}' já existe!")
            update = input("Deseja atualizar a senha? (s/n): ").lower().strip()
            if update == 's':
                user = User.objects.get(username=username)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.is_active = True
                user.save()
                print("✅ Senha atualizada com sucesso!")
            else:
                print("❌ Operação cancelada.")
            return
        
        # Criar novo superusuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        
        print("✅ Superusuário criado com sucesso!")
        print(f"👤 Usuário: {username}")
        print(f"📧 Email: {email}")
        print("🔑 Senha: [senha digitada]")
        
    except Exception as e:
        print(f"❌ Erro ao criar superusuário: {e}")

if __name__ == "__main__":
    create_superuser() 