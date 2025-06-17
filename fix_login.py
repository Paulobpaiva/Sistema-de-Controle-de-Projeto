import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

print('⚠️  Criação/atualização automática de admin removida por segurança.')
print('Crie o superusuário manualmente com: python manage.py createsuperuser') 