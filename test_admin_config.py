#!/usr/bin/env python
"""
Script para testar as configurações do admin
"""

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib import admin

def test_admin_config():
    print("🔧 Testando Configurações do Admin")
    print("=" * 40)
    
    print(f"Site Header: {admin.site.site_header}")
    print(f"Site Title: {admin.site.site_title}")
    print(f"Index Title: {admin.site.index_title}")
    
    print("\n✅ Configurações aplicadas com sucesso!")
    print("🌐 Acesse: http://localhost:8000/admin/")
    print("📝 Você verá 'Administração do Sistema CP' no lugar de 'Administração do Django'")

if __name__ == "__main__":
    test_admin_config() 