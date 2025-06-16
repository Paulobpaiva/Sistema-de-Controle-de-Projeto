from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from activities.models import Worker

class Command(BaseCommand):
    help = 'Cria um usuário administrador padrão'

    def handle(self, *args, **options):
        try:
            # Verificar se o usuário admin já existe
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@example.com',
                    'first_name': 'Administrador',
                    'last_name': 'Sistema',
                    'is_staff': True,
                    'is_superuser': True,
                    'is_active': True
                }
            )
            
            if created:
                # Definir senha
                admin_user.set_password('1234')
                admin_user.save()
                self.stdout.write(
                    self.style.SUCCESS('✅ Usuário admin criado com sucesso!')
                )
            else:
                # Atualizar senha se o usuário já existe
                admin_user.set_password('1234')
                admin_user.is_active = True
                admin_user.is_staff = True
                admin_user.is_superuser = True
                admin_user.save()
                self.stdout.write(
                    self.style.SUCCESS('✅ Senha do usuário admin atualizada!')
                )
            
            # Criar Worker para o admin
            worker, worker_created = Worker.objects.get_or_create(
                user=admin_user,
                defaults={
                    'level': 'admin',
                    'department': 'TI',
                    'phone': '(11) 99999-9999'
                }
            )
            
            if worker_created:
                self.stdout.write(
                    self.style.SUCCESS('✅ Perfil de Worker criado para admin!')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS('✅ Perfil de Worker já existe para admin!')
                )
            
            self.stdout.write(
                self.style.SUCCESS('\n🔑 Credenciais de acesso:')
            )
            self.stdout.write('   Usuário: admin')
            self.stdout.write('   Senha: 1234')
            self.stdout.write('   URL: http://localhost:8000')
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Erro ao criar usuário admin: {e}')
            ) 