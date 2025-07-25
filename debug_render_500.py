#!/usr/bin/env python3
"""
Script para diagnosticar e resolver erro 500 no Render
"""

def print_debug_instructions():
    """Imprime instruções para debugar erro 500"""
    
    print("🔍 DIAGNOSTICAR ERRO 500 - RENDER")
    print("=" * 60)
    print()
    print("O erro 500 geralmente indica problemas de configuração.")
    print("Vamos resolver isso passo a passo:")
    print()
    
    print("📋 PASSO A PASSO PARA RESOLVER:")
    print()
    
    print("1. 🔍 VERIFICAR LOGS")
    print("   - Acesse: https://dashboard.render.com")
    print("   - Vá para o serviço 'controle-projetos'")
    print("   - Clique na aba 'Logs'")
    print("   - Procure por erros em vermelho")
    print("   - Copie os últimos erros e me envie")
    print()
    
    print("2. ⚙️ CONFIGURAR BANCO NO SHELL")
    print("   - Clique na aba 'Shell' do serviço")
    print("   - Aguarde o shell carregar")
    print("   - Execute os comandos abaixo UM POR VEZ:")
    print()
    
    commands = [
        ("Verificar se Django está funcionando",
         "python -c \"import django; print('Django OK')\""),
        
        ("Verificar configurações",
         "python -c \"from project.settings_render import *; print('Settings OK')\""),
        
        ("Verificar conexão com banco",
         "python -c \"from django.db import connection; connection.ensure_connection(); print('Database OK')\""),
        
        ("Executar migrações (CRIAR TABELAS)",
         "python manage.py migrate"),
        
        ("Coletar arquivos estáticos",
         "python manage.py collectstatic --noinput"),
        
        ("Criar superusuário admin",
         "python manage.py createsuperuser --username admin --email admin@controleprojetos.com"),
    ]
    
    for i, (description, command) in enumerate(commands, 1):
        print(f"   {i}. {description}:")
        print(f"      {command}")
        print()
    
    print("3. 🔄 FAZER NOVO DEPLOY")
    print("   - Após configurar o banco")
    print("   - Clique em 'Manual Deploy'")
    print("   - Aguarde completar")
    print()
    
    print("4. ✅ TESTAR NOVAMENTE")
    print("   - Acesse: https://controle-projetos.onrender.com")
    print("   - Verifique se o erro 500 foi resolvido")
    print()

def print_common_errors():
    """Imprime erros comuns e soluções"""
    
    print("\n🚨 ERROS COMUNS E SOLUÇÕES:")
    print("=" * 40)
    print()
    
    print("❌ Erro: 'No module named django'")
    print("   Solução: Verificar se requirements.txt está correto")
    print()
    
    print("❌ Erro: 'Database connection failed'")
    print("   Solução: Verificar DATABASE_URL no Environment")
    print()
    
    print("❌ Erro: 'Table does not exist'")
    print("   Solução: Executar python manage.py migrate")
    print()
    
    print("❌ Erro: 'Static files not found'")
    print("   Solução: Executar python manage.py collectstatic")
    print()
    
    print("❌ Erro: 'SECRET_KEY not set'")
    print("   Solução: Verificar variável SECRET_KEY no Environment")
    print()

def print_environment_check():
    """Imprime verificação de variáveis de ambiente"""
    
    print("\n🔧 VERIFICAR VARIÁVEIS DE AMBIENTE:")
    print("=" * 40)
    print()
    print("No serviço 'controle-projetos', vá em 'Environment'")
    print("Verifique se estas variáveis estão configuradas:")
    print()
    
    env_vars = [
        "DATABASE_URL",
        "SECRET_KEY", 
        "DEBUG",
        "ALLOWED_HOSTS"
    ]
    
    for var in env_vars:
        print(f"   ✅ {var}")
    
    print()
    print("Se alguma estiver faltando, adicione:")
    print("   - Clique em 'Add Environment Variable'")
    print("   - Nome: NOME_DA_VARIAVEL")
    print("   - Valor: VALOR_DA_VARIAVEL")
    print()

def print_quick_fix():
    """Imprime solução rápida"""
    
    print("\n⚡ SOLUÇÃO RÁPIDA:")
    print("=" * 30)
    print()
    print("Se quiser uma solução mais direta:")
    print()
    print("1. Vá no Shell do serviço")
    print("2. Execute estes comandos:")
    print()
    
    quick_commands = [
        "export DJANGO_SETTINGS_MODULE=project.settings_render",
        "python manage.py migrate",
        "python manage.py collectstatic --noinput",
        "python manage.py createsuperuser --username admin --email admin@controleprojetos.com"
    ]
    
    for cmd in quick_commands:
        print(f"   {cmd}")
    
    print()
    print("3. Faça Manual Deploy")
    print("4. Teste novamente")

def main():
    """Função principal"""
    print("🔍 RESOLVER ERRO 500 - RENDER")
    print("=" * 60)
    print()
    
    print_debug_instructions()
    print_common_errors()
    print_environment_check()
    print_quick_fix()
    
    print("=" * 60)
    print("🎯 PRÓXIMOS PASSOS:")
    print("1. Verifique os logs primeiro")
    print("2. Configure o banco no Shell")
    print("3. Faça novo deploy")
    print("4. Teste o sistema")
    print()
    print("📞 Me envie os logs de erro se precisar de ajuda!")

if __name__ == "__main__":
    main() 