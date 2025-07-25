#!/usr/bin/env python3
"""
Script para facilitar o deploy no hosting próprio
"""

import os
import sys
import subprocess
import getpass

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

def create_env_file():
    """Cria arquivo .env com configurações do hosting"""
    
    print("\n🔧 CONFIGURAÇÃO DO ARQUIVO .ENV")
    print("=" * 50)
    
    # Coletar informações do usuário
    print("\n📝 Preencha as informações do seu hosting:")
    
    secret_key = input("SECRET_KEY (deixe vazio para gerar automaticamente): ").strip()
    if not secret_key:
        secret_key = "sua_chave_secreta_aqui_altere_em_producao"
    
    db_name = input("Nome do banco de dados: ").strip() or "controle_projetos"
    db_user = input("Usuário do banco: ").strip() or "root"
    db_password = getpass.getpass("Senha do banco: ").strip()
    db_host = input("Host do banco (localhost): ").strip() or "localhost"
    db_port = input("Porta do banco (5432 para PostgreSQL, 3306 para MySQL): ").strip() or "5432"
    
    domain = input("Seu domínio (ex: meusite.com): ").strip()
    
    # Criar conteúdo do .env
    env_content = f"""# Configurações do Django
SECRET_KEY={secret_key}
DEBUG=False

# Configurações do Banco de Dados
DB_NAME={db_name}
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_HOST={db_host}
DB_PORT={db_port}

# Configurações do Domínio
ALLOWED_HOSTS={domain},www.{domain}

# Configurações de Email (opcional)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=seu_email@gmail.com
# EMAIL_HOST_PASSWORD=sua_senha_de_app
"""
    
    # Salvar arquivo .env
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"\n✅ Arquivo .env criado com sucesso!")
    print("⚠️  IMPORTANTE: Nunca commite este arquivo no Git!")
    
    return True

def create_passenger_wsgi():
    """Cria arquivo passenger_wsgi.py para hosting"""
    
    passenger_content = '''import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(__file__))

# Configurar variáveis de ambiente
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings_hosting'

# Importar a aplicação Django
from project.wsgi import application
'''
    
    with open('passenger_wsgi.py', 'w') as f:
        f.write(passenger_content)
    
    print("✅ Arquivo passenger_wsgi.py criado!")

def create_htaccess():
    """Cria arquivo .htaccess para Apache"""
    
    htaccess_content = '''RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /passenger_wsgi.py/$1 [QSA,L]

# Configurações de segurança
<Files "*.py">
    Require all denied
</Files>

<Files "passenger_wsgi.py">
    Require all granted
</Files>

# Configurações de cache para arquivos estáticos
<FilesMatch "\\.(css|js|png|jpg|jpeg|gif|ico|svg)$">
    ExpiresActive On
    ExpiresDefault "access plus 1 month"
</FilesMatch>
'''
    
    with open('.htaccess', 'w') as f:
        f.write(htaccess_content)
    
    print("✅ Arquivo .htaccess criado!")

def prepare_deploy():
    """Prepara o projeto para deploy"""
    
    print("\n🚀 PREPARANDO PROJETO PARA DEPLOY")
    print("=" * 50)
    
    # 1. Criar arquivo .env
    if not create_env_file():
        return False
    
    # 2. Criar passenger_wsgi.py
    create_passenger_wsgi()
    
    # 3. Criar .htaccess
    create_htaccess()
    
    # 4. Coletar arquivos estáticos
    if not run_command("python manage.py collectstatic --noinput", "Coletar arquivos estáticos"):
        return False
    
    # 5. Verificar se há migrações pendentes
    if not run_command("python manage.py showmigrations", "Verificar migrações"):
        return False
    
    print("\n✅ PROJETO PREPARADO PARA DEPLOY!")
    print("=" * 50)
    
    return True

def generate_deploy_instructions():
    """Gera instruções específicas para deploy"""
    
    print("\n📋 INSTRUÇÕES PARA DEPLOY NO HOSTING")
    print("=" * 60)
    
    instructions = """
1. 📤 UPLOAD DOS ARQUIVOS:
   - Conecte via FTP/SFTP ao seu hosting
   - Faça upload de TODOS os arquivos para a pasta pública
   - EXCLUA estes arquivos:
     * venv/
     * .git/
     * db.sqlite3
     * *.pyc
     * __pycache__/

2. 🗄️ CONFIGURAR BANCO DE DADOS:
   - Acesse o painel do seu hosting
   - Crie um banco de dados (MySQL ou PostgreSQL)
   - Use as credenciais do arquivo .env

3. ⚙️ CONFIGURAR PYTHON:
   - No painel do hosting, configure Python 3.8+
   - Aponte para o arquivo passenger_wsgi.py
   - Configure as variáveis de ambiente do .env

4. 🔧 EXECUTAR COMANDOS:
   - Acesse o terminal do hosting
   - Execute:
     python manage.py migrate
     python manage.py createsuperuser

5. 🌐 CONFIGURAR DOMÍNIO:
   - Aponte seu domínio para a pasta do projeto
   - Configure SSL se disponível

6. ✅ TESTAR:
   - Acesse: https://seu-dominio.com
   - Teste login e funcionalidades
"""
    
    print(instructions)
    
    # Salvar instruções em arquivo
    with open('INSTRUCOES_DEPLOY_HOSTING.txt', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Instruções salvas em 'INSTRUCOES_DEPLOY_HOSTING.txt'")

def main():
    """Função principal"""
    print("🎯 DEPLOY NO HOSTING PRÓPRIO - SISTEMA DE CONTROLE DE PROJETOS")
    print("=" * 70)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('manage.py'):
        print("❌ Arquivo manage.py não encontrado!")
        print("Certifique-se de estar no diretório raiz do projeto.")
        return
    
    # Menu de opções
    print("\nEscolha uma opção:")
    print("1. Preparar projeto para deploy")
    print("2. Gerar instruções de deploy")
    print("3. Fazer tudo (preparar + instruções)")
    print("4. Sair")
    
    choice = input("\nOpção: ").strip()
    
    if choice == "1":
        prepare_deploy()
    elif choice == "2":
        generate_deploy_instructions()
    elif choice == "3":
        if prepare_deploy():
            generate_deploy_instructions()
    elif choice == "4":
        print("👋 Até logo!")
        return
    else:
        print("❌ Opção inválida!")
        return
    
    print("\n🎉 Processo concluído!")
    print("Agora siga as instruções para fazer o deploy no seu hosting.")

if __name__ == "__main__":
    main() 