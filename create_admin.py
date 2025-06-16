#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from activities.models import Worker

def create_admin_user():
    try:
        # Verificar se o usuário admin já existe
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
            # Definir senha
            admin_user.set_password('1234')
            admin_user.save()
            print("✅ Usuário admin criado com sucesso!")
        else:
            # Atualizar senha se o usuário já existe
            admin_user.set_password('1234')
            admin_user.is_active = True
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.save()
            print("✅ Senha do usuário admin atualizada!")
        
        # Criar Worker para o admin
        worker, worker_created = Worker.objects.get_or_create(
            user=admin_user,
            defaults={
                'level': 'admin',
                'department': 'TI',
                'phone': '(11) 99999-9999'
            }
        )
        
        if worker_created:
            print("✅ Perfil de Worker criado para admin!")
        else:
            print("✅ Perfil de Worker já existe para admin!")
        
        print(f"\n🔑 Credenciais de acesso:")
        print(f"   Usuário: admin")
        print(f"   Senha: 1234")
        print(f"   URL: http://localhost:8000")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar usuário admin: {e}")
        return False

if __name__ == '__main__':
    print("🚀 Criando usuário administrador...")
    success = create_admin_user()
    if success:
        print("\n🎉 Configuração concluída! O sistema está pronto para uso.")
    else:
        print("\n💥 Erro na configuração. Verifique os logs acima.") 