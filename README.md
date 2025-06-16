# Sistema de Controle de Projetos

Um sistema moderno de gestão de projetos desenvolvido em Django com interface responsiva e dashboard interativo.

## 🚀 Funcionalidades

### ✅ Sistema de Autenticação
- Login/Logout com "Lembrar-me"
- Registro de novos usuários
- Perfis de usuário com níveis (Admin, Gerente, Colaborador)
- Recuperação de senha

### 📊 Dashboard Interativo
- KPIs em tempo real
- Gráficos interativos com Plotly
- Progresso visual das ações
- Atividades recentes e atrasadas
- Animações e transições suaves

### 🎯 Gestão de Atividades
- CRUD completo de atividades
- Status personalizáveis (Não iniciado, Em andamento, Concluído, Pausado)
- Prioridades (Baixa, Média, Alta, Urgente)
- Registro de tempo gasto
- Comentários em atividades
- Filtros avançados

### 📈 Relatórios
- Relatório detalhado de atividades
- Relatório de tempo por trabalhador
- Exportação de dados
- Gráficos interativos

### 👥 Gestão de Usuários
- Níveis de acesso (Admin, Gerente, Colaborador)
- Departamentos
- Informações de contato

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Gráficos**: Plotly
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Ícones**: Font Awesome 6
- **Formulários**: Django Crispy Forms, Widget Tweaks

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd controle-de-prj
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py migrate
```

### 5. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 6. Execute o servidor
```bash
python manage.py runserver
```

## 🔧 Configuração

### Banco de Dados PostgreSQL (Opcional)
Para usar PostgreSQL em produção, edite `project/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "controle_projetos",
        "USER": "postgres",
        "PASSWORD": "sua_senha",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 🎨 Design System

### Cores Principais
- **Primária**: #1A2B50 (Azul profundo)
- **Secundária**: #00F5A0 (Verde elétrico)
- **Accent**: #4ECDC4 (Turquesa)
- **Sucesso**: #96CEB4 (Verde claro)
- **Aviso**: #FFE66D (Amarelo)
- **Perigo**: #FF6B6B (Vermelho)

### Tipografia
- **Fonte**: Inter (Google Fonts)
- **Pesos**: 300, 400, 500, 600, 700

## 📱 Responsividade

O sistema é totalmente responsivo e funciona em:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🔐 Segurança

- Autenticação baseada em sessões
- Proteção CSRF
- Validação de formulários
- Controle de acesso por níveis
- Senhas criptografadas

## 📊 Estrutura do Projeto

```
controle-de-prj/
├── project/              # Configurações do Django
├── core/                 # App principal
├── accounts/             # Autenticação e usuários
├── activities/           # Gestão de atividades
├── dashboard/            # Visualizações e relatórios
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── accounts/         # Templates de autenticação
│   ├── activities/       # Templates de atividades
│   └── dashboard/        # Templates do dashboard
├── static/               # Arquivos estáticos
├── requirements.txt      # Dependências
└── manage.py            # Script de gerenciamento
```

## 🚀 Uso Rápido

### 1. Acesse o sistema
- URL: http://localhost:8000
- Usuário: admin
- Senha: 1234

### 2. Complete seu perfil
- Acesse "Perfil" no menu
- Preencha as informações adicionais

### 3. Crie uma ação
- Vá para "Ações" no menu
- Clique em "Nova Ação"
- Preencha os dados

### 4. Crie atividades
- Vá para "Atividades" no menu
- Clique em "Nova Atividade"
- Associe à ação criada

### 5. Visualize o dashboard
- Acesse o dashboard principal
- Veja os KPIs e gráficos
- Acompanhe o progresso

## 📈 Funcionalidades Avançadas

### Registro de Tempo
- Registre o tempo gasto em cada atividade
- Visualize relatórios de produtividade
- Acompanhe horas estimadas vs. reais

### Comentários
- Adicione comentários às atividades
- Mantenha histórico de discussões
- Colabore com a equipe

### Filtros e Busca
- Filtre atividades por status, prioridade, ação
- Busque por nome ou descrição
- Visualize atividades atrasadas

## 🔧 Personalização

### Adicionar Novos Status
Edite `activities/models.py`:

```python
STATUS_CHOICES = [
    ('not_started', 'Não Iniciado'),
    ('in_progress', 'Em Andamento'),
    ('completed', 'Concluído'),
    ('paused', 'Pausado'),
    ('cancelled', 'Cancelado'),  # Novo status
]
```

### Adicionar Novos Níveis
Edite `activities/models.py`:

```python
LEVEL_CHOICES = [
    ('admin', 'Administrador'),
    ('manager', 'Gerente'),
    ('collaborator', 'Colaborador'),
    ('intern', 'Estagiário'),  # Novo nível
]
```

## 🐛 Solução de Problemas

### Erro de Migração
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erro de Dependências
```bash
pip install --upgrade -r requirements.txt
```

### Erro de Banco de Dados
```bash
python manage.py flush  # Limpa o banco
python manage.py migrate  # Recria as tabelas
```

## 📞 Suporte

Para suporte ou dúvidas:
- Abra uma issue no repositório
- Consulte a documentação do Django
- Verifique os logs do servidor

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👑 Superusuário e Painel Administrativo

- O sistema já vem com um superusuário padrão:
  - **Usuário:** admin
  - **Senha:** 1234
- Acesse o painel administrativo em: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- No painel admin, você pode:
  - Aprovar, bloquear, editar e excluir usuários
  - Promover usuários a staff/admin
  - Gerenciar permissões e grupos
  - Visualizar e editar todos os dados do sistema

### Aprovação manual de novos usuários (opcional)
Se desejar que novos usuários só possam acessar após aprovação, basta marcar o campo "Ativo" (is_active) no admin.

---

**Desenvolvido com ❤️ usando Django e Bootstrap** 