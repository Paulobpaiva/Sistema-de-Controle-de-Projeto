from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

# Configurar o admin padrão do Django
admin.site.site_header = "Administração do Sistema CP"
admin.site.site_title = "Administração do Sistema CP"
admin.site.index_title = "Bem-vindo à Administração do Sistema CP"

# Personalizar o site admin (opcional, para uso futuro)
class SistemaCPAdminSite(AdminSite):
    # Títulos personalizados
    site_header = _("Administração do Sistema CP")
    site_title = _("Administração do Sistema CP")
    index_title = _("Bem-vindo à Administração do Sistema CP")
    
    # Configurações adicionais
    site_url = "/dashboard/"  # Link para voltar ao sistema principal
    enable_nav_sidebar = True

# Criar instância personalizada do admin (para uso futuro)
admin_site = SistemaCPAdminSite(name='sistema_cp_admin')

# Registrar os modelos padrão do Django
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin) 