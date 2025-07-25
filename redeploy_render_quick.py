#!/usr/bin/env python3
"""
Script rápido para redeploy no Render e resolver banco suspenso
"""

import subprocess
import time

def run_command(command, description):
    """Executa um comando e mostra o resultado"""
    print(f"\n🔄 {description}...")
    print(f"Comando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ {description} - Sucesso!")
            if result.stdout:
                print(f"Saída: {result.stdout}")
        else:
            print(f"❌ {description} - Erro!")
            print(f"Erro: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao executar comando: {e}")
        return False
    
    return True

def quick_redeploy():
    """Faz redeploy rápido no Render"""
    
    print("🚀 REDEPLOY RÁPIDO NO RENDER")
    print("=" * 50)
    
    # 1. Verificar status do git
    print("\n📋 Verificando status do Git...")
    if not run_command("git status", "Verificar status do Git"):
        return False
    
    # 2. Adicionar mudanças
    print("\n📦 Adicionando mudanças...")
    if not run_command("git add .", "Adicionar arquivos"):
        return False
    
    # 3. Fazer commit
    commit_message = "Redeploy Render - Fix banco suspenso"
    if not run_command(f'git commit -m "{commit_message}"', "Fazer commit"):
        return False
    
    # 4. Push para GitHub
    print("\n🚀 Enviando para GitHub...")
    if not run_command("git push origin main", "Push para GitHub"):
        return False
    
    print("\n✅ REDEPLOY INICIADO!")
    print("=" * 50)
    
    # 5. Instruções para o Render
    print("\n📋 AGORA NO RENDER:")
    print("1. Acesse: https://dashboard.render.com")
    print("2. Vá para o serviço 'controle-projetos'")
    print("3. Aguarde o deploy automático (5-10 minutos)")
    print("4. Se o banco estiver suspenso:")
    print("   - Vá para 'Databases'")
    print("   - Clique em 'controle-projetos-db'")
    print("   - Clique em 'Resume' para reativar")
    print("5. Após o deploy, acesse o Shell e execute:")
    print("   export DJANGO_SETTINGS_MODULE=project.settings_render")
    print("   python manage.py migrate")
    print("   python manage.py collectstatic --noinput")
    print("   python manage.py createsuperuser --username admin --email admin@controleprojetos.com")
    print("6. Teste: https://controle-projetos.onrender.com")
    
    return True

def main():
    """Função principal"""
    print("⚡ REDEPLOY RÁPIDO - RENDER")
    print("=" * 40)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('render.yaml'):
        print("❌ Arquivo render.yaml não encontrado!")
        print("Certifique-se de estar no diretório raiz do projeto.")
        return
    
    # Fazer o redeploy
    if quick_redeploy():
        print("\n🎉 REDEPLOY CONCLUÍDO!")
        print("Aguarde 5-10 minutos para o deploy no Render completar.")
        print("Depois siga as instruções acima para configurar o banco.")
    else:
        print("\n❌ ERRO NO REDEPLOY!")
        print("Verifique os erros acima e tente novamente.")

if __name__ == "__main__":
    import os
    main() 