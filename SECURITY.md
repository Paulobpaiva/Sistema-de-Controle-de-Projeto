# 🔒 Segurança - Sistema de Controle de Projetos

## ⚠️ IMPORTANTE: Dados Sensíveis

Este projeto é **PÚBLICO** no GitHub. Nunca commite dados sensíveis!

## 🚨 O que NÃO commitar:

- ❌ **SECRET_KEY** do Django
- ❌ **Senhas** de banco de dados
- ❌ **Credenciais** de email
- ❌ **Chaves de API**
- ❌ **Arquivos .env** com dados reais
- ❌ **db.sqlite3** (banco local)

## ✅ O que é seguro commitar:

- ✅ Código fonte
- ✅ Templates HTML
- ✅ Arquivos de configuração (sem dados sensíveis)
- ✅ Migrações do Django
- ✅ Requirements.txt
- ✅ Arquivos de documentação

## 🔧 Configuração Segura

### 1. Variáveis de Ambiente
Use o arquivo `env.example` como modelo:

```bash
# Copie o arquivo de exemplo
cp env.example .env

# Edite o .env com seus dados reais
# NUNCA commite o arquivo .env!
```

### 2. SECRET_KEY
Gere uma nova SECRET_KEY para produção:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 3. Banco de Dados
- **Desenvolvimento**: SQLite (já no .gitignore)
- **Produção**: PostgreSQL (configurado via variáveis de ambiente)

## 🛡️ Configurações de Segurança

### Django Settings
- ✅ `DEBUG = False` em produção
- ✅ `SECURE_BROWSER_XSS_FILTER = True`
- ✅ `SECURE_CONTENT_TYPE_NOSNIFF = True`
- ✅ `X_FRAME_OPTIONS = 'DENY'`

### Render (Produção)
- ✅ Variáveis de ambiente configuradas
- ✅ SECRET_KEY gerada automaticamente
- ✅ Banco PostgreSQL isolado

## 📋 Checklist de Segurança

Antes de fazer commit:

- [ ] Verifique se não há SECRET_KEY hardcoded
- [ ] Verifique se não há senhas no código
- [ ] Verifique se o .env não está sendo commitado
- [ ] Verifique se db.sqlite3 não está sendo commitado
- [ ] Teste localmente antes do push

## 🔍 Verificação Automática

Execute este comando para verificar dados sensíveis:

```bash
# Verificar por dados sensíveis
grep -r "SECRET_KEY\|password\|senha\|admin123" . --exclude-dir=venv --exclude-dir=.git
```

## 🚨 Se encontrar dados sensíveis:

1. **Imediatamente**: Remova do commit
2. **Gere novos**: SECRET_KEY, senhas, etc.
3. **Atualize**: Variáveis de ambiente
4. **Teste**: Se tudo funciona
5. **Commit**: Apenas código seguro

## 📞 Suporte

Se encontrar dados sensíveis no histórico:
1. Use `git filter-branch` para remover
2. Force push para limpar o histórico
3. Gere novas credenciais

## ✅ Boas Práticas

- 🔐 Use sempre variáveis de ambiente
- 🔐 Gere SECRET_KEY únicas para cada ambiente
- 🔐 Nunca commite arquivos .env
- 🔐 Use senhas fortes em produção
- 🔐 Mantenha dependências atualizadas
- 🔐 Monitore logs de segurança

---

**Lembre-se: Segurança em primeiro lugar!** 🛡️ 