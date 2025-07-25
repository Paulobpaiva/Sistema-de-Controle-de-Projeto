#!/usr/bin/env python3
"""
Script com instruções para configurar o banco de dados no Render
"""

def print_instructions():
    """Imprime as instruções para configurar o banco no Render"""
    
    print("🔧 CONFIGURAÇÃO DO BANCO DE DADOS NO RENDER")
    print("=" * 60)
    print()
    print("O deploy foi concluído, mas o banco precisa ser configurado manualmente.")
    print("Siga estes passos:")
    print()
    
    print("📋 PASSO 1: Acessar o Render Dashboard")
    print("1. Vá para: https://dashboard.render.com")
    print("2. Faça login na sua conta")
    print("3. Clique no serviço 'controle-projetos'")
    print()
    
    print("📋 PASSO 2: Abrir o Shell")
    print("1. No painel do serviço, clique na aba 'Shell'")
    print("2. Aguarde o shell carregar")
    print("3. Execute os comandos abaixo um por vez:")
    print()
    
    print("🔧 COMANDOS PARA EXECUTAR NO SHELL DO RENDER:")
    print("-" * 50)
    
    commands = [
        ("Configurar variável de ambiente", 
         "export DJANGO_SETTINGS_MODULE=project.settings_render"),
        
        ("Executar migrações do banco", 
         "python manage.py migrate"),
        
        ("Coletar arquivos estáticos", 
         "python manage.py collectstatic --noinput"),
        
        ("Criar superusuário admin", 
         "python manage.py createsuperuser --username admin --email admin@controleprojetos.com"),
        
        ("Criar dados de exemplo (opcional)", 
         "python create_sample_data.py"),
    ]
    
    for i, (description, command) in enumerate(commands, 1):
        print(f"{i}. {description}:")
        print(f"   {command}")
        print()
    
    print("📋 PASSO 3: Testar o Sistema")
    print("1. Após executar todos os comandos, acesse:")
    print("   https://controle-projetos.onrender.com")
    print("2. Faça login com:")
    print("   Usuário: admin")
    print("   Senha: (a que você definiu no comando createsuperuser)")
    print()
    
    print("⚠️  IMPORTANTE:")
    print("- Execute os comandos um por vez")
    print("- Aguarde cada comando terminar antes do próximo")
    print("- Se algum comando der erro, copie a mensagem de erro")
    print("- O banco PostgreSQL do Render começa vazio, por isso precisa das migrações")
    print()
    
    print("🔍 SE DER ERRO:")
    print("1. Verifique se o serviço está 'Live' no Render")
    print("2. Tente 'Manual Deploy' se necessário")
    print("3. Copie e cole aqui qualquer erro que aparecer")
    print()
    
    print("✅ APÓS CONCLUIR:")
    print("- O sistema estará funcionando normalmente")
    print("- Todas as funcionalidades estarão disponíveis")
    print("- O banco de dados estará configurado corretamente")

def create_quick_script():
    """Cria um script rápido para copiar e colar no Render"""
    
    print("\n📋 SCRIPT RÁPIDO PARA COPIAR E COLAR NO RENDER:")
    print("-" * 60)
    
    script = '''#!/bin/bash
# Script para configurar o banco no Render
# Copie e cole este script no Shell do Render

echo "🔧 Configurando banco de dados no Render..."

# Configurar variável de ambiente
export DJANGO_SETTINGS_MODULE=project.settings_render
echo "✅ Variável de ambiente configurada"

# Executar migrações
echo "🔄 Executando migrações..."
python manage.py migrate
echo "✅ Migrações concluídas"

# Coletar arquivos estáticos
echo "🔄 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput
echo "✅ Arquivos estáticos coletados"

# Criar superusuário
echo "🔄 Criando superusuário..."
python manage.py createsuperuser --username admin --email admin@controleprojetos.com --noinput
echo "✅ Superusuário criado"

# Criar dados de exemplo (opcional)
echo "🔄 Criando dados de exemplo..."
python create_sample_data.py
echo "✅ Dados de exemplo criados"

echo "🎉 Configuração concluída!"
echo "Acesse: https://controle-projetos.onrender.com"
echo "Login: admin"
echo "Senha: (a senha que você definiu no comando createsuperuser)"
'''
    
    print(script)

def main():
    """Função principal"""
    print_instructions()
    create_quick_script()
    
    print("\n" + "=" * 60)
    print("🎯 RESUMO:")
    print("1. Acesse o Shell do Render")
    print("2. Execute os comandos acima")
    print("3. Teste o sistema")
    print("4. Se der erro, me avise!")
    print("=" * 60)

if __name__ == "__main__":
    main() 