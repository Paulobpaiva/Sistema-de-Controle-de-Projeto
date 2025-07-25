#!/usr/bin/env python3
"""
Script com instruções para remover e recriar banco de dados no Render
"""

def print_recreate_instructions():
    """Imprime instruções para recriar o banco no Render"""
    
    print("🗄️ REMOVER E RECRIAR BANCO DE DADOS NO RENDER")
    print("=" * 60)
    print()
    print("Vamos remover o banco atual e criar um novo para resolver")
    print("problemas de suspensão e configuração.")
    print()
    
    print("📋 PASSO A PASSO:")
    print()
    
    print("1. 🗑️ REMOVER BANCO ATUAL")
    print("   - Acesse: https://dashboard.render.com")
    print("   - Faça login na sua conta")
    print("   - Vá para a seção 'Databases'")
    print("   - Clique em 'controle-projetos-db'")
    print("   - Clique em 'Settings' (engrenagem)")
    print("   - Role até o final da página")
    print("   - Clique em 'Delete Database'")
    print("   - Confirme a exclusão")
    print("   - Aguarde a exclusão completar")
    print()
    
    print("2. 🆕 CRIAR NOVO BANCO")
    print("   - No painel principal, clique em 'New +'")
    print("   - Selecione 'PostgreSQL'")
    print("   - Nome: 'controle-projetos-db'")
    print("   - Database: 'controle_projetos'")
    print("   - User: 'controle_projetos_user'")
    print("   - Plano: 'Free'")
    print("   - Clique em 'Create Database'")
    print("   - Aguarde a criação (2-3 minutos)")
    print()
    
    print("3. 🔗 CONECTAR BANCO AO SERVIÇO")
    print("   - Vá para o serviço 'controle-projetos'")
    print("   - Clique em 'Environment'")
    print("   - Procure por 'DATABASE_URL'")
    print("   - Clique em 'Edit'")
    print("   - Clique em 'Connect Database'")
    print("   - Selecione o novo banco 'controle-projetos-db'")
    print("   - Clique em 'Connect'")
    print()
    
    print("4. 🔄 FAZER MANUAL DEPLOY")
    print("   - No serviço 'controle-projetos'")
    print("   - Clique em 'Manual Deploy'")
    print("   - Aguarde o deploy completar (5-10 minutos)")
    print("   - Verifique se o status está 'Live'")
    print()
    
    print("5. ⚙️ CONFIGURAR NOVO BANCO")
    print("   - Clique na aba 'Shell' do serviço")
    print("   - Aguarde o shell carregar")
    print("   - Execute os comandos abaixo UM POR VEZ:")
    print()
    
    commands = [
        ("Configurar ambiente", 
         "export DJANGO_SETTINGS_MODULE=project.settings_render"),
        
        ("Executar migrações (CRIAR TABELAS)", 
         "python manage.py migrate"),
        
        ("Coletar arquivos estáticos", 
         "python manage.py collectstatic --noinput"),
        
        ("Criar superusuário admin", 
         "python manage.py createsuperuser --username admin --email admin@controleprojetos.com"),
        
        ("Criar dados de exemplo (opcional)", 
         "python create_sample_data.py"),
    ]
    
    for i, (description, command) in enumerate(commands, 1):
        print(f"   {i}. {description}:")
        print(f"      {command}")
        print()
    
    print("6. ✅ TESTAR SISTEMA")
    print("   - Acesse: https://controle-projetos.onrender.com")
    print("   - Faça login com admin e a senha que você definiu")
    print("   - Teste todas as funcionalidades")
    print()

def print_alternative_method():
    """Imprime método alternativo usando Blueprint"""
    
    print("\n🔄 MÉTODO ALTERNATIVO - BLUEPRINT:")
    print("=" * 40)
    print()
    print("Se preferir, pode recriar tudo do zero:")
    print()
    print("1. Delete o serviço atual")
    print("2. Delete o banco atual")
    print("3. Vá em 'New +' → 'Blueprint'")
    print("4. Conecte seu repositório GitHub")
    print("5. Clique em 'Apply'")
    print("6. Render cria tudo automaticamente")
    print("7. Configure via Shell")
    print()

def print_troubleshooting():
    """Imprime troubleshooting"""
    
    print("\n🔍 TROUBLESHOOTING:")
    print("=" * 30)
    print()
    
    print("❌ Erro: 'Database not found'")
    print("   - Verifique se o banco foi criado")
    print("   - Verifique se a conexão está correta")
    print()
    
    print("❌ Erro: 'Connection refused'")
    print("   - Aguarde mais alguns minutos")
    print("   - O banco pode estar inicializando")
    print()
    
    print("❌ Erro: 'Permission denied'")
    print("   - Verifique se está no Shell correto")
    print("   - Tente recarregar a página")
    print()
    
    print("❌ Erro: 'Table already exists'")
    print("   - Execute: python manage.py migrate --fake-initial")
    print()

def main():
    """Função principal"""
    print("🗄️ RECRIAR BANCO DE DADOS - RENDER")
    print("=" * 60)
    print()
    
    print_recreate_instructions()
    print_alternative_method()
    print_troubleshooting()
    
    print("=" * 60)
    print("🎯 RESUMO:")
    print("1. Delete banco atual")
    print("2. Crie novo banco")
    print("3. Conecte ao serviço")
    print("4. Faça deploy")
    print("5. Configure via Shell")
    print("6. Teste o sistema")
    print()
    print("📞 Se precisar de ajuda, me avise!")

if __name__ == "__main__":
    main() 