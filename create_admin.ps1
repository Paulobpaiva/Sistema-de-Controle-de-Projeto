Write-Host "Ativando ambiente virtual..." -ForegroundColor Green
& "venv\Scripts\Activate.ps1"

Write-Host "Criando usuario admin..." -ForegroundColor Green
python manage.py shell -c "
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Criar ou atualizar usuário admin
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'first_name': 'Administrador',
        'last_name': 'Sistema',
        'is_staff': True,
        'is_superuser': True,
        'is_active': True,
        'password': make_password('1234')
    }
)

if not created:
    admin_user.set_password('1234')
    admin_user.is_active = True
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.save()

print('Usuario admin criado/atualizado com sucesso!')
"

Write-Host "`nCredenciais de acesso:" -ForegroundColor Yellow
Write-Host "Usuario: admin" -ForegroundColor White
Write-Host "Senha: 1234" -ForegroundColor White
Write-Host "URL: http://localhost:8000" -ForegroundColor White
Write-Host "`nPressione qualquer tecla para continuar..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 

Write-Host "Configurando variáveis de ambiente..." -ForegroundColor Green
$env:SECRET_KEY = "sua-chave-secreta-aqui"
$env:DJANGO_SETTINGS_MODULE = "project.settings_production"
Write-Host "Variáveis de ambiente configuradas com sucesso!" -ForegroundColor Green 