# 🚨 SOLUÇÃO RÁPIDA - Erro 500

## ⚡ Ação Imediata

### 1. Acesse o Render Dashboard
- Vá para: https://dashboard.render.com
- Faça login na sua conta
- Clique no serviço `controle-projetos`

### 2. Abra o Shell
- Clique em "Shell" no menu lateral
- Aguarde a conexão

### 3. Execute os Comandos

```bash
# Configurar ambiente
export DJANGO_SETTINGS_MODULE=project.settings_render

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar superusuário
python manage.py createsuperuser --username admin --email admin@controleprojetos.com

# Definir senha quando solicitado: (sua senha segura)
```

### 4. Testar Aplicação

```bash
# Verificar se não há erros
python manage.py check

# Testar servidor
python manage.py runserver 0.0.0.0:8000
```

## 🔧 Se Ainda Houver Erro

### Verificar Logs
- No Render Dashboard, clique em "Logs"
- Procure por erros específicos
- Copie os erros para análise

### Verificar Banco
```bash
python manage.py dbshell
# Dentro do shell:
\dt
SELECT * FROM auth_user;
\q
```

## 📞 Credenciais Finais

- **URL**: https://controle-projetos.onrender.com/
- **Login**: admin
- **Senha**: (definida pelo usuário)

## 🚀 Deploy Atualizado

Após executar os comandos:

1. **Commit as mudanças**:
```bash
git add .
git commit -m "Fix: Correção erro 500"
git push origin main
```

2. **Aguardar deploy automático** (5-10 min)

3. **Testar novamente** a aplicação

---

**Se o problema persistir, compartilhe os logs específicos do Render para análise detalhada.** 