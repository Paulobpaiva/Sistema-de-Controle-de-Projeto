from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import connection
from activities.models import Activity, Action, Worker
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Configurar dados iniciais para deploy no Render'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forçar recriação de dados existentes',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Configurando dados iniciais no Render...'))
        
        # Verificar conexão com banco
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                self.stdout.write(self.style.SUCCESS('✅ Conexão com banco: OK'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro na conexão com banco: {e}'))
            return
        
        # Executar migrações
        try:
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('✅ Migrações executadas'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro nas migrações: {e}'))
            return
        
        # Coletar arquivos estáticos
        try:
            call_command('collectstatic', '--noinput')
            self.stdout.write(self.style.SUCCESS('✅ Arquivos estáticos coletados'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro nos arquivos estáticos: {e}'))
        
        # Orientar criação manual do superusuário
        self.stdout.write(self.style.WARNING('⚠️  Crie o superusuário manualmente com: python manage.py createsuperuser'))
        
        # Criar perfil de worker para admin (opcional, pode ser removido se depender do admin)
        # Dados de exemplo
        if Activity.objects.count() == 0 or options['force']:
            try:
                # Criar ações de exemplo
                actions = [
                    Action.objects.get_or_create(
                        name='Desenvolvimento do Sistema',
                        defaults={
                            'description': 'Desenvolvimento do sistema de controle de projetos',
                            'status': 'em_andamento',
                            'priority': 'alta',
                            'start_date': datetime.now().date(),
                            'end_date': (datetime.now() + timedelta(days=30)).date(),
                        }
                    )[0],
                    Action.objects.get_or_create(
                        name='Testes de Qualidade',
                        defaults={
                            'description': 'Realizar testes de qualidade do sistema',
                            'status': 'pendente',
                            'priority': 'media',
                            'start_date': datetime.now().date(),
                            'end_date': (datetime.now() + timedelta(days=15)).date(),
                        }
                    )[0]
                ]
                
                # Criar atividades de exemplo
                for action in actions:
                    Activity.objects.get_or_create(
                        title=f'Atividade para {action.name}',
                        defaults={
                            'description': f'Atividade relacionada a {action.name}',
                            'action': action,
                            'status': 'pendente',
                            'priority': 'media',
                            'start_date': datetime.now().date(),
                            'end_date': (datetime.now() + timedelta(days=7)).date(),
                        }
                    )
                
                self.stdout.write(self.style.SUCCESS('✅ Dados de exemplo criados'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Erro ao criar dados de exemplo: {e}'))
        else:
            self.stdout.write(self.style.WARNING('ℹ️ Dados de exemplo já existem'))
        
        self.stdout.write(self.style.SUCCESS('🎉 Configuração concluída com sucesso!')) 