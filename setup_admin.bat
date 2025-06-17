@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo ⚠️  Criação automática de admin removida por segurança.
echo Crie o superusuário manualmente com: python manage.py createsuperuser

echo.
pause 