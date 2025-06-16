@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo Criando usuario admin...
python manage.py shell -c "from django.contrib.auth.models import User; admin_user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com', 'first_name': 'Administrador', 'last_name': 'Sistema', 'is_staff': True, 'is_superuser': True, 'is_active': True}); admin_user.set_password('1234'); admin_user.save(); print('Usuario admin criado/atualizado com sucesso!')"

echo.
echo Credenciais de acesso:
echo Usuario: admin
echo Senha: 1234
echo URL: http://localhost:8000
echo.
pause 