# 🚀 Deploy no Hosting Próprio

## 📋 Pré-requisitos

### 1. Acesso ao Hosting
- ✅ Acesso SSH ao servidor
- ✅ Painel de controle (cPanel, Plesk, etc.)
- ✅ Banco de dados configurado
- ✅ Python instalado (versão 3.8+)

### 2. Banco de Dados
- ✅ PostgreSQL ou MySQL configurado
- ✅ Usuário e senha do banco
- ✅ Nome do banco de dados

## 🔧 Configuração do Projeto

### 1. Preparar o Projeto Local

```bash
# Clone o repositório
git clone https://github.com/Paulobpaiva/Sistema-de-Controle-de-Projeto.git
cd Sistema-de-Controle-de-Projeto

# Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
# Configurações do Django
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=False

# Configurações do Banco de Dados
DB_NAME=controle_projetos
DB_USER=seu_usuario_banco
DB_PASSWORD=sua_senha_banco
DB_HOST=localhost
DB_PORT=5432  # ou 3306 para MySQL

# Configurações do Domínio
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com

# Configurações de Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
```

### 3. Configurar Settings

Edite `project/settings_hosting.py`:

```python
# Substitua 'seu-dominio.com' pelo seu domínio real
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'seu-dominio.com',  # SEU DOMÍNIO AQUI
    'www.seu-dominio.com',  # SEU DOMÍNIO AQUI
]
```

## 📤 Upload para o Hosting

### Opção 1: Via FTP/SFTP

1. **Conecte via FTP** ao seu hosting
2. **Faça upload** de todos os arquivos para a pasta pública
3. **Exclua** arquivos desnecessários:
   - `venv/`
   - `.git/`
   - `db.sqlite3`
   - `*.pyc`
   - `__pycache__/`

### Opção 2: Via Git (Recomendado)

```bash
# No seu hosting, clone o repositório
git clone https://github.com/Paulobpaiva/Sistema-de-Controle-de-Projeto.git
cd Sistema-de-Controle-de-Projeto

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## 🗄️ Configurar Banco de Dados

### PostgreSQL

```bash
# Conectar ao PostgreSQL
psql -U seu_usuario -d controle_projetos

# Ou via phpMyAdmin/cPanel
# Crie o banco 'controle_projetos'
```

### MySQL

```bash
# Conectar ao MySQL
mysql -u seu_usuario -p controle_projetos

# Ou via phpMyAdmin/cPanel
# Crie o banco 'controle_projetos'
```

## ⚙️ Configurar o Servidor

### 1. Configurar WSGI

Crie ou edite o arquivo `passenger_wsgi.py` na raiz:

```python
import os
import sys

# Adicionar o diretório do projeto ao path
sys.path.insert(0, os.path.dirname(__file__))

# Configurar variáveis de ambiente
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings_hosting'

# Importar a aplicação Django
from project.wsgi import application
```

### 2. Configurar .htaccess (Apache)

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)$ /passenger_wsgi.py/$1 [QSA,L]

# Configurações de segurança
<Files "*.py">
    Require all denied
</Files>

<Files "passenger_wsgi.py">
    Require all granted
</Files>
```

## 🚀 Deploy

### 1. Executar Migrações

```bash
# Ativar ambiente virtual
source venv/bin/activate

# Configurar variáveis de ambiente
export DJANGO_SETTINGS_MODULE=project.settings_hosting

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar superusuário
python manage.py createsuperuser
```

### 2. Configurar Serviço (Systemd)

Crie `/etc/systemd/system/controle-projetos.service`:

```ini
[Unit]
Description=Controle de Projetos Django
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/caminho/para/seu/projeto
Environment="PATH=/caminho/para/seu/projeto/venv/bin"
Environment="DJANGO_SETTINGS_MODULE=project.settings_hosting"
ExecStart=/caminho/para/seu/projeto/venv/bin/gunicorn project.wsgi:application --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

### 3. Iniciar Serviço

```bash
sudo systemctl daemon-reload
sudo systemctl enable controle-projetos
sudo systemctl start controle-projetos
sudo systemctl status controle-projetos
```

## 🔧 Configurações Específicas por Hosting

### cPanel

1. **Python App**: Crie uma aplicação Python
2. **Banco de Dados**: Use MySQL ou PostgreSQL
3. **Domínio**: Configure o domínio
4. **SSL**: Ative certificado SSL

### Plesk

1. **Domains**: Adicione seu domínio
2. **Python**: Configure aplicação Python
3. **Database**: Crie banco de dados
4. **SSL**: Configure certificado

### VPS/Dedicado

1. **Nginx/Apache**: Configure servidor web
2. **Gunicorn**: Configure servidor WSGI
3. **Firewall**: Configure regras de segurança
4. **SSL**: Configure certificado Let's Encrypt

## 📊 Monitoramento

### Logs

```bash
# Ver logs do Django
tail -f logs/django.log

# Ver logs do sistema
sudo journalctl -u controle-projetos -f

# Ver logs do servidor web
sudo tail -f /var/log/nginx/error.log
```

### Backup

```bash
# Backup do banco
pg_dump controle_projetos > backup_$(date +%Y%m%d).sql

# Backup dos arquivos
tar -czf backup_$(date +%Y%m%d).tar.gz /caminho/do/projeto
```

## 🔍 Troubleshooting

### Erro 500
- Verifique logs do Django
- Verifique configurações do banco
- Verifique permissões de arquivos

### Erro de Conexão com Banco
- Verifique credenciais
- Verifique se o banco existe
- Verifique firewall

### Arquivos Estáticos não Carregam
- Execute `collectstatic`
- Verifique configuração do servidor web
- Verifique permissões

## ✅ Checklist Final

- [ ] Projeto configurado localmente
- [ ] Variáveis de ambiente definidas
- [ ] Banco de dados criado
- [ ] Arquivos enviados para hosting
- [ ] Migrações executadas
- [ ] Superusuário criado
- [ ] Servidor web configurado
- [ ] SSL configurado
- [ ] Domínio apontando
- [ ] Sistema testado

## 🎯 URLs de Teste

- **Sistema**: https://seu-dominio.com
- **Admin**: https://seu-dominio.com/admin/
- **API**: https://seu-dominio.com/api/

---

**Pronto! Seu sistema estará rodando no seu próprio hosting!** 🚀 