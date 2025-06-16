# 🚀 Deploy no Railway - Sistema de Controle de Projetos

Este guia irá te ajudar a fazer o deploy do sistema de controle de projetos no Railway.

## 📋 Pré-requisitos

- Conta no Railway (https://railway.app)
- Projeto no GitHub
- $4,10 de crédito disponível no Railway

## 🔧 Passos para Deploy

### 1. Preparar o Projeto

Certifique-se de que todos os arquivos de configuração estão no repositório:

- ✅ `Procfile`
- ✅ `requirements.txt` (atualizado)
- ✅ `runtime.txt`
- ✅ `railway.json`
- ✅ `project/settings_production.py`
- ✅ `.gitignore`

### 2. Fazer Push para o GitHub

```bash
git add .
git commit -m "Configuração para deploy no Railway"
git push origin main
```

### 3. Conectar ao Railway

1. Acesse [Railway.app](https://railway.app)
2. Faça login com sua conta
3. Clique em "New Project"
4. Selecione "Deploy from GitHub repo"
5. Escolha seu repositório do sistema de controle de projetos
6. Clique em "Deploy Now"

### 4. Configurar Variáveis de Ambiente

No painel do Railway, vá em "Variables" e adicione:

```
SECRET_KEY=sua-chave-secreta-aqui
DJANGO_SETTINGS_MODULE=project.settings_production
```

**Para gerar uma nova SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. Configurar Banco de Dados

1. No Railway, vá em "New Service"
2. Selecione "Database" → "PostgreSQL"
3. Aguarde a criação
4. Vá em "Variables" e copie a `DATABASE_URL`
5. Cole no seu projeto (Railway fará isso automaticamente)

### 6. Executar Setup Inicial

Após o primeiro deploy, execute o script de configuração:

```bash
# No terminal do Railway ou via Railway CLI
python setup_railway.py
```

Ou via Railway Dashboard:
1. Vá em "Deployments"
2. Clique no último deployment
3. Vá em "Logs"
4. Execute: `python setup_railway.py`

### 7. Configurar Domínio

1. No Railway, vá em "Settings"
2. Em "Domains", clique em "Generate Domain"
3. Copie o domínio gerado (ex: `https://seu-projeto.railway.app`)

## 🔐 Credenciais de Acesso

Após o setup inicial:

- **URL:** `https://seu-projeto.railway.app`
- **Login:** `admin`
- **Senha:** `1234`

## 📊 Monitoramento

### Logs
- Acesse "Deployments" → "Logs" no Railway
- Monitore erros e performance

### Métricas
- Railway fornece métricas de CPU, memória e rede
- Monitore o uso de recursos

## 🔧 Comandos Úteis

### Railway CLI (opcional)
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login
railway login

# Conectar ao projeto
railway link

# Deploy manual
railway up

# Ver logs
railway logs

# Executar comando
railway run python manage.py migrate
```

### Comandos Django
```bash
# Migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar superusuário
python manage.py createsuperuser

# Shell
python manage.py shell
```

## 🚨 Troubleshooting

### Erro de Migração
```bash
# Resetar migrações se necessário
python manage.py migrate --fake-initial
```

### Erro de Arquivos Estáticos
```bash
# Forçar coleta de arquivos estáticos
python manage.py collectstatic --noinput --clear
```

### Erro de Conexão com Banco
- Verifique se a `DATABASE_URL` está correta
- Aguarde alguns minutos após criar o banco

### Erro de SECRET_KEY
- Gere uma nova SECRET_KEY
- Atualize a variável de ambiente no Railway

## 💰 Custos

- **PostgreSQL:** ~$5/mês
- **Aplicação:** ~$5/mês
- **Total estimado:** ~$10/mês

Com $4,10 você pode testar por algumas semanas.

## 🔄 Atualizações

Para atualizar o sistema:

1. Faça as alterações no código
2. Commit e push para o GitHub
3. Railway fará deploy automático
4. Execute migrações se necessário:
   ```bash
   python manage.py migrate
   ```

## 📞 Suporte

Se encontrar problemas:

1. Verifique os logs no Railway
2. Teste localmente primeiro
3. Verifique as variáveis de ambiente
4. Consulte a documentação do Railway

## 🎉 Pronto!

Seu sistema estará disponível em:
`https://seu-projeto.railway.app`

Acesse com:
- **Login:** admin
- **Senha:** 1234

Boa sorte com o deploy! 🚀 