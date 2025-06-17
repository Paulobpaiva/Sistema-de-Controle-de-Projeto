Write-Host "Ativando ambiente virtual..." -ForegroundColor Green
& "venv\Scripts\Activate.ps1"

Write-Host "⚠️  Criação automática de admin removida por segurança." -ForegroundColor Yellow
Write-Host "Crie o superusuário manualmente com: python manage.py createsuperuser" -ForegroundColor White

Write-Host "\nPressione qualquer tecla para continuar..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown") 

Write-Host "Configurando variáveis de ambiente..." -ForegroundColor Green
$env:SECRET_KEY = "sua-chave-secreta-aqui"
$env:DJANGO_SETTINGS_MODULE = "project.settings_production"
Write-Host "Variáveis de ambiente configuradas com sucesso!" -ForegroundColor Green 