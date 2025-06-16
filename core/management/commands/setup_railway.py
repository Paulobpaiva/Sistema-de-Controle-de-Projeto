from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
from core.models import Worker
from activities.models import Activity
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Configura dados iniciais para deploy no Railway'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Configurando dados iniciais no Railway...'))
        
        # Executar migrações
        try:
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('✅ Migrações executadas com sucesso'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro nas migrações: {e}'))
            return
        
        # Coletar arquivos estáticos
        try:
            call_command('collectstatic', '--noinput')
            self.stdout.write(self.style.SUCCESS('✅ Arquivos estáticos coletados'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro ao coletar arquivos estáticos: {e}'))
        
        # Criar superusuário
        self.create_superuser()
        
        # Criar perfil de worker
        self.create_worker_profile()
        
        # Criar dados de exemplo
        self.create_sample_data()
        
        self.stdout.write(self.style.SUCCESS('🎉 Configuração concluída com sucesso!'))
        self.stdout.write('📧 Login: admin')
        self.stdout.write('🔑 Senha: 1234')

    def create_superuser(self):
        """Criar superusuário se não existir"""
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@controleprojetos.com',
                password='1234'
            )
            self.stdout.write(self.style.SUCCESS("✅ Superusuário 'admin' criado com sucesso!"))
        else:
            self.stdout.write("ℹ️ Superusuário 'admin' já existe")

    def create_worker_profile(self):
        """Criar perfil de worker para o admin"""
        try:
            admin_user = User.objects.get(username='admin')
            worker, created = Worker.objects.get_or_create(
                user=admin_user,
                defaults={
                    'name': 'Administrador',
                    'email': 'admin@controleprojetos.com',
                    'phone': '(11) 99999-9999',
                    'role': 'Gerente',
                    'department': 'TI',
                    'is_active': True
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS("✅ Perfil de worker criado para o admin"))
            else:
                self.stdout.write("ℹ️ Perfil de worker já existe para o admin")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erro ao criar perfil de worker: {e}"))

    def create_sample_data(self):
        """Criar dados de exemplo"""
        try:
            # Criar algumas atividades de exemplo
            if Activity.objects.count() == 0:
                activities = [
                    {
                        'title': 'Desenvolvimento do Sistema',
                        'description': 'Desenvolvimento do sistema de controle de projetos',
                        'status': 'em_andamento',
                        'priority': 'alta',
                        'start_date': datetime.now().date(),
                        'end_date': (datetime.now() + timedelta(days=30)).date(),
                    },
                    {
                        'title': 'Testes de Qualidade',
                        'description': 'Realizar testes de qualidade do sistema',
                        'status': 'pendente',
                        'priority': 'media',
                        'start_date': datetime.now().date(),
                        'end_date': (datetime.now() + timedelta(days=15)).date(),
                    }
                ]
                
                for activity_data in activities:
                    Activity.objects.create(**activity_data)
                
                self.stdout.write(self.style.SUCCESS("✅ Dados de exemplo criados"))
            else:
                self.stdout.write("ℹ️ Dados de exemplo já existem")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Erro ao criar dados de exemplo: {e}")) 