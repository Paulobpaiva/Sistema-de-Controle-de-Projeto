# 📋 Instruções - Sistema de Controle de Projetos

## 🌐 **APLICAÇÃO ONLINE**

**Acesse o sistema:** [https://controle-projetos.onrender.com](https://controle-projetos.onrender.com)

---

## 🚀 Deploy Realizado

O sistema está **ONLINE** e funcionando no Render:

### ✅ **Status**
- **URL:** [https://controle-projetos.onrender.com](https://controle-projetos.onrender.com)
- **Plataforma:** Render (Gratuito)
- **Banco:** PostgreSQL
- **SSL:** HTTPS Ativo
- **Deploy:** Automático

### 🔄 **Atualizações**
- Faça alterações no código
- Commit e push para GitHub
- Render atualiza automaticamente

---

## 💻 Execução Local (Opcional)

Se quiser executar localmente:

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd controle-de-prj
```

### 2. Ative o ambiente virtual
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco
```bash
python manage.py migrate
```

### 5. Execute o servidor
```bash
python manage.py runserver
```

### 6. Acesse
- **URL:** http://localhost:8000

---

## 🔐 Criação do Superusuário

Após o deploy, crie o superusuário com:
```bash
python manage.py createsuperuser
```

Nunca compartilhe usuário e senha de admin publicamente.

---

## 📊 Funcionalidades

### Dashboard
- KPIs em tempo real
- Gráficos interativos
- Progresso visual
- Atividades recentes

### Gestão de Atividades
- CRUD completo
- Status personalizáveis
- Prioridades
- Registro de tempo
- Comentários

### Relatórios
- Relatório de atividades
- Relatório de tempo
- Exportação de dados
- Gráficos interativos

### Usuários
- Níveis de acesso
- Departamentos
- Perfis completos

---

## 🎯 Uso Rápido

### 1. Acesse o sistema
- **Online:** [https://controle-projetos.onrender.com](https://controle-projetos.onrender.com)
- **Local:** http://localhost:8000

### 2. Faça login
- **Usuário:** admin
- **Senha:** 1234

### 3. Complete seu perfil
- Acesse "Perfil" no menu
- Preencha informações adicionais

### 4. Crie uma ação
- Vá para "Ações"
- Clique em "Nova Ação"
- Preencha os dados

### 5. Crie atividades
- Vá para "Atividades"
- Clique em "Nova Atividade"
- Associe à ação criada

### 6. Visualize o dashboard
- Acesse o dashboard principal
- Veja KPIs e gráficos
- Acompanhe o progresso

---

## 🔧 Comandos Úteis

### Django
```bash
# Verificar sistema
python manage.py check

# Migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Shell
python manage.py shell
```

### Git
```bash
# Ver status
git status

# Adicionar mudanças
git add .

# Commit
git commit -m "Descrição das mudanças"

# Push
git push origin main
```

---

## 🚨 Solução de Problemas

### Erro de login
- Verifique se o usuário existe
- Confirme a senha
- Tente criar novo superusuário

### Erro de migração
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erro de dependências
```bash
pip install --upgrade -r requirements.txt
```

### Erro de banco
```bash
python manage.py flush
python manage.py migrate
```

---

## 📞 Suporte

- **Documentação:** README.md
- **Issues:** GitHub Issues
- **Deploy:** Render Dashboard

---

**🎉 Sistema online e funcionando!**

**Acesse:** [https://controle-projetos.onrender.com](https://controle-projetos.onrender.com) 