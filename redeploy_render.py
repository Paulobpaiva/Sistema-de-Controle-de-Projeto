#!/usr/bin/env python3
"""
Script para redeploy no Render e restauração do banco de dados
"""

import os
import sys
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

def redeploy_render():
    """Faz o redeploy no Render"""
    
    print("🚀 INICIANDO REDEPLOY NO RENDER")
    print("=" * 50)
    
    # 1. Verificar se estamos no diretório correto
    if not os.path.exists('render.yaml'):
        print("❌ Arquivo render.yaml não encontrado!")
        print("Certifique-se de estar no diretório raiz do projeto.")
        return False
    
    # 2. Verificar status do git
    print("\n📋 Verificando status do Git...")
    if not run_command("git status", "Verificar status do Git"):
        return False
    
    # 3. Adicionar todas as mudanças
    print("\n📦 Adicionando mudanças ao Git...")
    if not run_command("git add .", "Adicionar arquivos"):
        return False
    
    # 4. Fazer commit
    commit_message = "Redeploy Render - Correção banco de dados e melhorias JS"
    if not run_command(f'git commit -m "{commit_message}"', "Fazer commit"):
        return False
    
    # 5. Push para GitHub
    print("\n🚀 Enviando para GitHub...")
    if not run_command("git push origin main", "Push para GitHub"):
        return False
    
    print("\n✅ REDEPLOY INICIADO COM SUCESSO!")
    print("=" * 50)
    
    # 6. Instruções para o Render
    print("\n📋 PRÓXIMOS PASSOS NO RENDER:")
    print("1. Acesse: https://dashboard.render.com")
    print("2. Vá para seu serviço 'controle-projetos'")
    print("3. Aguarde o deploy automático (5-10 minutos)")
    print("4. Após o deploy, acesse o Shell e execute:")
    print("   export DJANGO_SETTINGS_MODULE=project.settings_render")
    print("   python manage.py migrate")
    print("   python manage.py collectstatic --noinput")
    print("   python manage.py createsuperuser --username admin --email admin@controleprojetos.com")
    print("5. Acesse: https://controle-projetos.onrender.com")
    
    return True

def check_render_status():
    """Verifica o status do deploy no Render"""
    print("\n🔍 VERIFICANDO STATUS DO RENDER:")
    print("1. Acesse: https://dashboard.render.com")
    print("2. Vá para o serviço 'controle-projetos'")
    print("3. Verifique se o status está 'Live'")
    print("4. Se estiver 'Failed', clique em 'Manual Deploy'")
    print("5. Aguarde o deploy completar")

def main():
    """Função principal"""
    print("🎯 REDEPLOY RENDER - SISTEMA DE CONTROLE DE PROJETOS")
    print("=" * 60)
    
    # Verificar se o usuário quer continuar
    response = input("\nDeseja fazer o redeploy no Render? (s/n): ").lower()
    if response not in ['s', 'sim', 'y', 'yes']:
        print("❌ Redeploy cancelado!")
        return
    
    # Fazer o redeploy
    if redeploy_render():
        print("\n🎉 REDEPLOY CONCLUÍDO!")
        print("Aguarde 5-10 minutos para o deploy no Render completar.")
        print("Depois acesse: https://controle-projetos.onrender.com")
        
        # Perguntar se quer verificar o status
        check = input("\nDeseja ver instruções para verificar o status? (s/n): ").lower()
        if check in ['s', 'sim', 'y', 'yes']:
            check_render_status()
    else:
        print("\n❌ ERRO NO REDEPLOY!")
        print("Verifique os erros acima e tente novamente.")

if __name__ == "__main__":
    main() 