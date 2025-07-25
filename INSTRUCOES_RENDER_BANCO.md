# 🔧 Configuração do Banco de Dados no Render

## 🚨 Problema
O deploy foi concluído, mas o banco de dados PostgreSQL do Render começa vazio e precisa ser configurado manualmente.

## 📋 Solução Passo a Passo

### 1. Acessar o Render Dashboard
1. Vá para: https://dashboard.render.com
2. Faça login na sua conta
3. Clique no serviço **"controle-projetos"**

### 2. Abrir o Shell
1. No painel do serviço, clique na aba **"Shell"**
2. Aguarde o shell carregar (pode demorar alguns segundos)

### 3. Executar os Comandos

**Execute os comandos UM POR VEZ, aguardando cada um terminar:**

```bash
# 1. Configurar variável de ambiente
export DJANGO_SETTINGS_MODULE=project.settings_render

# 2. Executar migrações (CRIAR TABELAS)
python manage.py migrate

# 3. Coletar arquivos estáticos
python manage.py collectstatic --noinput

# 4. Criar superusuário (IMPORTANTE!)
python manage.py createsuperuser --username admin --email admin@controleprojetos.com

# 5. Criar dados de exemplo (OPCIONAL)
python create_sample_data.py
```

### 4. Testar o Sistema
1. Após executar todos os comandos, acesse:
   **https://controle-projetos.onrender.com**
2. Faça login com:
   - **Usuário:** `admin`
   - **Senha:** (a que você definiu no comando createsuperuser)

## ⚠️ Comandos Individuais

### Comando 1: Configurar Ambiente
```bash
export DJANGO_SETTINGS_MODULE=project.settings_render
```

### Comando 2: Criar Tabelas
```bash
python manage.py migrate
```
**Aguarde aparecer:** `Operations to perform: ... OK`

### Comando 3: Arquivos Estáticos
```bash
python manage.py collectstatic --noinput
```
**Aguarde aparecer:** `... static files copied`

### Comando 4: Criar Admin
```bash
python manage.py createsuperuser --username admin --email admin@controleprojetos.com
```
**Digite a senha quando pedir** (exemplo: `1234`)

### Comando 5: Dados de Exemplo (Opcional)
```bash
python create_sample_data.py
```

## 🔍 Se Der Erro

### Erro 1: "Service not found"
- Verifique se o serviço está "Live" no Render
- Tente "Manual Deploy" se necessário

### Erro 2: "Database connection failed"
- Aguarde alguns minutos e tente novamente
- O banco pode estar inicializando

### Erro 3: "Permission denied"
- Verifique se está no Shell correto
- Tente recarregar a página do Render

### Erro 4: "Module not found"
- O deploy pode não ter terminado
- Aguarde mais alguns minutos

## 📞 Suporte

Se algum comando der erro:
1. **Copie a mensagem de erro completa**
2. **Cole aqui no chat**
3. **Vou te ajudar a resolver**

## ✅ Após Concluir

- ✅ Sistema funcionando em https://controle-projetos.onrender.com
- ✅ Login com admin funcionando
- ✅ Todas as funcionalidades disponíveis
- ✅ Banco de dados configurado

## 🎯 Resumo Rápido

1. **Acesse:** https://dashboard.render.com
2. **Vá para:** Shell do serviço controle-projetos
3. **Execute:** `export DJANGO_SETTINGS_MODULE=project.settings_render`
4. **Execute:** `python manage.py migrate`
5. **Execute:** `python manage.py collectstatic --noinput`
6. **Execute:** `python manage.py createsuperuser --username admin --email admin@controleprojetos.com`
7. **Teste:** https://controle-projetos.onrender.com

**Pronto!** 🎉 