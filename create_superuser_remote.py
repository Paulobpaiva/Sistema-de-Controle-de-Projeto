#!/usr/bin/env python
"""
Script para criar superusuário conectando diretamente no banco do Render
Execute este script localmente com as credenciais do banco do Render
"""

import os
import sys
import django
import dj_database_url

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings_render')
django.setup()

from django.contrib.auth.models import User

def create_superuser_remote():
    print("🔐 Criação de Superusuário - Conexão Remota")
    print("=" * 50)
    
    # Solicitar URL do banco
    database_url = input("Digite a DATABASE_URL do Render (ou pressione Enter para usar variável de ambiente): ").strip()
    
    if database_url:
        # Configurar banco manualmente
        os.environ['DATABASE_URL'] = database_url
    
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
        print("\n🌐 Agora você pode fazer login na aplicação!")
        
    except Exception as e:
        print(f"❌ Erro ao criar superusuário: {e}")
        print("\n💡 Dicas:")
        print("1. Verifique se a DATABASE_URL está correta")
        print("2. Certifique-se de que o banco está acessível")
        print("3. Tente usar a Opção 1 (Variáveis de Ambiente)")

if __name__ == "__main__":
    create_superuser_remote() 