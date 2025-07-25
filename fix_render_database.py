#!/usr/bin/env python3
"""
Script para resolver problema do banco de dados suspenso no Render
"""

def print_fix_instructions():
    """Imprime instruções para resolver o banco suspenso no Render"""
    
    print("🔧 RESOLVENDO BANCO DE DADOS SUSPENSO NO RENDER")
    print("=" * 60)
    print()
    print("O banco de dados está suspenso porque o Render suspende bancos gratuitos")
    print("quando ficam inativos por muito tempo. Vamos resolver isso!")
    print()
    
    print("📋 SOLUÇÃO PASSO A PASSO:")
    print()
    
    print("1. 🌐 ACESSAR O RENDER DASHBOARD")
    print("   - Vá para: https://dashboard.render.com")
    print("   - Faça login na sua conta")
    print("   - Clique no serviço 'controle-projetos'")
    print()
    
    print("2. 🔄 REATIVAR O BANCO DE DADOS")
    print("   - No painel, procure por 'Databases' ou 'PostgreSQL'")
    print("   - Clique no banco 'controle-projetos-db'")
    print("   - Procure por botão 'Resume' ou 'Activate'")
    print("   - Clique para reativar o banco")
    print("   - Aguarde alguns minutos para inicializar")
    print()
    
    print("3. 🔄 FAZER MANUAL DEPLOY")
    print("   - No serviço 'controle-projetos', clique em 'Manual Deploy'")
    print("   - Aguarde o deploy completar (5-10 minutos)")
    print("   - Verifique se o status está 'Live'")
    print()
    
    print("4. ⚙️ CONFIGURAR O BANCO")
    print("   - Clique na aba 'Shell' do serviço")
    print("   - Aguarde o shell carregar")
    print("   - Execute os comandos abaixo UM POR VEZ:")
    print()
    
    commands = [
        ("Configurar ambiente", 
         "export DJANGO_SETTINGS_MODULE=project.settings_render"),
        
        ("Executar migrações", 
         "python manage.py migrate"),
        
        ("Coletar arquivos estáticos", 
         "python manage.py collectstatic --noinput"),
        
        ("Criar superusuário", 
         "python manage.py createsuperuser --username admin --email admin@controleprojetos.com"),
        
        ("Criar dados de exemplo (opcional)", 
         "python create_sample_data.py"),
    ]
    
    for i, (description, command) in enumerate(commands, 1):
        print(f"   {i}. {description}:")
        print(f"      {command}")
        print()
    
    print("5. ✅ TESTAR O SISTEMA")
    print("   - Acesse: https://controle-projetos.onrender.com")
    print("   - Faça login com admin e a senha que você definiu")
    print("   - Teste as funcionalidades")
    print()

def print_alternative_solutions():
    """Imprime soluções alternativas"""
    
    print("🔄 SOLUÇÕES ALTERNATIVAS:")
    print("=" * 40)
    print()
    
    print("📊 OPÇÃO 1: UPGRADE PARA PLANO PAGO")
    print("   - Vá para as configurações do banco no Render")
    print("   - Clique em 'Upgrade'")
    print("   - Escolha um plano pago (a partir de $7/mês)")
    print("   - Bancos pagos não são suspensos")
    print()
    
    print("🔄 OPÇÃO 2: RECRIAR O BANCO")
    print("   - Delete o banco atual")
    print("   - Crie um novo banco PostgreSQL")
    print("   - Atualize as variáveis de ambiente")
    print("   - Faça novo deploy")
    print()
    
    print("🌐 OPÇÃO 3: USAR BANCO EXTERNO")
    print("   - Use um banco PostgreSQL externo (Railway, Supabase, etc.)")
    print("   - Configure as variáveis de ambiente")
    print("   - Faça deploy")
    print()

def print_prevention_tips():
    """Imprime dicas para evitar suspensão"""
    
    print("💡 DICAS PARA EVITAR SUSPENSÃO:")
    print("=" * 40)
    print()
    
    print("⏰ ACESSO REGULAR")
    print("   - Acesse o sistema pelo menos uma vez por semana")
    print("   - Isso mantém o banco ativo")
    print()
    
    print("🤖 AUTOMAÇÃO")
    print("   - Configure um cron job para acessar periodicamente")
    print("   - Use serviços como UptimeRobot para monitorar")
    print()
    
    print("📊 MONITORAMENTO")
    print("   - Verifique o status do Render regularmente")
    print("   - Configure alertas por email")
    print()

def main():
    """Função principal"""
    print("🚨 BANCO DE DADOS SUSPENSO NO RENDER - SOLUÇÃO")
    print("=" * 70)
    print()
    
    print_fix_instructions()
    print_alternative_solutions()
    print_prevention_tips()
    
    print("=" * 70)
    print("🎯 RESUMO:")
    print("1. Reative o banco no Render Dashboard")
    print("2. Faça Manual Deploy")
    print("3. Configure via Shell")
    print("4. Teste o sistema")
    print()
    print("📞 Se precisar de ajuda, me avise!")

if __name__ == "__main__":
    main() 