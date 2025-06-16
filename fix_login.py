import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User

# Criar ou atualizar usuário admin
try:
    # Tentar obter usuário existente
    admin_user = User.objects.get(username='admin')
    print(f"Usuário admin encontrado: {admin_user.username}")
    
    # Atualizar senha
    admin_user.set_password('1234')
    admin_user.is_active = True
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()
    print("Senha atualizada para: 1234")
    
except User.DoesNotExist:
    # Criar novo usuário
    admin_user = User.objects.create_user(
        username='admin',
        email='admin@example.com',
        password='1234',
        first_name='Administrador',
        last_name='Sistema',
        is_staff=True,
        is_superuser=True,
        is_active=True
    )
    print("Usuário admin criado com senha: 1234")

print("\nCredenciais:")
print("Usuário: admin")
print("Senha: 1234")
print("URL: http://localhost:8000") 