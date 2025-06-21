#!/usr/bin/env python
"""
Script para redefinir senha de usuário no ambiente local
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from activities.models import Worker

def reset_password():
    print("🔐 Redefinir Senha - Ambiente Local")
    print("=" * 40)
    
    # Listar usuários disponíveis
    users = User.objects.all()
    print("Usuários disponíveis:")
    for i, user in enumerate(users, 1):
        try:
            worker = user.worker
            print(f"{i}. {user.username} (nível: {worker.level})")
        except Worker.DoesNotExist:
            print(f"{i}. {user.username} (sem perfil worker)")
    
    # Escolher usuário
    try:
        choice = int(input("\nEscolha o número do usuário: ")) - 1
        if 0 <= choice < len(users):
            user = users[choice]
        else:
            print("❌ Opção inválida!")
            return
    except ValueError:
        print("❌ Digite um número válido!")
        return
    
    # Definir nova senha
    new_password = input(f"Digite a nova senha para {user.username}: ").strip()
    
    if not new_password:
        print("❌ Senha não pode estar vazia!")
        return
    
    try:
        # Redefinir senha
        user.set_password(new_password)
        user.save()
        
        print(f"✅ Senha de {user.username} redefinida com sucesso!")
        print(f"🔑 Nova senha: {new_password}")
        print(f"🌐 URL local: http://localhost:8000")
        
        # Verificar se tem perfil worker
        try:
            worker = user.worker
            print(f"👤 Perfil worker: {worker.level}")
        except Worker.DoesNotExist:
            print("⚠️  Usuário não tem perfil worker - pode ter problemas no sistema")
            
    except Exception as e:
        print(f"❌ Erro ao redefinir senha: {e}")

if __name__ == "__main__":
    reset_password() 