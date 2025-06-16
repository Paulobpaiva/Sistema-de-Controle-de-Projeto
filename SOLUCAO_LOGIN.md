# 🔧 Solução para Problema de Login

## ❌ Problema Identificado
O usuário admin não está conseguindo fazer login com as credenciais fornecidas.

## ✅ Solução Manual

### Passo 1: Abrir o Terminal/Prompt de Comando
1. Pressione `Win + R`
2. Digite `cmd` e pressione Enter
3. Navegue até a pasta do projeto:
   ```cmd
   cd "C:\Users\Paulo Paiva\Downloads\controle de prj"
   ```

### Passo 2: Ativar o Ambiente Virtual
```cmd
venv\Scripts\activate
```

### Passo 3: Criar o Usuário Admin
Execute o comando:
```cmd
python manage.py shell
```

### Passo 4: No Shell do Django, Cole o Código:
```python
from django.contrib.auth.models import User

# Criar usuário admin
admin_user = User.objects.create_user(
    username='admin',
    email='admin@example.com',
    password='1234',
    first_name='Administrador',
    last_name='Sistema',
    is_staff=True,
    is_superuser=True,
    is_active=True
)

print("Usuário admin criado com sucesso!")
print("Usuário: admin")
print("Senha: 1234")
```

### Passo 5: Sair do Shell
```python
exit()
```

### Passo 6: Iniciar o Servidor
```cmd
python manage.py runserver
```

### Passo 7: Acessar o Sistema
- Abra o navegador
- Acesse: http://localhost:8000
- Use as credenciais:
  - **Usuário**: admin
  - **Senha**: 1234

## 🔄 Alternativa: Se o Usuário Já Existe

Se aparecer erro de usuário já existente, use este código no shell:

```python
from django.contrib.auth.models import User

# Buscar usuário existente
admin_user = User.objects.get(username='admin')

# Atualizar senha e permissões
admin_user.set_password('1234')
admin_user.is_active = True
admin_user.is_staff = True
admin_user.is_superuser = True
admin_user.save()

print("Senha do usuário admin atualizada!")
print("Usuário: admin")
print("Senha: 1234")
```

## 🎯 Resultado Esperado

Após seguir os passos, você deve conseguir:
1. Fazer login com admin/1234
2. Acessar o dashboard
3. Ver todas as funcionalidades do sistema

## 🆘 Se Ainda Não Funcionar

1. **Verifique se o ambiente virtual está ativo** (deve aparecer `(venv)` no início da linha)
2. **Verifique se está na pasta correta** (deve ter o arquivo `manage.py`)
3. **Tente recriar o banco de dados**:
   ```cmd
   python manage.py flush --noinput
   python manage.py migrate
   ```
   E depois repita os passos acima.

## 📞 Suporte

Se ainda houver problemas, verifique:
- Se o Python está instalado corretamente
- Se o Django está instalado no ambiente virtual
- Se não há erros no terminal ao executar os comandos

---

**🎉 Após resolver, o sistema estará 100% funcional!** 