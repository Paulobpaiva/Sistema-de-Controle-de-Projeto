# 🔧 Solução para Erro 500 - Sistema de Controle de Projetos

## 🚨 Problema Identificado

O erro 500 está ocorrendo no login da aplicação em `https://controle-projetos.onrender.com/`

## 🔍 Possíveis Causas

1. **Configuração de Settings incorreta**
2. **Banco de dados não configurado**
3. **Migrações não executadas**
4. **Arquivos estáticos não coletados**
5. **Dependências faltando**

## 🛠️ Solução Passo a Passo

### 1. Verificar Logs no Render

1. Acesse o [Dashboard do Render](https://dashboard.render.com)
2. Vá em seu serviço `controle-projetos`
3. Clique em "Logs"
4. Procure por erros específicos

### 2. Executar Setup Inicial

Via Render Dashboard → Shell, execute:

```bash
# Configurar Django
export DJANGO_SETTINGS_MODULE=project.settings_render

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Criar superusuário
python manage.py createsuperuser --username admin --email admin@controleprojetos.com

# Executar setup inicial
python setup_railway.py
```

### 3. Verificar Banco de Dados

```bash
# Verificar conexão
python manage.py dbshell

# Dentro do shell do banco:
\dt  # Listar tabelas
SELECT * FROM auth_user;  # Verificar usuários
\q  # Sair
```

### 4. Testar Aplicação

```bash
# Testar servidor localmente
python manage.py runserver 0.0.0.0:8000

# Verificar se não há erros de import
python manage.py check
```

### 5. Verificar Configurações

Certifique-se de que:

- ✅ `DJANGO_SETTINGS_MODULE=project.settings_render`
- ✅ `DATABASE_URL` está configurada
- ✅ `SECRET_KEY` está definida
- ✅ Todas as dependências estão instaladas

## 🔧 Correções Aplicadas

### 1. Requirements.txt Atualizado

Adicionada dependência:
```
crispy-bootstrap5==0.7
```

### 2. Settings Render Melhorado

- Logging mais detalhado
- Configurações de segurança
- Tratamento de erros melhorado

### 3. Render.yaml Corrigido

- Configuração correta do `DJANGO_SETTINGS_MODULE`
- Variáveis de ambiente adequadas

## 🚀 Deploy Atualizado

Após as correções:

1. **Commit e Push**:
```bash
git add .
git commit -m "Correção erro 500 - configurações atualizadas"
git push origin main
```

2. **Render fará deploy automático**

3. **Aguardar 5-10 minutos**

4. **Testar novamente**: `https://controle-projetos.onrender.com/`

## 🔍 Diagnóstico

Execute o script de diagnóstico:

```bash
python debug_deploy.py
```

Este script verificará:
- ✅ Variáveis de ambiente
- ✅ Conexão com banco
- ✅ Arquivos estáticos
- ✅ Imports importantes

## 📞 Credenciais de Acesso

Após o setup:
- **URL**: `https://controle-projetos.onrender.com/`
- **Login**: `admin`
- **Senha**: `(definida pelo usuário)`

## 🚨 Se o Problema Persistir

1. **Verificar logs detalhados** no Render Dashboard
2. **Executar diagnóstico completo** com `debug_deploy.py`
3. **Verificar se o banco PostgreSQL está ativo**
4. **Confirmar se todas as migrações foram aplicadas**

## 🎯 Resultado Esperado

Após as correções, o sistema deve:
- ✅ Carregar a página de login sem erro 500
- ✅ Permitir login com credenciais admin/(sua senha)
- ✅ Redirecionar para o dashboard
- ✅ Funcionar normalmente

## 📋 Checklist Final

- [ ] Logs verificados no Render
- [ ] Migrações executadas
- [ ] Arquivos estáticos coletados
- [ ] Superusuário criado
- [ ] Setup inicial executado
- [ ] Aplicação testada
- [ ] Login funcionando

---

**Se ainda houver problemas, verifique os logs específicos no Render Dashboard e compartilhe os erros encontrados.** 