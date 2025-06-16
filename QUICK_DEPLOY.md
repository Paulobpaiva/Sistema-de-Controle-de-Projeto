# ⚡ Deploy Rápido no Railway

## 🚀 Passos Rápidos

### 1. Push para GitHub
```bash
git add .
git commit -m "Configuração Railway"
git push origin main
```

### 2. Railway Setup
1. Acesse [Railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub repo"
3. Selecione seu repositório
4. "Deploy Now"

### 3. Configurar Variáveis
No Railway Dashboard → Variables:
```
SECRET_KEY=sua-chave-secreta-aqui
DJANGO_SETTINGS_MODULE=project.settings_production
```

### 4. Adicionar PostgreSQL
1. "New Service" → "Database" → "PostgreSQL"
2. Aguarde criação
3. Railway conectará automaticamente

### 5. Acessar Sistema
- URL: `https://seu-projeto.railway.app`
- Login: `admin`
- Senha: `1234`

## 🔧 Comandos Úteis

```bash
# Ver logs
railway logs

# Executar comando
railway run python manage.py shell

# Deploy manual
railway up
```

## 💰 Custos
- ~$10/mês (PostgreSQL + App)
- Com $4,10 você testa por algumas semanas

## 🎯 Pronto!
Seu sistema estará online e acessível de qualquer lugar! 🌐 